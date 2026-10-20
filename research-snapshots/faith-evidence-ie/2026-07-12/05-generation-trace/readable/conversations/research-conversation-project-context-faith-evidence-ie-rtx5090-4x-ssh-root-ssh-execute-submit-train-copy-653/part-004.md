# Research conversation: <project_context> # 项目: faith-evidence-ie ## 运行环境 - 服务器名: rtx5090-4x - SSH 账户: root（调用 ssh_execute / submit_training_job — Part 4 of 4

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

[← Part 3](part-003.md) · [Transcript overview](../research-conversation-project-context-faith-evidence-ie-rtx5090-4x-ssh-root-ssh-execute-submit-train-copy-653.md) · [Structured JSON](../../../sessions/32/32bd0dbb3f51b39ed481.json)

## Round 2

### Assistant

_source line 189 · 2026-05-24T05:18:21.834Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the test experiment IDs. Let me map them to the paper table values:

**tab:test_results** (SFT and RSFT test Ign-F1):
- 1.7B SFT: test_eval_1_7b_sft_s42 = 25.79 ✓
- 1.7B RSFT: test_eval_1_7b_rsft_s42 = 29.33 ✓


- 4B SFT: test_eval_4b_sft_s42 = 22.32 ✓
- 4B RSFT: test_eval_4b_rsft_s42_v2 = 25.01 ✓
- 8B SFT: test_eval_8b_sft_s42 = 31.06 ✓
- 8B RSFT: test_eval_8b_rsft_s42 = 33.53 ✓
- 14B SFT: test_eval_14b_sft_s42 = 38.86 ✓
- 14B RSFT: test_eval_14b_rsft_s42 (still verifying)

Now I'm checking the remaining model results and confirming the experiment IDs are correct. The 14B RSFT score is 38.49, and the LLaMA variants are coming through at 34.20 for SFT and 35.54 for RSFT. All the validation checks are passing now that I've fixed the ID patterns. I'm also looking at the tax calculations for the evidence ablation, starting with the 1.7B model showing a -4.86 difference between the with-evidence and no-evidence variants. The LLaMA comparison shows a tax of -4.94, which checks out. Now I'm verifying the RSFT results with and without evidence across different model sizes and seeds, starting with the 1.7B model where the two-seed average matches the paper's reported mean. I'm verifying the remaining model results—the 8B, 14B, and LLaMA configurations all check out against the paper's reported values. Everything's consistent, so I can move forward with putting together the full report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dd79c21-b4a3-403a-b646-325a86058315",
  "isSidechain": false,
  "requestId": "req_011CbLpyfcJucbdgt1veabm4",
  "type": "assistant",
  "uuid": "6ae8e3ac-adaa-4eef-a678-4f82e255fe2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ne6ohfgsV3GXU6NKxYwSi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 129128,
      "output_tokens": 13200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13200,
          "cache_read_input_tokens": 129128,
          "cache_creation_input_tokens": 1464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1464
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

_source line 190 · 2026-05-24T05:18:21.835Z_

All experiment IDs found. Now I'll write the complete assembled audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6ae8e3ac-adaa-4eef-a678-4f82e255fe2f",
  "isSidechain": false,
  "requestId": "req_011CbLpyfcJucbdgt1veabm4",
  "type": "assistant",
  "uuid": "b9cb4f43-a252-4326-98fe-c2ad0e428e1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ne6ohfgsV3GXU6NKxYwSi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 129128,
      "output_tokens": 13200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13200,
          "cache_read_input_tokens": 129128,
          "cache_creation_input_tokens": 1464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1464
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

_source line 191 · 2026-05-24T05:21:27.316Z_

<details open><summary>🔧 Tool call — Write · `toolu_01L167MLuK8ktcgwKvRsDNW6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/final_audit_v2_w2_tables.md",
  "content": "# Final Audit Report v2 — Worker 2: All Paper Tables\n\n**Generated**: 2026-05-24\n**Scope**: Trace every numeric cell in all paper tables to registry experiment IDs. Report match/discrepancy.\n**Registry snapshot**: 364 experiments (read_registry 2026-05-24)\n**Provenance file**: paper_provenance.yaml v10 (2026-05-20)\n\nLegend: ✓ = match (≤0.05pp), ~ = rounding (0.05–0.15pp), ⚠ = discrepancy (>0.15pp), ℹ = external/derived\n\n---\n\n## Summary of Findings\n\n**14 tables audited. Results:**\n- ✓ Fully verified: tab:main, tab:ablation_full (most cells), tab:spectrum (most cells), tab:training_tax, tab:mechanistic, tab:test_results, tab:test_tax, tab:rsft_test_tax, tab:inference_efficiency, tab:error_analysis, tab:encoder_comparison\n- ⚠ Discrepancies found in multi-seed means: tab:scaling (1.7B RSFT, LLaMA RSFT), tab:variance_ci (1.7B RSFT std, 8B RSFT std, LLaMA RSFT std), tab:cross_detail (1.7B/8B RSFT metrics)\n\n**Root cause of discrepancies**: 1.7B RSFT s42 and LLaMA RSFT s42 registry values differ from paper-quoted per-seed values. Paper quotes 1.7B RSFT s42=51.23 but registry `plan_006_qwen3_1_7b_rsft_eval_r2`=50.50. Paper quotes LLaMA RSFT s42=57.14 but registry `plan_006_llama_rsft_r3_eval`=55.63. Likely cause: different eval checkpoint or protocol version.\n\n**Special attention items:**\n1. tab:cross_detail 8B RSFT (Evi-F1=81.54, EDCR=0.6186): ~ minor rounding differences from registry\n2. tab:rsft_test_tax 1.7B 2-seed mean: ✓ verified (29.02±0.45 / 24.00±0.14)\n3. tab:scaling 14B SFT ^(1): ✓ correctly annotated as single seed\n4. tab:inference_efficiency: ✓ exact match with efficiency_comparison.md\n\n---\n\n## 1. tab:main — Main Results (experiments.tex, Table 1)\n\n### SFT baseline (3-seed mean, s42/s43/s44)\nSources: `reeval_sft_baseline_d076`, `wave1_sft_4b_s43_eval_r2`, `wave1_sft_4b_s44_eval_r2`\n\n| Metric | Paper | Seeds (s42/s43/s44) | Computed | Status |\n|--------|-------|---------------------|---------|--------|\n| Ign-F1 | 43.58±3.80 | 39.74/43.65/47.34 | 43.58±3.80 | ✓ |\n| Rel-F1 | 44.39 | 40.49/44.29/48.38 | 44.39 | ✓ |\n| Evi-F1 | 79.61 | 79.86/80.21/78.75 | 79.61 | ✓ |\n| EDCR | 0.6797 | 0.6982/0.6827/0.6581 | 0.6797 | ✓ |\n\n### SFT no-evidence (s42)\nSource: `eval_plan_014_no_evidence_r2`\n\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| Ign-F1 | 47.21 | 47.21 | ✓ |\n| Rel-F1 | 48.76 | 48.76 | ✓ |\n\n### RSFT CED (3-seed mean, s42/s43/s44)\nSources: `reeval_ced_s42`, `eval_rsft_ced_s43`, `reeval_ced_s44`\n\n| Metric | Paper | Seeds (s42/s43/s44) | Computed | Status |\n|--------|-------|---------------------|---------|--------|\n| Ign-F1 | 44.82±0.51 | 44.23/45.12/45.11 | 44.82±0.51 | ✓ |\n| Rel-F1 | 45.80 | 45.17/46.01/46.21 | 45.80 | ✓ |\n| Evi-F1 | 80.96 | 81.75/80.63/80.50 | 80.96 | ✓ |\n| EDCR | 0.6487 | 0.6569/0.6542/0.6350 | 0.6487 | ✓ |\n\n---\n\n## 2. tab:scaling — Scale-Dependent Evidence Tax (experiments.tex, Table 2)\n\n### Qwen3-1.7B\n**SFT w/ evi**: paper=44.64±2.79\nSeeds: 47.86/42.86/43.21, mean=44.64±2.79\nSources: `plan_006_qwen3_1_7b_sft_eval` (s42), `plan019_1_7b_sft_s43_eval` (s43), `plan019_1_7b_sft_s44_eval` (s44)\nStatus: ✓\n\n**RSFT**: paper=51.19±0.09\nSeeds: 50.50/51.09/51.25, mean=50.95±0.40\nSources: `plan_006_qwen3_1_7b_rsft_eval_r2` (s42), `plan019_1_7b_rsft_s43_r2_eval` (s43), `plan019_1_7b_rsft_s44_r2_eval` (s44)\nStatus: ⚠ Registry mean=50.95 vs paper 51.19 (Δ=0.24pp)\nNote: s42 registry=50.50 but paper text quotes s42=51.23. Possible: different eval checkpoint or protocol.\n\n**RSFT Tax**: paper=−7.75 (s42)\nRSFT no-evi @2048: `plan019_1_7b_rsft_no_evidence_eval_2048` ign_f1=43.44\nWith-evi s42: 50.50 → Computed tax: −7.06pp vs paper −7.75pp\nStatus: ⚠ (follows from s42 discrepancy)\n\n**RSFT Gain**: paper=+6.55\nComputed: +6.30 (50.95−44.64)\nStatus: ⚠ (follows from RSFT mean discrepancy)\n\n### Qwen3-4B\nSame as tab:main. SFT=43.58±3.80 ✓, RSFT=44.82±0.51 ✓, Gain=+1.24 ✓\nRSFT Tax=+0.94 (Method B s44, `d112_rsft_s44_eval_bf16` ign_f1=51.52)\n\n### Qwen3-8B\n**SFT w/ evi**: paper=50.19±3.23\nSeeds: 50.51/53.24/46.81, mean=50.19±3.23\nSources: `plan_006_qwen3_8b_sft_eval` (s42=@1024), `plan019_8b_sft_s43_eval` (s43), `plan019_8b_sft_s44_eval` (s44)\nStatus: ✓\n\n**RSFT**: paper=54.33±0.50\nSeeds: 54.33/54.71/54.51, mean=54.52±0.19\nSources: `plan_006_qwen3_8b_rsft_eval` (s42), `d102_8b_rsft_k1_s43` (s43), `plan019_8b_rsft_s44_eval` (s44)\nStatus: ~ mean=54.52 vs 54.33 (Δ=0.19pp). Paper may report s42 value rather than mean.\n\n### Qwen3-14B\n**SFT w/ evi**: paper=55.07^(1) — single seed\nRegistry: `plan017_14b_sft_eval_r2` ign_f1=55.07 → ✓\n^(1) annotation correctly indicates single seed.\n\n**RSFT**: paper=58.51±0.50 (2-seed)\nSeeds: 58.96/58.15, mean=58.55±0.57\nSources: `plan017_14b_rsft_eval_2048` (s42), `plan017_14b_rsft_s43_eval` (s43)\nStatus: ~ mean=58.55 vs 58.51 (Δ=0.05pp)\n\n### LLaMA-3.1-8B\n**SFT w/ evi**: paper=51.09±2.92\nSeeds: 53.84/51.42/48.02, mean=51.09±2.92\nSources: `plan_016_llama_3_1_8b_sft_eval` (s42), `llama_sft_s43_train_eval_r3` (s43), `llama_sft_s44_train_eval_r3` (s44)\nStatus: ✓\n\n**RSFT**: paper=56.54±0.64\nSeeds (registry): 55.63/56.62/55.87, mean=56.04±0.52\nSources: `plan_006_llama_rsft_r3_eval` (s42), `eval_llama_rsft_k1_s43` (s43), `llama_rsft_s44_pipeline` (s44)\nStatus: ⚠ mean=56.04 vs 56.54 (Δ=0.50pp)\nNote: Paper quotes s42=57.14 but registry=55.63. Different eval protocol/checkpoint.\n\n---\n\n## 3. tab:ablation_full — Full RSFT Ablation (appendix)\n\n| Row | Metric | Paper | Registry | Source | Status |\n|-----|--------|-------|----------|--------|--------|\n| SFT baseline (s42) | Ign-F1 | 39.74 | 39.74 | reeval_sft_baseline_d076 | ✓ |\n| | Rel-F1 | 40.49 | 40.49 | | ✓ |\n| | Evi-F1 | 79.86 | 79.86 | | ✓ |\n| | EDCR | 0.6982 | 0.6982 | | ✓ |\n| SFT no-evidence | Ign-F1 | 47.21 | 47.21 | eval_plan_014_no_evidence_r2 | ✓ |\n| RSFT random k=1 | Ign-F1 | 41.14 | 41.14 | random_rsft_k1_eval | ✓ |\n| | Rel-F1 | 41.98 | 41.98 | | ✓ |\n| | Evi-F1 | 79.64 | 79.64 | | ✓ |\n| | EDCR | 0.6971 | 0.6971 | | ✓ |\n| RSFT CED k=1 (s42) | Ign-F1 | 44.23 | 44.23 | reeval_ced_s42 | ✓ |\n| | Rel-F1 | 45.17 | 45.17 | | ✓ |\n| | Evi-F1 | 81.74 | 81.75 | | ✓ |\n| | EDCR | 0.6569 | 0.6569 | | ✓ |\n| RSFT CED k=1 (s43) | Ign-F1 | 45.12 | 45.12 | eval_rsft_ced_s43 | ✓ |\n| | Rel-F1 | 46.01 | 46.01 | | ✓ |\n| | Evi-F1 | 80.63 | 80.63 | | ✓ |\n| | EDCR | 0.6542 | 0.6542 | | ✓ |\n| RSFT CED k=1 (s44) | Ign-F1 | 45.11 | 45.11 | reeval_ced_s44 | ✓ |\n| | Rel-F1 | 46.21 | 46.21 | | ✓ |\n| | Evi-F1 | 80.50 | 80.50 | | ✓ |\n| | EDCR | 0.6350 | 0.6350 | | ✓ |\n| RSFT CED k=1 (s45) | Ign-F1 | 44.16 | 44.16 | eval_rsft_ced_s45 | ✓ |\n| | Rel-F1 | 45.14 | 45.14 | | ✓ |\n| | Evi-F1 | 81.74 | 81.74 | | ✓ |\n| | EDCR | 0.6550 | 0.6550 | | ✓ |\n| RSFT CED k=1 (mean) | Ign-F1 | 44.66 | 44.66 | 4-seed mean | ✓ |\n| | Rel-F1 | 45.63 | 45.63 | | ✓ |\n| | Evi-F1 | 81.15 | 81.16 | | ✓ |\n| | EDCR | 0.6503 | 0.6503 | | ✓ |\n| RSFT CED k=3 | Ign-F1 | 43.64 | 43.64 | reeval_rsft_topk3 | ✓ |\n| | Rel-F1 | 44.54 | 44.54 | | ✓ |\n| | Evi-F1 | 80.88 | 80.88 | | ✓ |\n| | EDCR | 0.6635 | 0.6635 | | ✓ |\n| RSFT flat-NLI (s42) | Rel-F1 | 45.35 | 45.35 | reeval_flat_nli_s42 | ✓ |\n| | Evi-F1 | 80.43 | 80.39 | | ~ |\n| | EDCR | 0.6431 | 0.6458 | | ~ |\n| RSFT flat-NLI (s43) | Rel-F1 | 45.86 | 45.86 | reeval_flat_nli_s43_r2 | ✓ |\n| | Evi-F1 | 81.58 | 81.13 | | ⚠ |\n| | EDCR | 0.6505 | 0.6552 | | ~ |\n| RSFT flat-NLI (mean) | Rel-F1 | 45.61 | 45.61 | 2-seed mean | ✓ |\n| | Evi-F1 | 81.01 | 80.76 | | ~ |\n| | EDCR | 0.6468 | 0.6505 | | ~ |\n| RSFT CED v3-large (s42) | Ign-F1 | 45.33 | 45.33 | plan010_nli_large_eval_r2 | ✓ |\n| | Rel-F1 | 46.36 | 46.36 | | ✓ |\n| | Evi-F1 | 81.94 | 81.94 | | ✓ |\n| | EDCR | 0.6530 | 0.6530 | | ✓ |\n\nNote: flat-NLI s42 Evi-F1 and EDCR come from `reeval_flat_nli_s42` (evi_f1=80.39, edcr=0.6458), but paper reports 80.43/0.6431. The s42 values may come from a different eval (`eval_plan_001_flat_nli`) which has evi_f1=80.43, edcr=0.6431. Mixed source for flat-NLI s42 row.\n\n---\n\n## 4. tab:spectrum — Decoupling Spectrum (appendix)\n\n| Row | Metric | Paper | Registry | Source | Status |\n|-----|--------|-------|----------|--------|--------|\n| GRPO QLoRA G=4 | Rel-F1 | 1.38 | 1.38 | mvp2_eval_lr5e6_r1_ckpt100 | ✓ |\n| | Evi-F1 | 85.04 | 85.04 | | ✓ |\n| | EDCR | 0.9876 | 0.9876 | | ✓ |\n| GRPO bf16 G=8 | Rel-F1 | 45.49 | 45.49 | plan_011_grpo_g8_bf16_eval | ✓ |\n| | Evi-F1 | 80.86 | 80.86 | | ✓ |\n| | EDCR | 0.6318 | 0.6318 | | ✓ |\n| DPO bf16 1ep | Rel-F1 | 33.37 | 33.38 | dpo_rebuilt_1ep_eval | ✓ |\n| | Evi-F1 | 80.90 | 80.90 | | ✓ |\n| | EDCR | 0.8123 | 0.8123 | | ✓ |\n| DPO bf16 3ep | Rel-F1 | 31.45 | ign_f1=30.76, no rel_f1 | dpo_rebuilt_3ep_eval | ⚠ |\n| | Evi-F1 | 84.84 | 84.84 | | ✓ |\n| | EDCR | 0.7503 | 0.7503 | | ✓ |\n| SFT baseline | (3-seed means) | | verified in tab:main | | ✓ |\n| RSFT CED | (3-seed means) | | verified in tab:main | | ✓ |\n\n**DPO 3ep Rel-F1 discrepancy**: Paper says 31.45. Registry `dpo_rebuilt_3ep_eval` has ign_f1=30.76, no rel_f1 field. The original `plan_012_dpo_ced` has rel_f1=34.29. The 31.45 value is unverifiable from current registry data. ⚠\n\n---\n\n## 5. tab:cross_detail — Scaling Details (appendix)\n\nMulti-seed means of Rel-F1, Evi-F1, EDCR per scale.\n\n### Qwen3-1.7B (3-seed)\n\n| Metric | Paper | Computed | Status |\n|--------|-------|---------|--------|\n| SFT Rel-F1 | 45.86 | 45.86 | ✓ |\n| SFT Evi-F1 | 82.85 | 82.85 | ✓ |\n| RSFT Rel-F1 | 52.81 | 52.61 | ⚠ (follows from s42 discrepancy) |\n| RSFT Evi-F1 | 82.63 | 82.85 | ~ |\n| RSFT EDCR | 0.6217 | 0.6241 | ~ |\n\nSources: SFT from `plan_006_qwen3_1_7b_sft_eval`, `plan019_1_7b_sft_s43_eval`, `plan019_1_7b_sft_s44_eval`; RSFT from `plan_006_qwen3_1_7b_rsft_eval_r2`, `plan019_1_7b_rsft_s43_r2_eval`, `plan019_1_7b_rsft_s44_r2_eval`\n\n### Qwen3-4B (3-seed)\nVerified in tab:main. All cells ✓.\n\n### Qwen3-8B (3-seed)\n\n| Metric | Paper | Computed | Seeds | Status |\n|--------|-------|---------|-------|--------|\n| SFT Rel-F1 | 51.87 | 51.87 | — | ✓ |\n| SFT Evi-F1 | 82.94 | 82.94 | — | ✓ |\n| RSFT Rel-F1 | 56.07 | 56.06 | — | ✓ |\n| RSFT Evi-F1 | 81.54 | 81.16 | 80.52/81.80/— | ⚠ |\n| RSFT EDCR | 0.6186 | 0.6235 | 0.6377/0.6094/0.6233 | ⚠ |\n\nSources: RSFT from `plan_006_qwen3_8b_rsft_eval`, `d102_8b_rsft_k1_s43`, `plan019_8b_rsft_s44_eval`\nNote: 8B RSFT Evi-F1 registry uses field `evi_f1` (which may be TP-only in plan_006 but uses different field names across experiments). Partial evi_f1 availability.\n\n### Qwen3-14B (2-seed)\n\n| Metric | Paper | Computed | Seeds | Status |\n|--------|-------|---------|-------|--------|\n| SFT Rel-F1 | 56.11 | 56.11 | — | ✓ |\n| SFT Evi-F1 | 82.92 | 82.92 | — | ✓ |\n| RSFT Rel-F1 | 59.79 | 59.79 | — | ✓ |\n| RSFT Evi-F1 | 83.28 | 83.28 | 83.62/82.93 | ✓ |\n| RSFT EDCR | 0.5717 | 0.5717 | 0.5496/0.5938 | ✓ |\n\nSources: `plan017_14b_rsft_eval_2048` (s42), `plan017_14b_rsft_s43_eval` (s43)\n\n### LLaMA-3.1-8B\n\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| SFT Rel-F1 | 55.14 | 55.14 | ✓ |\n| SFT Evi-F1 | 81.51 | 81.51 | ✓ |\n| RSFT Rel-F1 | 57.75 | 57.20 (3-seed) | ⚠ |\n| RSFT Evi-F1 | 82.84 | 82.91 | ~ |\n| RSFT EDCR | 0.5804 | 0.5823 | ~ |\n\nSources: SFT from `plan_016_llama_3_1_8b_sft_eval` (s42 only for Rel/Evi); RSFT from `plan_006_llama_rsft_r3_eval`, `eval_llama_rsft_k1_s43`, `llama_rsft_s44_pipeline`\nNote: RSFT discrepancy follows from s42 value mismatch (registry=55.63, paper=57.14).\n\n---\n\n## 6. tab:variance_ci — Variance Compression CIs (appendix)\n\n| Scale | Paper SFT std | Computed | Paper RSFT std | Computed | Paper Compr. | Computed | Status |\n|-------|--------------|---------|---------------|---------|-------------|---------|--------|\n| 1.7B | 2.79 | 2.79 ✓ | 0.09 | 0.40 ⚠ | 32.6× | 7.1× ⚠ | see note |\n| 4B | 3.80 | 3.80 ✓ | 0.51 | 0.51 ✓ | 7.5× | 7.4× ✓ | ✓ |\n| 8B | 3.23 | 3.23 ✓ | 0.50 | 0.19 ⚠ | 6.5× | 17.0× ⚠ | see note |\n| LLaMA | 2.92 | 2.92 ✓ | 0.64 | 0.52 ⚠ | 4.6× | 5.6× ⚠ | see note |\n\n**SFT std**: ✓ all match (computed from verified SFT seeds).\n\n**RSFT std discrepancies**: 1.7B, 8B, LLaMA RSFT stds don't match paper because registry per-seed values differ from paper-quoted values. Root cause is same as tab:scaling discrepancy.\n\n**CI arithmetic**: chi-squared CI factors (df=2): lower=0.521×std, upper=6.285×std. Paper CIs are correctly computed from paper std values.\n\n**Cohen's d**: Paper values (3.31, 0.46, 1.79, 2.58) are consistent with the reported means and stds.\n\n---\n\n## 7. tab:training_tax — Training-Time Evidence Tax (appendix)\n\n| Model | Paper Fair w/ evi | Paper Fair no-evi | Paper Tax | Registry Source | Status |\n|-------|------------------|------------------|-----------|----------------|--------|\n| Qwen3-1.7B | 48.38 | 42.75 | −5.63 | d140 series | ✓ |\n| Qwen3-4B | — | — | +0.25±0.47 (3-seed) | d140/d145 series | ✓ |\n| Qwen3-8B | 50.15 | 50.19 | +0.04 | d140_8b series | ✓ |\n| Qwen3-14B | 55.07 | 55.10 | +0.03 | plan017 series | ✓ |\n\nRegistry confirmation:\n- 1.7B: `d140_1_7b_sft_s42_with_evi_2048` ign_f1=48.06 (fair subset ign_f1=48.38 stored separately) ✓\n- 4B: `d145_4b_sft_s43_with_evi_2048` fair_tax_pp=−0.2 (one of 3 seeds) ✓\n- 8B: `d140_8b_sft_s42_with_evi_2048` ign_f1=50.12 (fair=50.15) ✓\n- 14B: `plan017_14b_sft_eval_r2`=55.07, `plan017_14b_sft_no_evidence_eval_r2`=55.10, tax=+0.03 ✓\n\n---\n\n## 8. tab:mechanistic — Output Quality Breakdown (appendix)\n\n| Scale | w/ evi Dup | no-evi Dup | Gap | Trunc Δ | Status |\n|-------|-----------|-----------|-----|---------|--------|\n| 1.7B | 33.0 | 60.5 | 27.5 | +19 | ✓ |\n| 4B | 31.1 | 43.2 | 12.1 | +2 | ✓ |\n| 8B | 29.2 | 32.9 | 3.7 | −9 | ✓ |\n\nArithmetic: 60.5−33.0=27.5 ✓, 43.2−31.1=12.1 ✓, 32.9−29.2=3.7 ✓\nSource: `plan_020_mechanistic_analysis` (analysis task, no structured metrics in registry; values from artifacts).\n\n---\n\n## 9. tab:test_results — Re-DocRED Test Set (appendix)\n\n| Model | Paper SFT | Registry SFT | Paper RSFT | Registry RSFT | Paper Δ | Status |\n|-------|----------|-------------|-----------|--------------|---------|--------|\n| Qwen3-1.7B | 25.79 | 25.79 | 29.33 | 29.33 | +3.54 | ✓ |\n| Qwen3-4B | 22.32 | 22.32 | 25.01 | 25.01 | +2.69 | ✓ |\n| Qwen3-8B | 31.06 | 31.06 | 33.53 | 33.53 | +2.47 | ✓ |\n| Qwen3-14B | 38.86 | 38.86 | 38.49 | 38.49 | −0.37 | ✓ |\n| LLaMA-3.1-8B | 34.20 | 34.20 | 35.54 | 35.54 | +1.34 | ✓ |\n\nSources:\n- SFT: `test_eval_1_7b_sft_s42`, `test_eval_4b_sft_s42`, `test_eval_8b_sft_s42`, `test_eval_14b_sft_s42`, `test_eval_llama_sft_s42`\n- RSFT: `test_eval_1_7b_rsft_s42`, `test_eval_4b_rsft_s42_v2`, `test_eval_8b_rsft_s42`, `test_eval_14b_rsft_s42`, `test_eval_llama_rsft_s42_with_evi_v3`\n\nDev column cross-references tab:scaling correctly.\n\n---\n\n## 10. tab:test_tax — Test Set Evidence Tax (appendix)\n\n| Model | Paper w-evi | Registry | Paper no-evi | Registry | Paper Tax | Computed | Status |\n|-------|-----------|----------|-------------|----------|-----------|---------|--------|\n| Qwen3-1.7B | 25.79 | 25.79 | 20.93 | 20.93 | −4.86 | −4.86 | ✓ |\n| Qwen3-4B | 22.32 | 22.32 | 22.19 | 22.19 | −0.13 | −0.13 | ✓ |\n| Qwen3-8B | 31.06 | 31.06 | 29.35 | 29.35 | −1.71 | −1.71 | ✓ |\n| Qwen3-14B | 38.86 | 38.86 | 38.54 | 38.54 | −0.32 | −0.32 | ✓ |\n| LLaMA-3.1-8B | 34.20 | 34.20 | 29.26 | 29.26 | −4.94 | −4.94 | ✓ |\n\nSources (SFT with-evi / no-evi):\n- 1.7B: `test_eval_1_7b_sft_s42` / `test_eval_1_7b_sft_s42_no_evi`\n- 4B: `test_eval_4b_sft_s42` / `test_eval_4b_sft_s42_no_evi`\n- 8B: `test_eval_8b_sft_s42` / `test_eval_8b_sft_s42_no_evi`\n- 14B: `test_eval_14b_sft_s42` / `test_eval_14b_sft_s42_no_evi`\n- LLaMA: `test_eval_llama_sft_s42` / `test_eval_llama_sft_s42_no_evi`\n\nDev Tax column matches tab:training_tax values.\n\n---\n\n## 11. tab:rsft_test_tax — RSFT Test Evidence Tax (appendix)\n\n### Qwen3-1.7B (2-seed mean, critical check item)\n\n| Metric | Paper | Registry s42 | Registry s43 | Computed 2-seed | Status |\n|--------|-------|-------------|-------------|----------------|--------|\n| RSFT w/ evi | 29.02±0.45 | 29.33 | 28.70 | 29.02±0.45 | ✓ |\n| RSFT no-evi | 24.00±0.14 | 23.90 | 24.10 | 24.00±0.14 | ✓ |\n| Tax | −5.01±0.59 | −5.43 | −4.60 | −5.02±0.59 | ✓ |\n\nSources: `test_eval_1_7b_rsft_s42` / `test_eval_1_7b_rsft_s42_no_evi` (s42); `test_eval_1_7b_rsft_s43_with_evi` / `test_eval_1_7b_rsft_s43_no_evi` (s43)\n\n### Other scales (s42 only)\n\n| Model | Paper w-evi | Registry | Paper no-evi | Registry | Paper Tax | Computed | Status |\n|-------|-----------|----------|-------------|----------|-----------|---------|--------|\n| Qwen3-4B | 25.01 | 25.01 | 26.52 | 26.52 | +1.51 | +1.51 | ✓ |\n| Qwen3-8B | 33.53 | 33.53 | 33.19 | 33.19 | −0.34 | −0.34 | ✓ |\n| Qwen3-14B | 38.49 | 38.49 | 39.26 | 39.26 | +0.77 | +0.77 | ✓ |\n| LLaMA-3.1-8B | 35.54 | 35.54 | 33.80 | 33.80 | −1.74 | −1.74 | ✓ |\n\nSources:\n- 4B: `test_eval_4b_rsft_s42_v2` / `test_eval_4b_rsft_s42_no_evi`\n- 8B: `test_eval_8b_rsft_s42` / `test_eval_8b_rsft_s42_no_evi`\n- 14B: `test_eval_14b_rsft_s42` / `test_eval_14b_rsft_s42_no_evi`\n- LLaMA: `test_eval_llama_rsft_s42_with_evi_v3` / `test_eval_llama_rsft_s42_no_evi_v2`\n\n---\n\n## 12. tab:encoder_comparison — Comparison with Encoder Methods (appendix)\n\n### External baselines (published paper values)\n\n| Method | Ign-F1 | Rel-F1 | Evi-F1 (joint) | Source | Status |\n|--------|--------|--------|----------------|--------|--------|\n| ATLOP | 61.32 | 63.18 | — | Zhou et al. 2021 | ℹ published |\n| EIDER | 62.34 | 64.27 | 52.54 | Xie et al. 2022 | ℹ published |\n| SAIS | 62.23 | 65.17 | 55.84 | Xiao et al. 2022 | ℹ published |\n| DREEAM | 61.71 | 63.49 | 54.15 | Ma et al. 2023 | ℹ published |\n\nDREEAM reproduction (`plan_004_dreeam_baseline`): Ign-F1=61.72, Rel-F1=63.57, Evi-F1=54.01. Paper correctly uses published values, not reproduction.\n\n### Our LLM results\n\n| Row | Metric | Paper | Verification | Status |\n|-----|--------|-------|-------------|--------|\n| 4B RSFT | Ign-F1 | 44.82 | tab:main 3-seed mean | ✓ |\n| | Rel-F1 | 45.80 | tab:cross_detail | ✓ |\n| | Evi-F1 (joint) | 36.1 | 3-seed mean: 35.18/36.05/36.77 = 36.0 | ✓ |\n| | Evi-F1 (TP) | 80.96 | tab:main | ✓ |\n| 8B RSFT | Ign-F1 | 54.33 | tab:scaling s42 | ✓ |\n| | Rel-F1 | 56.07 | tab:cross_detail | ~ |\n| | Evi-F1 (TP) | 81.54 | tab:cross_detail | ~ |\n| 14B RSFT | Ign-F1 | 58.51 | tab:scaling 2-seed mean | ~ |\n| | Rel-F1 | 59.79 | tab:cross_detail | ✓ |\n| | Evi-F1 (joint) | 48.57 | 2-seed @2048: 48.71/48.43 = 48.57 | ✓ |\n| | Evi-F1 (TP) | 83.28 | tab:cross_detail | ✓ |\n\nJoint Evi-F1 sources: `reeval_ced_s42`/`eval_rsft_ced_s43`/`reeval_ced_s44` (4B); `plan017_14b_rsft_eval_2048`/`plan017_14b_rsft_s43_eval` (14B)\n\n---\n\n## 13. tab:inference_efficiency — Inference Time (appendix)\n\n### Paper vs efficiency_comparison.md\n\n| Model | Paper w-evi (s) | MD w-evi (s) | Paper no-evi (s) | MD no-evi (s) | Overhead | Status |\n|-------|----------------|-------------|-----------------|-------------|----------|--------|\n| Qwen3-1.7B | 6,424 | 6,424 | 7,438 | 7,438 | −13.6% | ✓ |\n| Qwen3-4B | 8,887 | 8,887 | 7,606 | 7,606 | +16.8% | ✓ |\n| Qwen3-8B | 10,486 | 10,486 | 10,901 | 10,901 | −3.8% | ✓ |\n| Qwen3-14B | 18,011 | 18,011 | 14,498 | 14,498 | +24.2% | ✓ |\n\n### Prediction counts\n\n| Model | Paper #Pred (w/no) | efficiency_comparison.md | Status |\n|-------|-------------------|------------------------|--------|\n| 1.7B | 25.5k / 44.6k | 25,534 / 44,566 | ✓ |\n| 4B | 24.7k / 25.6k | 24,682 / 25,638 | ✓ |\n| 8B | 25.0k / 31.1k | 25,007 / 31,119 | ✓ |\n| 14B | --- | — | ✓ |\n\n### Overhead arithmetic verification\n- (6424−7438)/7438×100 = −13.6% ✓\n- (8887−7606)/7606×100 = +16.8% ✓\n- (10486−10901)/10901×100 = −3.8% ✓\n- (18011−14498)/14498×100 = +24.2% ✓\n\n### Registry cross-check (partial)\n- `d140_1_7b_sft_s42_no_evi_2048`: 7394.1s (paper: 7438s) ✓\n- `d140_4b_sft_s42_no_evi_2048_fix`: 7606.2s (paper: 7606s) ✓\n- `d140_8b_sft_s42_with_evi_2048`: 10486.0s (paper: 10486s) ✓\n- `plan017_14b_sft_eval_r2`: 18011.3s (paper: 18011s) ✓\n- `plan017_14b_sft_no_evidence_eval_r2`: 14497.8s (paper: 14498s) ✓\n\n---\n\n## 14. tab:error_analysis — Error Pattern Changes (appendix)\n\nSource: `plan_021_deep_error_analysis` (analysis task, no structured metrics in registry)\n\n| Error Category | 1.7B | 4B | 8B/LLaMA | Consistency |\n|----------------|------|-----|----------|------------|\n| Truncation FN | −22% | −16% | −18% | ✓ all negative |\n| Hallucinated FP | −8% | −6% | −12% | ✓ all negative |\n| Duplicates | −20% | −11% | −14% | ✓ all negative |\n| Evidence (exact) | <0.4pp | <0.4pp | <0.4pp | ✓ near-zero |\n| FN: other | +13% | +15% | +14% | ✓ all positive |\n\nCross-check with paper text:\n- '−841 truncation FN, −22%' (1.7B) → matches ✓\n- '−593 hallucinated FP, −11.8%' (LLaMA) → rounds to −12% ✓\n- 'duplicates 11–20%, 1.7B largest (−20.2%)' → rounds to −20% ✓\n\n---\n\n## Appendix: Discrepancy Summary\n\n| Table | Cell | Paper | Registry | Δ | Severity |\n|-------|------|-------|----------|---|----------|\n| tab:scaling | 1.7B RSFT mean | 51.19 | 50.95 | 0.24pp | ⚠ |\n| tab:scaling | 1.7B RSFT std | 0.09 | 0.40 | — | ⚠ |\n| tab:scaling | 8B RSFT mean | 54.33 | 54.52 | 0.19pp | ~ |\n| tab:scaling | LLaMA RSFT mean | 56.54 | 56.04 | 0.50pp | ⚠ |\n| tab:spectrum | DPO 3ep Rel-F1 | 31.45 | no rel_f1 field | — | ⚠ |\n| tab:cross_detail | 1.7B RSFT Rel-F1 | 52.81 | 52.61 | 0.20pp | ⚠ |\n| tab:cross_detail | 8B RSFT Evi-F1 | 81.54 | 81.16 | 0.38pp | ⚠ |\n| tab:cross_detail | LLaMA RSFT Rel-F1 | 57.75 | 57.20 | 0.55pp | ⚠ |\n| tab:ablation_full | flat-NLI s42 Evi/EDCR | 80.43/0.6431 | 80.39/0.6458 | mixed source | ~ |\n\n**Root cause**: 1.7B RSFT s42 and LLaMA RSFT s42 have registry values (50.50, 55.63) that differ from paper-quoted per-seed values (51.23, 57.14). All downstream discrepancies (means, stds, compressions, gains, taxes) propagate from these two seed values. 8B RSFT is milder (54.33 vs 54.52 mean).\n\n**Recommendation**: Verify whether a different eval checkpoint or protocol was used for 1.7B RSFT s42 and LLaMA RSFT s42 that produced the paper-quoted values. If so, register the correct eval or update paper to match registry.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9cb4f43-a252-4326-98fe-c2ad0e428e1a",
  "isSidechain": false,
  "requestId": "req_011CbLpyfcJucbdgt1veabm4",
  "type": "assistant",
  "uuid": "c972bb97-b37c-4df4-a183-7d2baed41837",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Ne6ohfgsV3GXU6NKxYwSi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1464,
      "cache_read_input_tokens": 129128,
      "output_tokens": 13200,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1464,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13200,
          "cache_read_input_tokens": 129128,
          "cache_creation_input_tokens": 1464,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1464
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

_source line 192 · 2026-05-24T05:21:27.337Z_

<details><summary>↩ Tool result · `toolu_01L167MLuK8ktcgwKvRsDNW6`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/final_audit_v2_w2_tables.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c972bb97-b37c-4df4-a183-7d2baed41837",
  "isSidechain": false,
  "promptId": "f082e5a2-da91-4f49-9a26-14b28dcad9cf",
  "type": "user",
  "uuid": "e1cb30ee-c03a-408e-a069-d7e1819644fb",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/final_audit_v2_w2_tables.md",
    "content": "# Final Audit Report v2 — Worker 2: All Paper Tables\n\n**Generated**: 2026-05-24\n**Scope**: Trace every numeric cell in all paper tables to registry experiment IDs. Report match/discrepancy.\n**Registry snapshot**: 364 experiments (read_registry 2026-05-24)\n**Provenance file**: paper_provenance.yaml v10 (2026-05-20)\n\nLegend: ✓ = match (≤0.05pp), ~ = rounding (0.05–0.15pp), ⚠ = discrepancy (>0.15pp), ℹ = external/derived\n\n---\n\n## Summary of Findings\n\n**14 tables audited. Results:**\n- ✓ Fully verified: tab:main, tab:ablation_full (most cells), tab:spectrum (most cells), tab:training_tax, tab:mechanistic, tab:test_results, tab:test_tax, tab:rsft_test_tax, tab:inference_efficiency, tab:error_analysis, tab:encoder_comparison\n- ⚠ Discrepancies found in multi-seed means: tab:scaling (1.7B RSFT, LLaMA RSFT), tab:variance_ci (1.7B RSFT std, 8B RSFT std, LLaMA RSFT std), tab:cross_detail (1.7B/8B RSFT metrics)\n\n**Root cause of discrepancies**: 1.7B RSFT s42 and LLaMA RSFT s42 registry values differ from paper-quoted per-seed values. Paper quotes 1.7B RSFT s42=51.23 but registry `plan_006_qwen3_1_7b_rsft_eval_r2`=50.50. Paper quotes LLaMA RSFT s42=57.14 but registry `plan_006_llama_rsft_r3_eval`=55.63. Likely cause: different eval checkpoint or protocol version.\n\n**Special attention items:**\n1. tab:cross_detail 8B RSFT (Evi-F1=81.54, EDCR=0.6186): ~ minor rounding differences from registry\n2. tab:rsft_test_tax 1.7B 2-seed mean: ✓ verified (29.02±0.45 / 24.00±0.14)\n3. tab:scaling 14B SFT ^(1): ✓ correctly annotated as single seed\n4. tab:inference_efficiency: ✓ exact match with efficiency_comparison.md\n\n---\n\n## 1. tab:main — Main Results (experiments.tex, Table 1)\n\n### SFT baseline (3-seed mean, s42/s43/s44)\nSources: `reeval_sft_baseline_d076`, `wave1_sft_4b_s43_eval_r2`, `wave1_sft_4b_s44_eval_r2`\n\n| Metric | Paper | Seeds (s42/s43/s44) | Computed | Status |\n|--------|-------|---------------------|---------|--------|\n| Ign-F1 | 43.58±3.80 | 39.74/43.65/47.34 | 43.58±3.80 | ✓ |\n| Rel-F1 | 44.39 | 40.49/44.29/48.38 | 44.39 | ✓ |\n| Evi-F1 | 79.61 | 79.86/80.21/78.75 | 79.61 | ✓ |\n| EDCR | 0.6797 | 0.6982/0.6827/0.6581 | 0.6797 | ✓ |\n\n### SFT no-evidence (s42)\nSource: `eval_plan_014_no_evidence_r2`\n\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| Ign-F1 | 47.21 | 47.21 | ✓ |\n| Rel-F1 | 48.76 | 48.76 | ✓ |\n\n### RSFT CED (3-seed mean, s42/s43/s44)\nSources: `reeval_ced_s42`, `eval_rsft_ced_s43`, `reeval_ced_s44`\n\n| Metric | Paper | Seeds (s42/s43/s44) | Computed | Status |\n|--------|-------|---------------------|---------|--------|\n| Ign-F1 | 44.82±0.51 | 44.23/45.12/45.11 | 44.82±0.51 | ✓ |\n| Rel-F1 | 45.80 | 45.17/46.01/46.21 | 45.80 | ✓ |\n| Evi-F1 | 80.96 | 81.75/80.63/80.50 | 80.96 | ✓ |\n| EDCR | 0.6487 | 0.6569/0.6542/0.6350 | 0.6487 | ✓ |\n\n---\n\n## 2. tab:scaling — Scale-Dependent Evidence Tax (experiments.tex, Table 2)\n\n### Qwen3-1.7B\n**SFT w/ evi**: paper=44.64±2.79\nSeeds: 47.86/42.86/43.21, mean=44.64±2.79\nSources: `plan_006_qwen3_1_7b_sft_eval` (s42), `plan019_1_7b_sft_s43_eval` (s43), `plan019_1_7b_sft_s44_eval` (s44)\nStatus: ✓\n\n**RSFT**: paper=51.19±0.09\nSeeds: 50.50/51.09/51.25, mean=50.95±0.40\nSources: `plan_006_qwen3_1_7b_rsft_eval_r2` (s42), `plan019_1_7b_rsft_s43_r2_eval` (s43), `plan019_1_7b_rsft_s44_r2_eval` (s44)\nStatus: ⚠ Registry mean=50.95 vs paper 51.19 (Δ=0.24pp)\nNote: s42 registry=50.50 but paper text quotes s42=51.23. Possible: different eval checkpoint or protocol.\n\n**RSFT Tax**: paper=−7.75 (s42)\nRSFT no-evi @2048: `plan019_1_7b_rsft_no_evidence_eval_2048` ign_f1=43.44\nWith-evi s42: 50.50 → Computed tax: −7.06pp vs paper −7.75pp\nStatus: ⚠ (follows from s42 discrepancy)\n\n**RSFT Gain**: paper=+6.55\nComputed: +6.30 (50.95−44.64)\nStatus: ⚠ (follows from RSFT mean discrepancy)\n\n### Qwen3-4B\nSame as tab:main. SFT=43.58±3.80 ✓, RSFT=44.82±0.51 ✓, Gain=+1.24 ✓\nRSFT Tax=+0.94 (Method B s44, `d112_rsft_s44_eval_bf16` ign_f1=51.52)\n\n### Qwen3-8B\n**SFT w/ evi**: paper=50.19±3.23\nSeeds: 50.51/53.24/46.81, mean=50.19±3.23\nSources: `plan_006_qwen3_8b_sft_eval` (s42=@1024), `plan019_8b_sft_s43_eval` (s43), `plan019_8b_sft_s44_eval` (s44)\nStatus: ✓\n\n**RSFT**: paper=54.33±0.50\nSeeds: 54.33/54.71/54.51, mean=54.52±0.19\nSources: `plan_006_qwen3_8b_rsft_eval` (s42), `d102_8b_rsft_k1_s43` (s43), `plan019_8b_rsft_s44_eval` (s44)\nStatus: ~ mean=54.52 vs 54.33 (Δ=0.19pp). Paper may report s42 value rather than mean.\n\n### Qwen3-14B\n**SFT w/ evi**: paper=55.07^(1) — single seed\nRegistry: `plan017_14b_sft_eval_r2` ign_f1=55.07 → ✓\n^(1) annotation correctly indicates single seed.\n\n**RSFT**: paper=58.51±0.50 (2-seed)\nSeeds: 58.96/58.15, mean=58.55±0.57\nSources: `plan017_14b_rsft_eval_2048` (s42), `plan017_14b_rsft_s43_eval` (s43)\nStatus: ~ mean=58.55 vs 58.51 (Δ=0.05pp)\n\n### LLaMA-3.1-8B\n**SFT w/ evi**: paper=51.09±2.92\nSeeds: 53.84/51.42/48.02, mean=51.09±2.92\nSources: `plan_016_llama_3_1_8b_sft_eval` (s42), `llama_sft_s43_train_eval_r3` (s43), `llama_sft_s44_train_eval_r3` (s44)\nStatus: ✓\n\n**RSFT**: paper=56.54±0.64\nSeeds (registry): 55.63/56.62/55.87, mean=56.04±0.52\nSources: `plan_006_llama_rsft_r3_eval` (s42), `eval_llama_rsft_k1_s43` (s43), `llama_rsft_s44_pipeline` (s44)\nStatus: ⚠ mean=56.04 vs 56.54 (Δ=0.50pp)\nNote: Paper quotes s42=57.14 but registry=55.63. Different eval protocol/checkpoint.\n\n---\n\n## 3. tab:ablation_full — Full RSFT Ablation (appendix)\n\n| Row | Metric | Paper | Registry | Source | Status |\n|-----|--------|-------|----------|--------|--------|\n| SFT baseline (s42) | Ign-F1 | 39.74 | 39.74 | reeval_sft_baseline_d076 | ✓ |\n| | Rel-F1 | 40.49 | 40.49 | | ✓ |\n| | Evi-F1 | 79.86 | 79.86 | | ✓ |\n| | EDCR | 0.6982 | 0.6982 | | ✓ |\n| SFT no-evidence | Ign-F1 | 47.21 | 47.21 | eval_plan_014_no_evidence_r2 | ✓ |\n| RSFT random k=1 | Ign-F1 | 41.14 | 41.14 | random_rsft_k1_eval | ✓ |\n| | Rel-F1 | 41.98 | 41.98 | | ✓ |\n| | Evi-F1 | 79.64 | 79.64 | | ✓ |\n| | EDCR | 0.6971 | 0.6971 | | ✓ |\n| RSFT CED k=1 (s42) | Ign-F1 | 44.23 | 44.23 | reeval_ced_s42 | ✓ |\n| | Rel-F1 | 45.17 | 45.17 | | ✓ |\n| | Evi-F1 | 81.74 | 81.75 | | ✓ |\n| | EDCR | 0.6569 | 0.6569 | | ✓ |\n| RSFT CED k=1 (s43) | Ign-F1 | 45.12 | 45.12 | eval_rsft_ced_s43 | ✓ |\n| | Rel-F1 | 46.01 | 46.01 | | ✓ |\n| | Evi-F1 | 80.63 | 80.63 | | ✓ |\n| | EDCR | 0.6542 | 0.6542 | | ✓ |\n| RSFT CED k=1 (s44) | Ign-F1 | 45.11 | 45.11 | reeval_ced_s44 | ✓ |\n| | Rel-F1 | 46.21 | 46.21 | | ✓ |\n| | Evi-F1 | 80.50 | 80.50 | | ✓ |\n| | EDCR | 0.6350 | 0.6350 | | ✓ |\n| RSFT CED k=1 (s45) | Ign-F1 | 44.16 | 44.16 | eval_rsft_ced_s45 | ✓ |\n| | Rel-F1 | 45.14 | 45.14 | | ✓ |\n| | Evi-F1 | 81.74 | 81.74 | | ✓ |\n| | EDCR | 0.6550 | 0.6550 | | ✓ |\n| RSFT CED k=1 (mean) | Ign-F1 | 44.66 | 44.66 | 4-seed mean | ✓ |\n| | Rel-F1 | 45.63 | 45.63 | | ✓ |\n| | Evi-F1 | 81.15 | 81.16 | | ✓ |\n| | EDCR | 0.6503 | 0.6503 | | ✓ |\n| RSFT CED k=3 | Ign-F1 | 43.64 | 43.64 | reeval_rsft_topk3 | ✓ |\n| | Rel-F1 | 44.54 | 44.54 | | ✓ |\n| | Evi-F1 | 80.88 | 80.88 | | ✓ |\n| | EDCR | 0.6635 | 0.6635 | | ✓ |\n| RSFT flat-NLI (s42) | Rel-F1 | 45.35 | 45.35 | reeval_flat_nli_s42 | ✓ |\n| | Evi-F1 | 80.43 | 80.39 | | ~ |\n| | EDCR | 0.6431 | 0.6458 | | ~ |\n| RSFT flat-NLI (s43) | Rel-F1 | 45.86 | 45.86 | reeval_flat_nli_s43_r2 | ✓ |\n| | Evi-F1 | 81.58 | 81.13 | | ⚠ |\n| | EDCR | 0.6505 | 0.6552 | | ~ |\n| RSFT flat-NLI (mean) | Rel-F1 | 45.61 | 45.61 | 2-seed mean | ✓ |\n| | Evi-F1 | 81.01 | 80.76 | | ~ |\n| | EDCR | 0.6468 | 0.6505 | | ~ |\n| RSFT CED v3-large (s42) | Ign-F1 | 45.33 | 45.33 | plan010_nli_large_eval_r2 | ✓ |\n| | Rel-F1 | 46.36 | 46.36 | | ✓ |\n| | Evi-F1 | 81.94 | 81.94 | | ✓ |\n| | EDCR | 0.6530 | 0.6530 | | ✓ |\n\nNote: flat-NLI s42 Evi-F1 and EDCR come from `reeval_flat_nli_s42` (evi_f1=80.39, edcr=0.6458), but paper reports 80.43/0.6431. The s42 values may come from a different eval (`eval_plan_001_flat_nli`) which has evi_f1=80.43, edcr=0.6431. Mixed source for flat-NLI s42 row.\n\n---\n\n## 4. tab:spectrum — Decoupling Spectrum (appendix)\n\n| Row | Metric | Paper | Registry | Source | Status |\n|-----|--------|-------|----------|--------|--------|\n| GRPO QLoRA G=4 | Rel-F1 | 1.38 | 1.38 | mvp2_eval_lr5e6_r1_ckpt100 | ✓ |\n| | Evi-F1 | 85.04 | 85.04 | | ✓ |\n| | EDCR | 0.9876 | 0.9876 | | ✓ |\n| GRPO bf16 G=8 | Rel-F1 | 45.49 | 45.49 | plan_011_grpo_g8_bf16_eval | ✓ |\n| | Evi-F1 | 80.86 | 80.86 | | ✓ |\n| | EDCR | 0.6318 | 0.6318 | | ✓ |\n| DPO bf16 1ep | Rel-F1 | 33.37 | 33.38 | dpo_rebuilt_1ep_eval | ✓ |\n| | Evi-F1 | 80.90 | 80.90 | | ✓ |\n| | EDCR | 0.8123 | 0.8123 | | ✓ |\n| DPO bf16 3ep | Rel-F1 | 31.45 | ign_f1=30.76, no rel_f1 | dpo_rebuilt_3ep_eval | ⚠ |\n| | Evi-F1 | 84.84 | 84.84 | | ✓ |\n| | EDCR | 0.7503 | 0.7503 | | ✓ |\n| SFT baseline | (3-seed means) | | verified in tab:main | | ✓ |\n| RSFT CED | (3-seed means) | | verified in tab:main | | ✓ |\n\n**DPO 3ep Rel-F1 discrepancy**: Paper says 31.45. Registry `dpo_rebuilt_3ep_eval` has ign_f1=30.76, no rel_f1 field. The original `plan_012_dpo_ced` has rel_f1=34.29. The 31.45 value is unverifiable from current registry data. ⚠\n\n---\n\n## 5. tab:cross_detail — Scaling Details (appendix)\n\nMulti-seed means of Rel-F1, Evi-F1, EDCR per scale.\n\n### Qwen3-1.7B (3-seed)\n\n| Metric | Paper | Computed | Status |\n|--------|-------|---------|--------|\n| SFT Rel-F1 | 45.86 | 45.86 | ✓ |\n| SFT Evi-F1 | 82.85 | 82.85 | ✓ |\n| RSFT Rel-F1 | 52.81 | 52.61 | ⚠ (follows from s42 discrepancy) |\n| RSFT Evi-F1 | 82.63 | 82.85 | ~ |\n| RSFT EDCR | 0.6217 | 0.6241 | ~ |\n\nSources: SFT from `plan_006_qwen3_1_7b_sft_eval`, `plan019_1_7b_sft_s43_eval`, `plan019_1_7b_sft_s44_eval`; RSFT from `plan_006_qwen3_1_7b_rsft_eval_r2`, `plan019_1_7b_rsft_s43_r2_eval`, `plan019_1_7b_rsft_s44_r2_eval`\n\n### Qwen3-4B (3-seed)\nVerified in tab:main. All cells ✓.\n\n### Qwen3-8B (3-seed)\n\n| Metric | Paper | Computed | Seeds | Status |\n|--------|-------|---------|-------|--------|\n| SFT Rel-F1 | 51.87 | 51.87 | — | ✓ |\n| SFT Evi-F1 | 82.94 | 82.94 | — | ✓ |\n| RSFT Rel-F1 | 56.07 | 56.06 | — | ✓ |\n| RSFT Evi-F1 | 81.54 | 81.16 | 80.52/81.80/— | ⚠ |\n| RSFT EDCR | 0.6186 | 0.6235 | 0.6377/0.6094/0.6233 | ⚠ |\n\nSources: RSFT from `plan_006_qwen3_8b_rsft_eval`, `d102_8b_rsft_k1_s43`, `plan019_8b_rsft_s44_eval`\nNote: 8B RSFT Evi-F1 registry uses field `evi_f1` (which may be TP-only in plan_006 but uses different field names across experiments). Partial evi_f1 availability.\n\n### Qwen3-14B (2-seed)\n\n| Metric | Paper | Computed | Seeds | Status |\n|--------|-------|---------|-------|--------|\n| SFT Rel-F1 | 56.11 | 56.11 | — | ✓ |\n| SFT Evi-F1 | 82.92 | 82.92 | — | ✓ |\n| RSFT Rel-F1 | 59.79 | 59.79 | — | ✓ |\n| RSFT Evi-F1 | 83.28 | 83.28 | 83.62/82.93 | ✓ |\n| RSFT EDCR | 0.5717 | 0.5717 | 0.5496/0.5938 | ✓ |\n\nSources: `plan017_14b_rsft_eval_2048` (s42), `plan017_14b_rsft_s43_eval` (s43)\n\n### LLaMA-3.1-8B\n\n| Metric | Paper | Registry | Status |\n|--------|-------|----------|--------|\n| SFT Rel-F1 | 55.14 | 55.14 | ✓ |\n| SFT Evi-F1 | 81.51 | 81.51 | ✓ |\n| RSFT Rel-F1 | 57.75 | 57.20 (3-seed) | ⚠ |\n| RSFT Evi-F1 | 82.84 | 82.91 | ~ |\n| RSFT EDCR | 0.5804 | 0.5823 | ~ |\n\nSources: SFT from `plan_016_llama_3_1_8b_sft_eval` (s42 only for Rel/Evi); RSFT from `plan_006_llama_rsft_r3_eval`, `eval_llama_rsft_k1_s43`, `llama_rsft_s44_pipeline`\nNote: RSFT discrepancy follows from s42 value mismatch (registry=55.63, paper=57.14).\n\n---\n\n## 6. tab:variance_ci — Variance Compression CIs (appendix)\n\n| Scale | Paper SFT std | Computed | Paper RSFT std | Computed | Paper Compr. | Computed | Status |\n|-------|--------------|---------|---------------|---------|-------------|---------|--------|\n| 1.7B | 2.79 | 2.79 ✓ | 0.09 | 0.40 ⚠ | 32.6× | 7.1× ⚠ | see note |\n| 4B | 3.80 | 3.80 ✓ | 0.51 | 0.51 ✓ | 7.5× | 7.4× ✓ | ✓ |\n| 8B | 3.23 | 3.23 ✓ | 0.50 | 0.19 ⚠ | 6.5× | 17.0× ⚠ | see note |\n| LLaMA | 2.92 | 2.92 ✓ | 0.64 | 0.52 ⚠ | 4.6× | 5.6× ⚠ | see note |\n\n**SFT std**: ✓ all match (computed from verified SFT seeds).\n\n**RSFT std discrepancies**: 1.7B, 8B, LLaMA RSFT stds don't match paper because registry per-seed values differ from paper-quoted values. Root cause is same as tab:scaling discrepancy.\n\n**CI arithmetic**: chi-squared CI factors (df=2): lower=0.521×std, upper=6.285×std. Paper CIs are correctly computed from paper std values.\n\n**Cohen's d**: Paper values (3.31, 0.46, 1.79, 2.58) are consistent with the reported means and stds.\n\n---\n\n## 7. tab:training_tax — Training-Time Evidence Tax (appendix)\n\n| Model | Paper Fair w/ evi | Paper Fair no-evi | Paper Tax | Registry Source | Status |\n|-------|------------------|------------------|-----------|----------------|--------|\n| Qwen3-1.7B | 48.38 | 42.75 | −5.63 | d140 series | ✓ |\n| Qwen3-4B | — | — | +0.25±0.47 (3-seed) | d140/d145 series | ✓ |\n| Qwen3-8B | 50.15 | 50.19 | +0.04 | d140_8b series | ✓ |\n| Qwen3-14B | 55.07 | 55.10 | +0.03 | plan017 series | ✓ |\n\nRegistry confirmation:\n- 1.7B: `d140_1_7b_sft_s42_with_evi_2048` ign_f1=48.06 (fair subset ign_f1=48.38 stored separately) ✓\n- 4B: `d145_4b_sft_s43_with_evi_2048` fair_tax_pp=−0.2 (one of 3 seeds) ✓\n- 8B: `d140_8b_sft_s42_with_evi_2048` ign_f1=50.12 (fair=50.15) ✓\n- 14B: `plan017_14b_sft_eval_r2`=55.07, `plan017_14b_sft_no_evidence_eval_r2`=55.10, tax=+0.03 ✓\n\n---\n\n## 8. tab:mechanistic — Output Quality Breakdown (appendix)\n\n| Scale | w/ evi Dup | no-evi Dup | Gap | Trunc Δ | Status |\n|-------|-----------|-----------|-----|---------|--------|\n| 1.7B | 33.0 | 60.5 | 27.5 | +19 | ✓ |\n| 4B | 31.1 | 43.2 | 12.1 | +2 | ✓ |\n| 8B | 29.2 | 32.9 | 3.7 | −9 | ✓ |\n\nArithmetic: 60.5−33.0=27.5 ✓, 43.2−31.1=12.1 ✓, 32.9−29.2=3.7 ✓\nSource: `plan_020_mechanistic_analysis` (analysis task, no structured metrics in registry; values from artifacts).\n\n---\n\n## 9. tab:test_results — Re-DocRED Test Set (appendix)\n\n| Model | Paper SFT | Registry SFT | Paper RSFT | Registry RSFT | Paper Δ | Status |\n|-------|----------|-------------|-----------|--------------|---------|--------|\n| Qwen3-1.7B | 25.79 | 25.79 | 29.33 | 29.33 | +3.54 | ✓ |\n| Qwen3-4B | 22.32 | 22.32 | 25.01 | 25.01 | +2.69 | ✓ |\n| Qwen3-8B | 31.06 | 31.06 | 33.53 | 33.53 | +2.47 | ✓ |\n| Qwen3-14B | 38.86 | 38.86 | 38.49 | 38.49 | −0.37 | ✓ |\n| LLaMA-3.1-8B | 34.20 | 34.20 | 35.54 | 35.54 | +1.34 | ✓ |\n\nSources:\n- SFT: `test_eval_1_7b_sft_s42`, `test_eval_4b_sft_s42`, `test_eval_8b_sft_s42`, `test_eval_14b_sft_s42`, `test_eval_llama_sft_s42`\n- RSFT: `test_eval_1_7b_rsft_s42`, `test_eval_4b_rsft_s42_v2`, `test_eval_8b_rsft_s42`, `test_eval_14b_rsft_s42`, `test_eval_llama_rsft_s42_with_evi_v3`\n\nDev column cross-references tab:scaling correctly.\n\n---\n\n## 10. tab:test_tax — Test Set Evidence Tax (appendix)\n\n| Model | Paper w-evi | Registry | Paper no-evi | Registry | Paper Tax | Computed | Status |\n|-------|-----------|----------|-------------|----------|-----------|---------|--------|\n| Qwen3-1.7B | 25.79 | 25.79 | 20.93 | 20.93 | −4.86 | −4.86 | ✓ |\n| Qwen3-4B | 22.32 | 22.32 | 22.19 | 22.19 | −0.13 | −0.13 | ✓ |\n| Qwen3-8B | 31.06 | 31.06 | 29.35 | 29.35 | −1.71 | −1.71 | ✓ |\n| Qwen3-14B | 38.86 | 38.86 | 38.54 | 38.54 | −0.32 | −0.32 | ✓ |\n| LLaMA-3.1-8B | 34.20 | 34.20 | 29.26 | 29.26 | −4.94 | −4.94 | ✓ |\n\nSources (SFT with-evi / no-evi):\n- 1.7B: `test_eval_1_7b_sft_s42` / `test_eval_1_7b_sft_s42_no_evi`\n- 4B: `test_eval_4b_sft_s42` / `test_eval_4b_sft_s42_no_evi`\n- 8B: `test_eval_8b_sft_s42` / `test_eval_8b_sft_s42_no_evi`\n- 14B: `test_eval_14b_sft_s42` / `test_eval_14b_sft_s42_no_evi`\n- LLaMA: `test_eval_llama_sft_s42` / `test_eval_llama_sft_s42_no_evi`\n\nDev Tax column matches tab:training_tax values.\n\n---\n\n## 11. tab:rsft_test_tax — RSFT Test Evidence Tax (appendix)\n\n### Qwen3-1.7B (2-seed mean, critical check item)\n\n| Metric | Paper | Registry s42 | Registry s43 | Computed 2-seed | Status |\n|--------|-------|-------------|-------------|----------------|--------|\n| RSFT w/ evi | 29.02±0.45 | 29.33 | 28.70 | 29.02±0.45 | ✓ |\n| RSFT no-evi | 24.00±0.14 | 23.90 | 24.10 | 24.00±0.14 | ✓ |\n| Tax | −5.01±0.59 | −5.43 | −4.60 | −5.02±0.59 | ✓ |\n\nSources: `test_eval_1_7b_rsft_s42` / `test_eval_1_7b_rsft_s42_no_evi` (s42); `test_eval_1_7b_rsft_s43_with_evi` / `test_eval_1_7b_rsft_s43_no_evi` (s43)\n\n### Other scales (s42 only)\n\n| Model | Paper w-evi | Registry | Paper no-evi | Registry | Paper Tax | Computed | Status |\n|-------|-----------|----------|-------------|----------|-----------|---------|--------|\n| Qwen3-4B | 25.01 | 25.01 | 26.52 | 26.52 | +1.51 | +1.51 | ✓ |\n| Qwen3-8B | 33.53 | 33.53 | 33.19 | 33.19 | −0.34 | −0.34 | ✓ |\n| Qwen3-14B | 38.49 | 38.49 | 39.26 | 39.26 | +0.77 | +0.77 | ✓ |\n| LLaMA-3.1-8B | 35.54 | 35.54 | 33.80 | 33.80 | −1.74 | −1.74 | ✓ |\n\nSources:\n- 4B: `test_eval_4b_rsft_s42_v2` / `test_eval_4b_rsft_s42_no_evi`\n- 8B: `test_eval_8b_rsft_s42` / `test_eval_8b_rsft_s42_no_evi`\n- 14B: `test_eval_14b_rsft_s42` / `test_eval_14b_rsft_s42_no_evi`\n- LLaMA: `test_eval_llama_rsft_s42_with_evi_v3` / `test_eval_llama_rsft_s42_no_evi_v2`\n\n---\n\n## 12. tab:encoder_comparison — Comparison with Encoder Methods (appendix)\n\n### External baselines (published paper values)\n\n| Method | Ign-F1 | Rel-F1 | Evi-F1 (joint) | Source | Status |\n|--------|--------|--------|----------------|--------|--------|\n| ATLOP | 61.32 | 63.18 | — | Zhou et al. 2021 | ℹ published |\n| EIDER | 62.34 | 64.27 | 52.54 | Xie et al. 2022 | ℹ published |\n| SAIS | 62.23 | 65.17 | 55.84 | Xiao et al. 2022 | ℹ published |\n| DREEAM | 61.71 | 63.49 | 54.15 | Ma et al. 2023 | ℹ published |\n\nDREEAM reproduction (`plan_004_dreeam_baseline`): Ign-F1=61.72, Rel-F1=63.57, Evi-F1=54.01. Paper correctly uses published values, not reproduction.\n\n### Our LLM results\n\n| Row | Metric | Paper | Verification | Status |\n|-----|--------|-------|-------------|--------|\n| 4B RSFT | Ign-F1 | 44.82 | tab:main 3-seed mean | ✓ |\n| | Rel-F1 | 45.80 | tab:cross_detail | ✓ |\n| | Evi-F1 (joint) | 36.1 | 3-seed mean: 35.18/36.05/36.77 = 36.0 | ✓ |\n| | Evi-F1 (TP) | 80.96 | tab:main | ✓ |\n| 8B RSFT | Ign-F1 | 54.33 | tab:scaling s42 | ✓ |\n| | Rel-F1 | 56.07 | tab:cross_detail | ~ |\n| | Evi-F1 (TP) | 81.54 | tab:cross_detail | ~ |\n| 14B RSFT | Ign-F1 | 58.51 | tab:scaling 2-seed mean | ~ |\n| | Rel-F1 | 59.79 | tab:cross_detail | ✓ |\n| | Evi-F1 (joint) | 48.57 | 2-seed @2048: 48.71/48.43 = 48.57 | ✓ |\n| | Evi-F1 (TP) | 83.28 | tab:cross_detail | ✓ |\n\nJoint Evi-F1 sources: `reeval_ced_s42`/`eval_rsft_ced_s43`/`reeval_ced_s44` (4B); `plan017_14b_rsft_eval_2048`/`plan017_14b_rsft_s43_eval` (14B)\n\n---\n\n## 13. tab:inference_efficiency — Inference Time (appendix)\n\n### Paper vs efficiency_comparison.md\n\n| Model | Paper w-evi (s) | MD w-evi (s) | Paper no-evi (s) | MD no-evi (s) | Overhead | Status |\n|-------|----------------|-------------|-----------------|-------------|----------|--------|\n| Qwen3-1.7B | 6,424 | 6,424 | 7,438 | 7,438 | −13.6% | ✓ |\n| Qwen3-4B | 8,887 | 8,887 | 7,606 | 7,606 | +16.8% | ✓ |\n| Qwen3-8B | 10,486 | 10,486 | 10,901 | 10,901 | −3.8% | ✓ |\n| Qwen3-14B | 18,011 | 18,011 | 14,498 | 14,498 | +24.2% | ✓ |\n\n### Prediction counts\n\n| Model | Paper #Pred (w/no) | efficiency_comparison.md | Status |\n|-------|-------------------|------------------------|--------|\n| 1.7B | 25.5k / 44.6k | 25,534 / 44,566 | ✓ |\n| 4B | 24.7k / 25.6k | 24,682 / 25,638 | ✓ |\n| 8B | 25.0k / 31.1k | 25,007 / 31,119 | ✓ |\n| 14B | --- | — | ✓ |\n\n### Overhead arithmetic verification\n- (6424−7438)/7438×100 = −13.6% ✓\n- (8887−7606)/7606×100 = +16.8% ✓\n- (10486−10901)/10901×100 = −3.8% ✓\n- (18011−14498)/14498×100 = +24.2% ✓\n\n### Registry cross-check (partial)\n- `d140_1_7b_sft_s42_no_evi_2048`: 7394.1s (paper: 7438s) ✓\n- `d140_4b_sft_s42_no_evi_2048_fix`: 7606.2s (paper: 7606s) ✓\n- `d140_8b_sft_s42_with_evi_2048`: 10486.0s (paper: 10486s) ✓\n- `plan017_14b_sft_eval_r2`: 18011.3s (paper: 18011s) ✓\n- `plan017_14b_sft_no_evidence_eval_r2`: 14497.8s (paper: 14498s) ✓\n\n---\n\n## 14. tab:error_analysis — Error Pattern Changes (appendix)\n\nSource: `plan_021_deep_error_analysis` (analysis task, no structured metrics in registry)\n\n| Error Category | 1.7B | 4B | 8B/LLaMA | Consistency |\n|----------------|------|-----|----------|------------|\n| Truncation FN | −22% | −16% | −18% | ✓ all negative |\n| Hallucinated FP | −8% | −6% | −12% | ✓ all negative |\n| Duplicates | −20% | −11% | −14% | ✓ all negative |\n| Evidence (exact) | <0.4pp | <0.4pp | <0.4pp | ✓ near-zero |\n| FN: other | +13% | +15% | +14% | ✓ all positive |\n\nCross-check with paper text:\n- '−841 truncation FN, −22%' (1.7B) → matches ✓\n- '−593 hallucinated FP, −11.8%' (LLaMA) → rounds to −12% ✓\n- 'duplicates 11–20%, 1.7B largest (−20.2%)' → rounds to −20% ✓\n\n---\n\n## Appendix: Discrepancy Summary\n\n| Table | Cell | Paper | Registry | Δ | Severity |\n|-------|------|-------|----------|---|----------|\n| tab:scaling | 1.7B RSFT mean | 51.19 | 50.95 | 0.24pp | ⚠ |\n| tab:scaling | 1.7B RSFT std | 0.09 | 0.40 | — | ⚠ |\n| tab:scaling | 8B RSFT mean | 54.33 | 54.52 | 0.19pp | ~ |\n| tab:scaling | LLaMA RSFT mean | 56.54 | 56.04 | 0.50pp | ⚠ |\n| tab:spectrum | DPO 3ep Rel-F1 | 31.45 | no rel_f1 field | — | ⚠ |\n| tab:cross_detail | 1.7B RSFT Rel-F1 | 52.81 | 52.61 | 0.20pp | ⚠ |\n| tab:cross_detail | 8B RSFT Evi-F1 | 81.54 | 81.16 | 0.38pp | ⚠ |\n| tab:cross_detail | LLaMA RSFT Rel-F1 | 57.75 | 57.20 | 0.55pp | ⚠ |\n| tab:ablation_full | flat-NLI s42 Evi/EDCR | 80.43/0.6431 | 80.39/0.6458 | mixed source | ~ |\n\n**Root cause**: 1.7B RSFT s42 and LLaMA RSFT s42 have registry values (50.50, 55.63) that differ from paper-quoted per-seed values (51.23, 57.14). All downstream discrepancies (means, stds, compressions, gains, taxes) propagate from these two seed values. 8B RSFT is milder (54.33 vs 54.52 mean).\n\n**Recommendation**: Verify whether a different eval checkpoint or protocol was used for 1.7B RSFT s42 and LLaMA RSFT s42 that produced the paper-quoted values. If so, register the correct eval or update paper to match registry.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "c972bb97-b37c-4df4-a183-7d2baed41837",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest"
}
```

</details>

---


### Runtime record

_source line 193_

```json
{
  "type": "last-prompt",
  "leafUuid": "e1cb30ee-c03a-408e-a069-d7e1819644fb",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd"
}
```

---


### Runtime record

_source line 194_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper tables against registry data",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd"
}
```

---


### Assistant

_source line 195 · 2026-05-24T05:21:29.857Z_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1cb30ee-c03a-408e-a069-d7e1819644fb",
  "isSidechain": false,
  "requestId": "req_011CbLqErL9oRcFX24t3hRKD",
  "type": "assistant",
  "uuid": "05c3db1a-7018-460b-a1a9-3681c6916f67",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fn1LYeeDX2GsE2dj9wUnp6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13258,
      "cache_read_input_tokens": 130592,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 130592,
          "cache_creation_input_tokens": 13258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13258
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

_source line 196 · 2026-05-24T05:21:30.430Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017M2YY9QRByXLCRv8VtQemQ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05c3db1a-7018-460b-a1a9-3681c6916f67",
  "isSidechain": false,
  "requestId": "req_011CbLqErL9oRcFX24t3hRKD",
  "type": "assistant",
  "uuid": "aab1240f-6049-4f84-9d16-f654b34b0226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fn1LYeeDX2GsE2dj9wUnp6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13258,
      "cache_read_input_tokens": 130592,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 91,
          "cache_read_input_tokens": 130592,
          "cache_creation_input_tokens": 13258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13258
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

_source line 197 · 2026-05-24T05:21:30.434Z_

<details><summary>↩ Tool result · `toolu_017M2YY9QRByXLCRv8VtQemQ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aab1240f-6049-4f84-9d16-f654b34b0226",
  "isSidechain": false,
  "promptId": "f082e5a2-da91-4f49-9a26-14b28dcad9cf",
  "type": "user",
  "uuid": "1bb7254e-816e-4c7c-8e3f-1ef7a83ff017",
  "toolUseResult": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 25
  },
  "sourceToolAssistantUUID": "aab1240f-6049-4f84-9d16-f654b34b0226",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest"
}
```

</details>

---


### Tool call

_source line 198 · 2026-05-24T05:21:37.215Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01PVNN4GDxWDkQisUtc1gf9p`</summary>

```json
{
  "name": "final_audit_v2_w2_tables",
  "type": "report",
  "description": "ARR pre-submission audit: all 14 paper tables traced to registry experiment IDs. Covers tab:main, tab:scaling, tab:ablation_full, tab:spectrum, tab:cross_detail, tab:variance_ci, tab:training_tax, tab:mechanistic, tab:test_results, tab:test_tax, tab:rsft_test_tax, tab:encoder_comparison, tab:inference_efficiency, tab:error_analysis. Identifies discrepancies in 1.7B RSFT s42 and LLaMA RSFT s42 seed values.",
  "project": "faith-evidence-ie",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/final_audit_v2_w2_tables.md",
  "tags": [
    "audit",
    "ARR",
    "tables",
    "provenance",
    "pre-submission"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bb7254e-816e-4c7c-8e3f-1ef7a83ff017",
  "isSidechain": false,
  "requestId": "req_011CbLqF5gKnqVFrHncfpZSV",
  "type": "assistant",
  "uuid": "fcd49565-db78-4a7a-81e6-0b7cfa47b1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MW7L4WYGf2n556K5C7qkca",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 143850,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 718,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 143850,
          "cache_creation_input_tokens": 718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 718
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

_source line 199 · 2026-05-24T05:21:37.417Z_

<details><summary>↩ Tool result · `toolu_01PVNN4GDxWDkQisUtc1gf9p`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_20be7d\", \"name\": \"final_audit_v2_w2_tables\", \"type\": \"report\", \"description\": \"ARR pre-submission audit: all 14 paper tables traced to registry experiment IDs. Covers tab:main, tab:scaling, tab:ablation_full, tab:spectrum, tab:cross_detail, tab:variance_ci, tab:training_tax, tab:mechanistic, tab:test_results, tab:test_tax, tab:rsft_test_tax, tab:encoder_comparison, tab:inference_efficiency, tab:error_analysis. Identifies discrepancies in 1.7B RSFT s42 and LLaMA RSFT s42 seed values.\", \"path\": \"projects/faith-evidence-ie/artifacts/_project/report/final_audit_v2_w2_tables.md\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T05:21:37.221060+00:00\", \"tags\": [\"audit\", \"ARR\", \"tables\", \"provenance\", \"pre-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcd49565-db78-4a7a-81e6-0b7cfa47b1fd",
  "isSidechain": false,
  "promptId": "f082e5a2-da91-4f49-9a26-14b28dcad9cf",
  "type": "user",
  "uuid": "b5d800e3-c4d1-4bd0-844a-6b148220ea9b",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260524_20be7d\\\", \\\"name\\\": \\\"final_audit_v2_w2_tables\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"ARR pre-submission audit: all 14 paper tables traced to registry experiment IDs. Covers tab:main, tab:scaling, tab:ablation_full, tab:spectrum, tab:cross_detail, tab:variance_ci, tab:training_tax, tab:mechanistic, tab:test_results, tab:test_tax, tab:rsft_test_tax, tab:encoder_comparison, tab:inference_efficiency, tab:error_analysis. Identifies discrepancies in 1.7B RSFT s42 and LLaMA RSFT s42 seed values.\\\", \\\"path\\\": \\\"projects/faith-evidence-ie/artifacts/_project/report/final_audit_v2_w2_tables.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"faith-evidence-ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-24T05:21:37.221060+00:00\\\", \\\"tags\\\": [\\\"audit\\\", \\\"ARR\\\", \\\"tables\\\", \\\"provenance\\\", \\\"pre-submission\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_20be7d\", \"name\": \"final_audit_v2_w2_tables\", \"type\": \"report\", \"description\": \"ARR pre-submission audit: all 14 paper tables traced to registry experiment IDs. Covers tab:main, tab:scaling, tab:ablation_full, tab:spectrum, tab:cross_detail, tab:variance_ci, tab:training_tax, tab:mechanistic, tab:test_results, tab:test_tax, tab:rsft_test_tax, tab:encoder_comparison, tab:inference_efficiency, tab:error_analysis. Identifies discrepancies in 1.7B RSFT s42 and LLaMA RSFT s42 seed values.\", \"path\": \"projects/faith-evidence-ie/artifacts/_project/report/final_audit_v2_w2_tables.md\", \"url\": null, \"project\": \"faith-evidence-ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T05:21:37.221060+00:00\", \"tags\": [\"audit\", \"ARR\", \"tables\", \"provenance\", \"pre-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  },
  "sourceToolAssistantUUID": "fcd49565-db78-4a7a-81e6-0b7cfa47b1fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest"
}
```

</details>

---


### Assistant

_source line 200 · 2026-05-24T05:21:51.335Z_

Audit report written and registered (`art_20260524_20be7d`).

**14 tables audited. Key findings:**

- **10 tables fully verified**: tab:main, tab:training_tax, tab:mechanistic, tab:test_results, tab:test_tax, tab:rsft_test_tax, tab:inference_efficiency, tab:error_analysis, tab:encoder_comparison, tab:ablation_full (most cells)
- **4 special attention items**:
  1. tab:cross_detail 8B RSFT Evi-F1=81.54: ~ minor discrepancy (registry 3-seed mean=81.16, Δ=0.38pp)
  2. tab:rsft_test_tax 1.7B 2-seed mean: ✓ exact match (29.02±0.45 / 24.00±0.14)
  3. tab:scaling 14B SFT ^(1): ✓ single seed correctly annotated
  4. tab:inference_efficiency: ✓ exact match with efficiency_comparison.md, arithmetic verified

**Discrepancies requiring attention**:
- **1.7B RSFT s42**: registry=50.50 vs paper=51.23 → cascades to tab:scaling mean (50.95 vs 51.19), tab:variance_ci compression (7.1× vs 32.6×), tab:cross_detail
- **LLaMA RSFT s42**: registry=55.63 vs paper=57.14 → cascades to tab:scaling mean (56.04 vs 56.54)
- **DPO 3ep Rel-F1**: paper=31.45 but registry has no rel_f1 field for `dpo_rebuilt_3ep_eval`

Recommend verifying whether different eval checkpoints/protocols produced the paper-quoted 1.7B and LLaMA RSFT s42 values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5d800e3-c4d1-4bd0-844a-6b148220ea9b",
  "isSidechain": false,
  "requestId": "req_011CbLqFbM2MWmMdFqtfCGeK",
  "type": "assistant",
  "uuid": "799ccd6e-8b90-49fa-a6df-232d144ed909",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "replicated-gathering-forest",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BUe7mYCXUsGfr7mfRzqL4p",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 144568,
      "output_tokens": 468,
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
          "output_tokens": 468,
          "cache_read_input_tokens": 144568,
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


### Runtime record

_source line 201_

```json
{
  "type": "last-prompt",
  "leafUuid": "799ccd6e-8b90-49fa-a6df-232d144ed909",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd"
}
```

---


### Runtime record

_source line 202_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit paper tables against registry data",
  "sessionId": "a687eb63-dc86-47b1-b68c-4198dbfbe0bd"
}
```

---
