# Research conversation: <project_context> # 项目: faith-evidence-ie ## 运行环境 - 服务器名: rtx5090-4x - SSH 账户: root（调用 ssh_execute / submit_training_job — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-faith-evidence-ie-rtx5090-4x-ssh-root-ssh-execute-submit-train-copy-424.md) · [Structured JSON](../../../sessions/64/64133b971c72955d53bd.json)

## Round 1

### Runtime record

_source line 321 · 2026-05-26T10:45:57.583Z_

```json
{
  "parentUuid": "efedae1c-2b6d-4949-ac04-b8e76826ee5e",
  "isSidechain": false,
  "attachment": {
    "type": "queued_command",
    "prompt": "&lt;task-notification>\n&lt;task-id>a32692ef3570c895e&lt;/task-id>\n&lt;tool-use-id>toolu_01LA2M8BxwEz1zuuEeibZRyH&lt;/tool-use-id>\n&lt;output-file>/tmp/claude-1000/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/7ad27970-2427-4427-8982-3e07c0bbdf41/tasks/a32692ef3570c895e.output&lt;/output-file>\n&lt;status>completed&lt;/status>\n&lt;summary>Agent \"Verify refs batch 5 (42-52)\" completed&lt;/summary>\n&lt;result>Now I have all the data. The bib file author list for `gulcehre2023rest` includes \"Dyer, Chris\" and \"Grangier, David\" but the actual paper has \"Doucet, Arnaud\" and \"de Freitas, Nando\". This is a significant author list error. Let me now compile the full structured report.\n\n---\n\n## Reference Audit Report\n\n### 42. he2023debertav3\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2111.09543 |\n| Title | ✓ | \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\" -- matches |\n| Authors | ✓ | He, Pengcheng; Gao, Jianfeng; Chen, Weizhu -- matches |\n| Year | ✓ | 2023 (ICLR 2023) -- matches |\n| Venue | ✓ | ICLR 2023 -- matches (bib says \"International Conference on Learning Representations\") |\n| arXiv ID | ✓ | 2111.09543 -- matches |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 43. dettmers2023qlora\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2305.14314 |\n| Title | ✓ | \"QLoRA: Efficient Finetuning of Quantized LLMs\" -- matches |\n| Authors | ✓ | Dettmers, Tim; Pagnoni, Artidoro; Holtzman, Ari; Zettlemoyer, Luke -- matches |\n| Year | ✓ | 2023 -- matches |\n| Venue | ✓ | NeurIPS 2023 -- confirmed in NeurIPS proceedings (bib says \"Advances in Neural Information Processing Systems\") |\n| arXiv ID | ✓ | 2305.14314 -- matches |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 44. hoffmann2022chinchilla\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2203.15556 |\n| Title | ✓ | \"Training Compute-Optimal Large Language Models\" -- matches |\n| Authors | ✓ | Hoffmann, Jordan; Borgeaud, Sebastian; Mensch, Arthur; and many others -- bib lists 22 authors which is consistent with the actual paper |\n| Year | ✓ | 2022 -- matches |\n| Venue | ✓ | NeurIPS 2022 -- confirmed in NeurIPS proceedings (bib says \"Advances in Neural Information Processing Systems\") |\n| arXiv ID | ✓ | 2203.15556 -- matches |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 45. yuan2023rft\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2308.01825 |\n| Title | ✓ | \"Scaling Relationship on Learning Mathematical Reasoning with Large Language Models\" -- matches |\n| Authors | ✓ | Yuan, Zheng; Yuan, Hongyi; Li, Chengpeng; Dong, Guanting; Lu, Keming; Tan, Chuanqi; Zhou, Chang; Zhou, Jingren -- matches |\n| Year | ✓ | 2023 -- matches arXiv submission date |\n| Venue | ✓ | Listed as `@article` with \"arXiv preprint arXiv:2308.01825\" -- this is appropriate. The paper was submitted to ICLR 2024 via OpenReview but the acceptance status is unclear; treating it as an arXiv preprint is safe |\n| arXiv ID | ✓ | 2308.01825 -- matches |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 46. tamo2026evidencerl\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2603.19532 (posted March 2026) |\n| Title | ✓ | \"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\" -- matches |\n| Authors | ✓ | Tamo, J. Ben; Lu, Yuxing; Marteau, Benoit L.; Nnamdi, Micky C.; Wang, May D. -- matches |\n| Year | ✓ | 2026 -- matches (posted March 2026) |\n| Venue | ✓ | Listed as `@article` with arXiv preprint -- appropriate for a preprint |\n| arXiv ID | ✓ | 2603.19532 -- matches |\n\n**Verdict: ALL CORRECT -- paper is real (not fabricated)**\n\n---\n\n### 47. liu2026rift\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2601.09253 (posted January 2026) |\n| Title | ✓ | \"RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning\" -- matches |\n| Authors | ✓ | Liu, Zehua; Liu, Shuqi; Zhong, Tao; Yuan, Mingxuan -- matches (Huawei Noah's Ark Lab) |\n| Year | ✓ | 2026 -- matches (posted January 14, 2026) |\n| Venue | ✓ | Listed as `@article` with arXiv preprint -- appropriate |\n| arXiv ID | ✓ | 2601.09253 -- matches |\n\n**Verdict: ALL CORRECT -- paper is real (not fabricated)**\n\n---\n\n### 48. deng2026trajfusion\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2602.04391 (posted February 2026) |\n| Title | ✓ | \"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning\" -- matches |\n| Authors | ✓ | Deng, Jie; Tong, Hanshuang; Li, Jun; Liang, Shining; Wu, Ning; Li, Hongzhi; Xie, Yutao -- matches |\n| Year | ✓ | 2026 -- matches (posted February 2026) |\n| Venue | ✓ | Listed as `@article` with arXiv preprint -- appropriate |\n| arXiv ID | ✓ | 2602.04391 -- matches |\n\n**Verdict: ALL CORRECT -- paper is real (not fabricated)**\n\n---\n\n### 49. tian2026mugrpo\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2605.17570 (posted May 2026) |\n| Title | ✓ | \"How Off-Policy Can GRPO Be? μ-GRPO for Efficient LLM Reinforcement Learning\" -- matches (bib uses LaTeX `$\\mu$-GRPO` which renders correctly) |\n| Authors | ✓ | Tian, Minghao; Xie, Yunfei; Wei, Chen -- matches (3 authors, Rice University) |\n| Year | ✓ | 2026 -- matches (posted May 17, 2026) |\n| Venue | ✓ | Listed as `@article` with arXiv preprint -- appropriate |\n| arXiv ID | ✓ | 2605.17570 -- matches |\n\n**Verdict: ALL CORRECT -- paper is real (not fabricated)**\n\n---\n\n### 50. ji2026treegrpo\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2509.21240 |\n| Title | ✓ | \"Tree Search for LLM Agent Reinforcement Learning\" -- matches |\n| Authors | ✓ | Ji, Yuxiang; Ma, Ziyu; Wang, Yong; Chen, Guanhua; Chu, Xiangxiang; Wu, Liaoni -- matches |\n| Year | ✓ | 2026 (ICLR 2026) -- matches (paper accepted at ICLR 2026, confirmed by GitHub repo tag \"[ICLR 2026]\") |\n| Venue | ✓ | ICLR 2026 -- confirmed (bib says \"International Conference on Learning Representations\") |\n| arXiv ID | ✓ | 2509.21240 -- matches |\n\n**Verdict: ALL CORRECT -- paper is real (not fabricated)**\n\n---\n\n### 51. deepseek2025r1\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2501.12948 |\n| Title | ✓ | \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\" -- matches |\n| Authors | ✓ | DeepSeek-AI (team paper) -- matches |\n| Year | ✓ | 2025 -- matches (posted January 22, 2025) |\n| Venue | ✓ | Listed as `@article` with arXiv preprint -- appropriate (also later published in Nature, but arXiv preprint listing is fine) |\n| arXiv ID | ✓ | 2501.12948 -- matches |\n\n**Verdict: ALL CORRECT**\n\n---\n\n### 52. gulcehre2023rest\n\n| Field | Status | Notes |\n|-------|--------|-------|\n| Exists | ✓ | Paper exists on arXiv at 2308.08998 |\n| Title | ✓ | \"Reinforced Self-Training (ReST) for Language Modeling\" -- matches |\n| Authors | **✗** | **INCORRECT.** The bib lists: \"Gulcehre, Caglar and Paine, Tom Le and Srinivasan, Srivatsan and Konyushkova, Ksenia and Weerts, Lotte and Sharma, Abhishek and Siddhant, Aditya and Ahern, Alex and Wang, Miaosen and Gu, Chenjie and Macherey, Wolfgang and **Dyer, Chris** and **Grangier, David** and Firat, Orhan\". The actual paper lists: \"...Macherey, Wolfgang and **Doucet, Arnaud** and Firat, Orhan and **de Freitas, Nando**\". Two authors are wrong: **Dyer, Chris** should be **Doucet, Arnaud**, and **Grangier, David** should be **de Freitas, Nando**. |\n| Year | ✓ | 2023 -- matches |\n| Venue | **✗** | **INVALID.** Entry type is `@inproceedings` but `booktitle` is set to \"arXiv preprint arXiv:2308.08998\". This is not a valid venue for `@inproceedings`. Should be changed to `@article` with `journal = {arXiv preprint arXiv:2308.08998}`. The paper appears to remain an arXiv preprint (no conference publication found). |\n| arXiv ID | ✓ | 2308.08998 -- matches |\n\n**Verdict: TWO ERRORS FOUND**\n1. **Author list error**: \"Dyer, Chris\" and \"Grangier, David\" are not authors. The correct authors in those positions are \"Doucet, Arnaud\" and \"de Freitas, Nando\".\n2. **Entry type/venue error**: Should be `@article` not `@inproceedings`, since the booktitle is just the arXiv preprint identifier, not a conference.\n\n---\n\n## Summary\n\n| # | Key | Status | Issues |\n|---|-----|--------|--------|\n| 42 | he2023debertav3 | ✓ PASS | None |\n| 43 | dettmers2023qlora | ✓ PASS | None |\n| 44 | hoffmann2022chinchilla | ✓ PASS | None |\n| 45 | yuan2023rft | ✓ PASS | None |\n| 46 | tamo2026evidencerl | ✓ PASS | Real 2026 paper, verified |\n| 47 | liu2026rift | ✓ PASS | Real 2026 paper, verified |\n| 48 | deng2026trajfusion | ✓ PASS | Real 2026 paper, verified |\n| 49 | tian2026mugrpo | ✓ PASS | Real 2026 paper, verified |\n| 50 | ji2026treegrpo | ✓ PASS | Real 2026 paper, verified |\n| 51 | deepseek2025r1 | ✓ PASS | None |\n| 52 | gulcehre2023rest | **✗ FAIL** | (1) Wrong authors: \"Dyer, Chris\" and \"Grangier, David\" should be \"Doucet, Arnaud\" and \"de Freitas, Nando\"; (2) Entry type should be `@article` not `@inproceedings` |\n\n**Total: 10 pass, 1 fail.** The only reference with errors is `gulcehre2023rest` (#52), which has two incorrect author names and an improper BibTeX entry type. All five 2026 references (items 46-50) were verified as real, existing papers -- none are fabricated.\n\nThe bib file location is `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper/references.bib` (lines 412-418 for the problematic entry).&lt;/result>\n&lt;usage>&lt;total_tokens>54445&lt;/total_tokens>&lt;tool_uses>32&lt;/tool_uses>&lt;duration_ms>437375&lt;/duration_ms>&lt;/usage>\n&lt;/task-notification>",
    "commandMode": "task-notification"
  },
  "type": "attachment",
  "uuid": "15a7caf4-20a0-416b-a7de-60ea1b689885",
  "timestamp": "2026-05-26T10:45:57.583Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41",
  "version": "2.1.126",
  "gitBranch": "main"
}
```

---


### Runtime record

_source line 322_

```json
{
  "type": "last-prompt",
  "leafUuid": "15a7caf4-20a0-416b-a7de-60ea1b689885",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41"
}
```

---


### Runtime record

_source line 323_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit all 52 references in faith-evidence-ie paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41"
}
```

---


### Assistant

_source line 324 · 2026-05-26T10:46:27.725Z_

<details><summary>Logged reasoning block</summary>

```text
Batch 5 has now completed as well. Let me compile all findings:

**Batch 5 results:**
- he2023debertav3: ✓ OK
- dettmers2023qlora: ✓ OK
- hoffmann2022chinchilla: ✓ OK
- yuan2023rft: ✓ OK
- tamo2026evidencerl: ✓ OK (real paper)


- liu2026rift: ✓ OK (real paper)
- deng2026trajfusion: ✓ OK (real paper)
- tian2026mugrpo: ✓ OK (real paper)
- ji2026treegrpo: ✓ OK (real paper)
- deepseek2025r1: ✓ OK

I found an issue with gulcehre2023rest — the author names are incorrect, listing Dyer and Grangier when it should be Doucet and de Freitas, and there's another problem I'm still examining.

Now that I've gone through all 52 references, I'm compiling the full audit report. Looking at the cited references, I've identified several issues: ma2023dreeam has the wrong venue designation, li2026qurl needs its ICLR 2026 acceptance reflected, xu2024lmrc and wang2025rear have incorrect cite keys based on actual first authors, and wang2025relprior appears to have a fabricated title prefix that doesn't match the real paper.

I'm also finding more serious problems with tang2025rsftppo—the venue is completely fabricated and the cite key is wrong—and gulcehre2023rest has both incorrect author names and an invalid @inproceedings format using "arXiv preprint" as a booktitle. Continuing through the remaining issues with tan2022redocred and others.

I'm also noticing some uncited references with their own problems: ito2025mogrpo, wang2025rullm, and zhang2025glidre all have incorrect cite keys where the first author doesn't match. Now I need to look more carefully at how citations are actually being used in the text—for instance, the xu2024lmrc citation in the introduction claims the paper frames relation extraction as multi-choice reading comprehension, but the actual title suggests it's about a relation classifier instead, so I should verify whether that characterization is accurate. Since the bibliography is configured to only include cited entries in the final PDF output, those 17 uncited entries in the bib file won't actually appear. Now I'll compile the complete audit report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15a7caf4-20a0-416b-a7de-60ea1b689885",
  "isSidechain": false,
  "requestId": "req_011CbR3bv6N71DxMnmt8jxzZ",
  "type": "assistant",
  "uuid": "b98f29be-d38d-4e41-b1f2-d298cb10a5e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41",
  "version": "2.1.126",
  "gitBranch": "main",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fq9Mz4y9CUp5cioUUKdB3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 596,
      "cache_creation_input_tokens": 6201,
      "cache_read_input_tokens": 106268,
      "output_tokens": 1368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 596,
          "output_tokens": 1368,
          "cache_read_input_tokens": 106268,
          "cache_creation_input_tokens": 6201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6201
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

_source line 325 · 2026-05-26T10:46:28.617Z_

All 5 batches complete. Now compiling the full audit report.

**Critical findings from batch 5:**
- **gulcehre2023rest**: 2 wrong authors (Dyer → Doucet, Grangier → de Freitas) + invalid @inproceedings for arXiv
- All 2026 references verified as real papers

Now writing the complete audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b98f29be-d38d-4e41-b1f2-d298cb10a5e0",
  "isSidechain": false,
  "requestId": "req_011CbR3bv6N71DxMnmt8jxzZ",
  "type": "assistant",
  "uuid": "71563965-3568-4013-9177-8ad7f1902421",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41",
  "version": "2.1.126",
  "gitBranch": "main",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fq9Mz4y9CUp5cioUUKdB3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 596,
      "cache_creation_input_tokens": 6201,
      "cache_read_input_tokens": 106268,
      "output_tokens": 1368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 596,
          "output_tokens": 1368,
          "cache_read_input_tokens": 106268,
          "cache_creation_input_tokens": 6201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6201
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

_source line 326 · 2026-05-26T10:46:29.370Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ErKh3cb2WktBDPzhnYpcLE`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71563965-3568-4013-9177-8ad7f1902421",
  "isSidechain": false,
  "requestId": "req_011CbR3bv6N71DxMnmt8jxzZ",
  "type": "assistant",
  "uuid": "a86d0c21-1c0d-41cc-b635-937aaae83639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41",
  "version": "2.1.126",
  "gitBranch": "main",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016fq9Mz4y9CUp5cioUUKdB3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 596,
      "cache_creation_input_tokens": 6201,
      "cache_read_input_tokens": 106268,
      "output_tokens": 1368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6201,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 596,
          "output_tokens": 1368,
          "cache_read_input_tokens": 106268,
          "cache_creation_input_tokens": 6201,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6201
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

_source line 327 · 2026-05-26T10:46:29.425Z_

<details><summary>↩ Tool result · `toolu_01ErKh3cb2WktBDPzhnYpcLE`</summary>

```text
14b_rsft_status.md
1_7b_repetition_fair_eval.md
_project
anon_cleanup_report.md
anon_repo_diff.md
baseline_verification.md
ced_eval_commands.md
ced_stabilizer_literature_survey.md
comprehensive_results.md
cuda3_diagnostic.md
d024_literature_survey.md
d076_eval_audit.py
d076_final_audit.py
d076_seed_status.md
d102_next_batch
d112
d112_pipeline_plan.md
d112_rsft_no_evidence_eval_r3_analysis.md
d112_rsft_no_evidence_eval_r3_prep.md
d112_rsft_s44_train_prep.md
d140_4b_sft_s42_no_evi_2048_diagnosis.md
d140_progress_check.md
dev_test_gap_paragraph.md
diag_mvp2_grpo_flatnli_r3.md
diag_plan019_1_7b_rsft_s43.md
diag_redocred_rsft_r2.md
diagnose_8b_timeout.md
diagnose_eval_llama_rsft_s42_with_evidence_2048.md
diagnose_eval_llama_sft_s42_no_evidence_std.md
diagnose_plan_001.md
diversity_probe.py
diversity_probe_results.md
dpo_rebuilt_3ep_eval
dream_reports
dreeam_evif1_alignment_report.md
edcr_analysis.md
edcr_analysis_r2b.md
edcr_diagnostic_table.md
efficiency_comparison.md
eval_plan_014_no_evidence_r2_analysis.md
eval_progress_20260516.md
eval_progress_check_0515.md
eval_rsft_ced_s43
eval_rsft_ced_s45
eval_script_audit.md
eval_status_check.md
evidence_cost_literature_scan.md
evidence_tax_annotation_notes.md
experiment_summary_table.md
fig_edcr_relations.pdf
fig_edcr_relations.png
fig_evidence_tax.pdf
fig_evidence_tax.png
fig_grpo_dynamics.pdf
fig_grpo_dynamics.png
fig_spectrum.pdf
fig_spectrum.png
final_audit_v2_w1_text.md
final_audit_v2_w2_tables.md
final_audit_v2_w3_figures_appendix.md
final_audit_w1_abstract.md
final_audit_w2_tables.md
final_audit_w3_figures.md
freige
gap_analysis_w3.md
grpo_forgetting_dynamics.pdf
grpo_forgetting_dynamics.png
kl_analysis_report.md
literature_quantization_rl.md
literature_survey_evidence_overhead.md
manifest.yaml
metrics_summary.csv
metrics_summary_table.md
mvp2_eval_rsft_r2b_maxtok1536_r2
negative_review.md
next_batch_plan.md
no_evi_test_commands.md
paired_ttest_analysis.py
paper
paper_evidence_table.md
paper_main_tables_draft.md
paper_metrics_table.md
paper_status_audit.md
paper_table1_data.md
plan017_14b_rsft_s43_eval
plan017_14b_rsft_s43_no_evi_eval
plan019_8b_sft_s43_eval_analysis.md
plan_001_flat_nli_seed45
plan_003
plan_003_edcr_cross_method_table.md
plan_003_edcr_diagnostic
plan_003_edcr_diagnostic.md
plan_006_qwen3_1_7b_no_evidence_eval_v3_results.json
plan_007_redocred_rsft_eval_r2
plan_009
plan_009_dynamics_data.json
plan_009_dynamics_figure
plan_009_forgetting_data.csv
plan_009_forgetting_data_v5.csv
plan_009_forgetting_figure
plan_009_grpo_forgetting
plan_012_dpo_ced
plan_012_dpo_ced_1ep_analysis.md
process_check_report.md
reeval_ced_s42
reeval_ced_s44
reeval_commands.md
reeval_flat_nli_s42
reeval_flat_nli_s43_r2
reeval_sft_baseline_d076
ref_audit_worker2.md
related_work_gap_analysis.md
related_work_survey
review_issues.yaml
review_reports
review_round_2
review_round_3
review_round_4
rsft_gen_progress_check.md
rsft_pipeline_commands.md
server_audit_bjb2.md
server_audit_rtx5090.md
server_state_20260522.md
status_check_loop4.md
test_eval_14b_rsft_s43
test_eval_14b_rsft_s43_no_evi
test_eval_14b_rsft_s43_pair
test_eval_4b_rsft_s44_no_evi_r2
test_eval_8b_rsft_s42
test_eval_commands.md
test_eval_llama_rsft_s42_no_evi_v2
test_eval_llama_rsft_s42_with_evi_v3
test_table_compilation.md
test_table_draft.md
topk_ablation_lit_review.md
training_health_check.md
training_trajectory_loop4.md
trl_grpo_stability_research.md
worker_check_status.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a86d0c21-1c0d-41cc-b635-937aaae83639",
  "isSidechain": false,
  "promptId": "8765e186-da5a-48f9-b659-e510c65c176b",
  "type": "user",
  "uuid": "7d29da4e-d372-4db6-9c0e-09be33cecf66",
  "toolUseResult": {
    "stdout": "14b_rsft_status.md\n1_7b_repetition_fair_eval.md\n_project\nanon_cleanup_report.md\nanon_repo_diff.md\nbaseline_verification.md\nced_eval_commands.md\nced_stabilizer_literature_survey.md\ncomprehensive_results.md\ncuda3_diagnostic.md\nd024_literature_survey.md\nd076_eval_audit.py\nd076_final_audit.py\nd076_seed_status.md\nd102_next_batch\nd112\nd112_pipeline_plan.md\nd112_rsft_no_evidence_eval_r3_analysis.md\nd112_rsft_no_evidence_eval_r3_prep.md\nd112_rsft_s44_train_prep.md\nd140_4b_sft_s42_no_evi_2048_diagnosis.md\nd140_progress_check.md\ndev_test_gap_paragraph.md\ndiag_mvp2_grpo_flatnli_r3.md\ndiag_plan019_1_7b_rsft_s43.md\ndiag_redocred_rsft_r2.md\ndiagnose_8b_timeout.md\ndiagnose_eval_llama_rsft_s42_with_evidence_2048.md\ndiagnose_eval_llama_sft_s42_no_evidence_std.md\ndiagnose_plan_001.md\ndiversity_probe.py\ndiversity_probe_results.md\ndpo_rebuilt_3ep_eval\ndream_reports\ndreeam_evif1_alignment_report.md\nedcr_analysis.md\nedcr_analysis_r2b.md\nedcr_diagnostic_table.md\nefficiency_comparison.md\neval_plan_014_no_evidence_r2_analysis.md\neval_progress_20260516.md\neval_progress_check_0515.md\neval_rsft_ced_s43\neval_rsft_ced_s45\neval_script_audit.md\neval_status_check.md\nevidence_cost_literature_scan.md\nevidence_tax_annotation_notes.md\nexperiment_summary_table.md\nfig_edcr_relations.pdf\nfig_edcr_relations.png\nfig_evidence_tax.pdf\nfig_evidence_tax.png\nfig_grpo_dynamics.pdf\nfig_grpo_dynamics.png\nfig_spectrum.pdf\nfig_spectrum.png\nfinal_audit_v2_w1_text.md\nfinal_audit_v2_w2_tables.md\nfinal_audit_v2_w3_figures_appendix.md\nfinal_audit_w1_abstract.md\nfinal_audit_w2_tables.md\nfinal_audit_w3_figures.md\nfreige\ngap_analysis_w3.md\ngrpo_forgetting_dynamics.pdf\ngrpo_forgetting_dynamics.png\nkl_analysis_report.md\nliterature_quantization_rl.md\nliterature_survey_evidence_overhead.md\nmanifest.yaml\nmetrics_summary.csv\nmetrics_summary_table.md\nmvp2_eval_rsft_r2b_maxtok1536_r2\nnegative_review.md\nnext_batch_plan.md\nno_evi_test_commands.md\npaired_ttest_analysis.py\npaper\npaper_evidence_table.md\npaper_main_tables_draft.md\npaper_metrics_table.md\npaper_status_audit.md\npaper_table1_data.md\nplan017_14b_rsft_s43_eval\nplan017_14b_rsft_s43_no_evi_eval\nplan019_8b_sft_s43_eval_analysis.md\nplan_001_flat_nli_seed45\nplan_003\nplan_003_edcr_cross_method_table.md\nplan_003_edcr_diagnostic\nplan_003_edcr_diagnostic.md\nplan_006_qwen3_1_7b_no_evidence_eval_v3_results.json\nplan_007_redocred_rsft_eval_r2\nplan_009\nplan_009_dynamics_data.json\nplan_009_dynamics_figure\nplan_009_forgetting_data.csv\nplan_009_forgetting_data_v5.csv\nplan_009_forgetting_figure\nplan_009_grpo_forgetting\nplan_012_dpo_ced\nplan_012_dpo_ced_1ep_analysis.md\nprocess_check_report.md\nreeval_ced_s42\nreeval_ced_s44\nreeval_commands.md\nreeval_flat_nli_s42\nreeval_flat_nli_s43_r2\nreeval_sft_baseline_d076\nref_audit_worker2.md\nrelated_work_gap_analysis.md\nrelated_work_survey\nreview_issues.yaml\nreview_reports\nreview_round_2\nreview_round_3\nreview_round_4\nrsft_gen_progress_check.md\nrsft_pipeline_commands.md\nserver_audit_bjb2.md\nserver_audit_rtx5090.md\nserver_state_20260522.md\nstatus_check_loop4.md\ntest_eval_14b_rsft_s43\ntest_eval_14b_rsft_s43_no_evi\ntest_eval_14b_rsft_s43_pair\ntest_eval_4b_rsft_s44_no_evi_r2\ntest_eval_8b_rsft_s42\ntest_eval_commands.md\ntest_eval_llama_rsft_s42_no_evi_v2\ntest_eval_llama_rsft_s42_with_evi_v3\ntest_table_compilation.md\ntest_table_draft.md\ntopk_ablation_lit_review.md\ntraining_health_check.md\ntraining_trajectory_loop4.md\ntrl_grpo_stability_research.md\nworker_check_status.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a86d0c21-1c0d-41cc-b635-937aaae83639",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41",
  "version": "2.1.126",
  "gitBranch": "main"
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-26T10:49:36.918Z_

<details open><summary>🔧 Tool call — Write · `toolu_01NZZ4qzWB9GvPqMjiiSFwdk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/ref_audit_worker3.md",
  "content": "# 引用核对清单 — Worker 3\n\n总计: 52 条引用 (35 条在正文中被引用, 17 条仅存在于 bib 文件), 11 条有问题\n\n## 问题汇总\n\n| 严重度 | 数量 | 说明 |\n|--------|------|------|\n| 高危 (内容错误) | 4 | gulcehre2023rest 作者错误, wang2025relprior 标题虚构, tang2025rsftppo 会议名虚构, ma2023dreeam venue 错误 |\n| 中等 (格式/key 问题) | 5 | xu2024lmrc/wang2025rear/wang2025rullm cite key 与首作者不一致, gulcehre2023rest entry type 错误, li2026qurl 缺少 venue 更新 |\n| 低 (仅限未引用条目) | 3 | ito2025mogrpo/zhang2025glidre cite key 错误 (未被引用), tan2022redocred 标题标点 |\n\n## 逐条结果\n\n---\n\n### 1. [autore2024] — ✓\n- 真实性: ✓\n- 作者: ✓ Xue, Lilong; Zhang, Dan; Dong, Yuxiao; Tang, Jie\n- 年份: ✓ 2024\n- 标题: ✓ \"AutoRE: Document-Level Relation Extraction with Large Language Models\"\n- Venue: ✓ ACL 2024 System Demonstrations\n- arXiv ID: ✓ 2403.14888\n- 正文用法: ✓ intro: \"fine-tune LLMs with structured decomposition\"; related work: \"uses QLoRA with relation-head-facts decomposition\"\n- 备注: 无问题\n\n### 2. [xu2025docksrag] — ✓\n- 真实性: ✓\n- 作者: ✓ Xu, Xiaolong et al.\n- 年份: ✓ 2025\n- 标题: ✓ \"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\"\n- Venue: ✓ ICML 2025 (PMLR 267)\n- arXiv ID: N/A\n- 正文用法: ✓ intro: \"combine retrieval-augmented generation with structured knowledge\"\n- 备注: 无问题\n\n### 3. [dai2025r1re] — ✓\n- 真实性: ✓\n- 作者: ✓ Dai, Runpeng; Zheng, Tong; Yang, Run; Yu, Kaixian; Zhu, Hongtu\n- 年份: ✓ 2025\n- 标题: ✓ \"R1-RE: Cross-Domain Relation Extraction with RLVR\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2507.04642\n- 正文用法: ✓ related work: \"applications to structured IE include R1-RE\"\n- 备注: 无问题\n\n### 4. [gao2023scaling] — ✓\n- 真实性: ✓\n- 作者: ✓ Gao, Leo; Schulman, John; Hilton, Jacob\n- 年份: ✓ 2023\n- 标题: ✓ \"Scaling Laws for Reward Model Overoptimization\"\n- Venue: ✓ ICML 2023\n- arXiv ID: ✓ 2210.10760\n- 正文用法: ✓ related work: \"capacity-dependent scaling dynamics\"; experiments: reward optimization dynamics\n- 备注: 无问题\n\n### 5. [hu2022lora] — ✓\n- 真实性: ✓\n- 作者: ✓ Hu, Edward J. et al.\n- 年份: ✓ 2022\n- 标题: ✓ \"LoRA: Low-Rank Adaptation of Large Language Models\"\n- Venue: ✓ ICLR 2022\n- arXiv ID: ✓ 2106.09685\n- 正文用法: ✓ method: \"Low-Rank Adaptation (LoRA)\"\n- 备注: 无问题\n\n### 6. [li2026qurl] — ✗\n- 真实性: ✓\n- 作者: ✓ Li, Yuhang; Elangovan, Reena; Dong, Xin; Panda, Priyadarshini; Khailany, Brucek\n- 年份: ✓ 2026\n- 标题: ✓ \"QuRL: Efficient Reinforcement Learning with Quantized Rollout\"\n- Venue: ✗ bib 列为 arXiv preprint，实际已被 **ICLR 2026** 接收\n- arXiv ID: ✓ 2602.13953\n- 正文用法: ✓ experiments: \"resembling the quantized-actor divergence of \\citet{li2026qurl}\"\n- 备注: 应更新 venue 为 ICLR 2026\n\n### 7. [laban2022summac] — ✓\n- 真实性: ✓\n- 作者: ✓ Laban, Philippe; Schnabel, Tobias; Bennett, Paul N.; Hearst, Marti A.\n- 年份: ✓ 2022\n- 标题: ✓ \"SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization\"\n- Venue: ✓ TACL, vol 10, pp 163-177\n- arXiv ID: N/A\n- 正文用法: ✓ related work: NLI-based faithfulness evaluation\n- 备注: 无问题\n\n### 8. [li2025srvf] — ✓\n- 真实性: ✓\n- 作者: ✓ Li, Yongqi; Miao, Xin; Zhou, Shen; Xu, Mayi; Ren, Yuyang; Qian, Tieyun\n- 年份: ✓ 2025\n- 标题: ✓ \"Enhancing Relation Extraction via Supervised Rationale Verification and Feedback\"\n- Venue: ✓ AAAI 2025\n- arXiv ID: ✓ 2412.07289\n- 正文用法: ✓ related work: \"reward-based evidence grounding\"\n- 备注: 无问题\n\n### 9. [jin2025rl_panacea] — ✓\n- 真实性: ✓\n- 作者: ✓ Jin, Hangzhan; Lv, Sicheng; Wu, Sifan; Hamdaqa, Mohammad\n- 年份: ✓ 2025\n- 标题: ✓ \"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2508.16546\n- 正文用法: ✓ related work: \"catastrophic forgetting in RL alignment\"\n- 备注: 无问题\n\n### 10. [ma2023dreeam] — ✗\n- 真实性: ✓\n- 作者: ✓ Ma, Youmi; Wang, An; Okazaki, Naoaki\n- 年份: ✓ 2023\n- 标题: ✓ \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\"\n- Venue: ✗ bib 写 \"Findings of the Association for Computational Linguistics: EACL 2023\"，实际是 **EACL 2023 主会议** (ACL Anthology: 2023.eacl-main.145)\n- arXiv ID: ✓ 2302.08675\n- 正文用法: ✓\n- 备注: **venue 错误**。应改为 \"Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics\"\n\n### 11. [moskovitz2024constrained] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Moskovitz, Ted et al.\n- 年份: ✓ 2024\n- 标题: ✓ \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n- Venue: ✓ ICLR 2024\n- arXiv ID: N/A (OpenReview URL 正确)\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite，不会出现在论文中\n\n### 12. [rafailov2023direct] — ✓\n- 真实性: ✓\n- 作者: ✓ Rafailov, Rafael; Sharma, Archit; Mitchell, Eric; Ermon, Stefano; Manning, Christopher D.; Finn, Chelsea\n- 年份: ✓ 2023\n- 标题: ✓ \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n- Venue: ✓ NeurIPS 2023\n- arXiv ID: ✓ 2305.18290\n- 正文用法: ✓ intro/method: DPO paradigm\n- 备注: 无问题\n\n### 13. [shao2024deepseekmath] — ✓\n- 真实性: ✓\n- 作者: ✓ Shao, Zhihong et al. (bib 中作者名略有缩写但可接受)\n- 年份: ✓ 2024\n- 标题: ✓ \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2402.03300\n- 正文用法: ✓ intro/method: GRPO\n- 备注: 无问题\n\n### 14. [tan2022redocred] — ✓ (微小问题)\n- 真实性: ✓\n- 作者: ✓ Tan, Qingyu; Xu, Lu; Bing, Lidong; Ng, Hwee Tou; Aljunied, Sharifah Mahani\n- 年份: ✓ 2022\n- 标题: ✓ (微小: 官方标题用 dash 不是 colon，但功能上可接受)\n- Venue: ✓ EMNLP 2022\n- arXiv ID: N/A\n- 正文用法: ✓\n- 备注: 官方标题用 dash \"Revisiting DocRED - Addressing...\" 而非 colon \"Revisiting DocRED: Addressing...\"，低优先级\n\n### 15. [xiao2022sais] — ✓\n- 真实性: ✓\n- 作者: ✓ Xiao, Yuxin; Zhang, Zecheng; Mao, Yuning; Yang, Carl; Han, Jiawei\n- 年份: ✓ 2022\n- 标题: ✓ \"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\"\n- Venue: ✓ NAACL 2022\n- arXiv ID: N/A\n- 正文用法: ✓\n- 备注: 无问题\n\n### 16. [xie2022eider] — ✓\n- 真实性: ✓\n- 作者: ✓ Xie, Yiqing; Shen, Jiaming; Li, Sha; Mao, Yuning; Han, Jiawei\n- 年份: ✓ 2022\n- 标题: ✓ \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\"\n- Venue: ✓ Findings ACL 2022\n- arXiv ID: ✓ 2106.08657\n- 正文用法: ✓\n- 备注: 无问题\n\n### 17. [xu2024lmrc] — ✗\n- 真实性: ✓\n- 作者: ✗ bib 中作者正确列为 Li, Xingzuo et al.，但 **cite key 写 \"xu2024\" 与首作者 Li 不一致**\n- 年份: ✓ 2024\n- 标题: ✓ (bib 加了 \"LMRC:\" 前缀，arXiv 原标题无此前缀，但作为缩写惯例可接受)\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2408.13889\n- 正文用法: ✗ 正文 \"\\citet{xu2024lmrc}\" 渲染为 \"Xu et al. (2024)\"，但首作者是 **Li**，读者看到的引用与实际作者不符\n- 备注: **cite key 命名错误导致正文显示错误作者**。应改 key 为 li2024lmrc，或修正正文中所有引用\n\n### 18. [yao2019docred] — ✓\n- 真实性: ✓\n- 作者: ✓ Yao, Yuan et al.\n- 年份: ✓ 2019\n- 标题: ✓ \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\"\n- Venue: ✓ ACL 2019\n- arXiv ID: N/A\n- 正文用法: ✓\n- 备注: 无问题\n\n### 19. [zelikman2022star] — ✓\n- 真实性: ✓\n- 作者: ✓ Zelikman, Eric; Wu, Yuhuai; Mu, Jesse; Goodman, Noah D.\n- 年份: ✓ 2022\n- 标题: ✓ \"STaR: Bootstrapping Reasoning With Reasoning\"\n- Venue: ✓ NeurIPS 2022\n- arXiv ID: ✓ 2203.14465\n- 正文用法: ✓ intro/method: STaR as RSFT foundation\n- 备注: 无问题\n\n### 20. [dong2023raft] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Dong, Hanze et al.\n- 年份: ✓ 2023\n- 标题: ✓ \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\"\n- Venue: ✓ TMLR\n- arXiv ID: ✓ 2304.06767\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 21. [ito2025mogrpo] — ✗ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Ichihara, Yuki; Jinnai, Yuu; Morimura, Tetsuro; Sakamoto, Mitsuki; Mitsuhashi, Ryota; Uchibe, Eiji\n- 年份: ✓ 2025\n- 标题: ✓ \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2509.22047\n- 正文用法: N/A (未在正文中被引用)\n- 备注: cite key \"ito2025\" 但首作者是 Ichihara。未被引用所以不影响论文。\n\n### 22. [li2025drift] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Li, Jiazheng; Yan, Hanqi; He, Yulan\n- 年份: ✓ 2025\n- 标题: ✓ \"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\"\n- Venue: ✓ ACL 2025\n- arXiv ID: N/A\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 23. [liu2026gdpo] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Liu, Shih-Yang et al.\n- 年份: ✓ 2026\n- 标题: ✓ \"GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward RL Optimization\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2601.05242\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 24. [liu2025drgrpo] — ✓\n- 真实性: ✓\n- 作者: ✓ Liu, Zichen; Chen, Changyu; Li, Wenjun; Qi, Penghui; Pang, Tianyu; Du, Chao; Lee, Wee Sun; Lin, Min\n- 年份: ✓ 2025\n- 标题: ✓ \"Understanding R1-Zero-Like Training: A Critical Perspective\"\n- Venue: ✓ Conference on Language Modeling (COLM 2025)\n- arXiv ID: ✓ 2503.20783\n- 正文用法: ✓ related work: \"length bias\" (paper proposes Dr. GRPO to address length bias)\n- 备注: cite key \"drgrpo\" 基于论文提出的方法名，可接受\n\n### 25. [yu2025dapo] — ✓\n- 真实性: ✓\n- 作者: ✓ Yu, Qiying et al.\n- 年份: ✓ 2025\n- 标题: ✓ \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2503.14476\n- 正文用法: ✓ related work: \"entropy collapse\"\n- 备注: 无问题\n\n### 26. [zhang2024infuse] — ✓\n- 真实性: ✓\n- 作者: ✓ Zhang, Huajian; Xu, Yumo; Perez-Beltrachini, Laura\n- 年份: ✓ 2024\n- 标题: ✓ \"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\"\n- Venue: ✓ EACL 2024\n- arXiv ID: N/A\n- 正文用法: ✓ related work: NLI-based faithfulness evaluation\n- 备注: 无问题\n\n### 27. [wang2025rear] — ✗\n- 真实性: ✓\n- 作者: ✓ Luo, Jianwen; Hong, Yu; Yang, Shuai; Yao, Jianmin (作者内容正确)\n- 年份: ✓ 2025\n- 标题: ✓ \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\"\n- Venue: ✓ Findings EMNLP 2025\n- arXiv ID: N/A\n- 正文用法: ✗ 正文 \"\\citep{wang2025rear}\" 但首作者是 **Luo**，BibTeX 渲染为 \"Luo et al.\" 是正确的因为 author field 正确，但 cite key 命名不一致\n- 备注: **cite key \"wang2025\" 与首作者 Luo 不一致**。由于 author field 内容正确，BibTeX 渲染不受影响，但 key 命名有误导性。\n\n### 28. [wang2025relprior] — ✗\n- 真实性: ✓\n- 作者: ✓ Pi, Qiankun; Sun, Yepeng; Lu, Jicang; Fan, Qinlong; Huang, Ningbo; Wang, Shiyu (作者内容正确)\n- 年份: ✓ 2025\n- 标题: ✗ bib 标题 \"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\"。**实际 arXiv 标题是 \"Relation as a Prior: A Novel Paradigm for LLM-based Document-Level Relation Extraction\"**。\"RelPrior:\" 前缀是虚构的，\"A Novel Paradigm\" 被省略。\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2511.08143\n- 正文用法: ✓ related work: \"RelPrior leverages relation priors\" (用法合理但论文实际不以 RelPrior 为简称)\n- 备注: **标题部分虚构**。cite key \"wang2025\" 与首作者 Pi 不一致。应修正标题为 \"Relation as a Prior: A Novel Paradigm for {LLM}-based Document-Level Relation Extraction\"\n\n### 29. [zhang2025glidre] — ✗ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Armingaud, Robin; Besançon, Romaric\n- 年份: ✓ 2025\n- 标题: ✓ \"GLiDRE: Generalist Lightweight Model for Document-level Relation Extraction\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2508.00757\n- 正文用法: N/A (未在正文中被引用)\n- 备注: cite key \"zhang2025\" 但作者是 Armingaud 和 Besançon，无 Zhang。未被引用不影响论文。\n\n### 30. [tang2025rsftppo] — ✗\n- 真实性: ✓\n- 作者: ✓ Anil, Gautham Govind; Nagaraj, Dheeraj Mysore; Shanmugam, Karthikeyan; Shakkottai, Sanjay (作者内容正确)\n- 年份: ✓ 2025\n- 标题: ✓ \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\"\n- Venue: ✗ bib 写 \"ICML 2025 Workshop on Practical Aspects of Unlearning and Test-time Adaptation (PUT)\"。**实际 workshop 名为 \"2nd Workshop on Test-Time Adaptation: Putting Updates to the Test (PUT)\"**。\"Practical Aspects of Unlearning and Test-time Adaptation\" 是虚构的。\n- arXiv ID: N/A (OpenReview URL 正确)\n- 正文用法: ✓ related work: \"theoretical connections to PPO\"\n- 备注: **venue 名称虚构**。cite key \"tang2025\" 与首作者 Anil 不一致。由于 author field 正确 BibTeX 渲染不受影响，但 venue 必须修正。\n\n### 31. [wang2025rullm] — ✗ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Zhang, Kunli; Wu, Pengcheng; Yu, Bohan; Li, Yunlong; Kong, Dezhi; Zan, Hongying; Peng, Min; Song, Yu (作者内容正确)\n- 年份: ✓ 2025\n- 标题: ✓ \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\"\n- Venue: ✓ NLPCC 2025 (但 entry type 有误)\n- arXiv ID: N/A\n- 正文用法: N/A (未在正文中被引用)\n- 备注: cite key \"wang2025\" 但首作者是 Zhang。@article 应改为 @inproceedings (NLPCC 是会议)。未被引用不影响论文。\n\n### 32. [zhou2021atlop] — ✓\n- 真实性: ✓\n- 作者: ✓ Zhou, Wenxuan; Huang, Kevin; Ma, Tengyu; Huang, Jing\n- 年份: ✓ 2021\n- 标题: ✓ \"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\"\n- Venue: ✓ AAAI 2021\n- arXiv ID: ✓ 2010.11304\n- 正文用法: ✓ intro: \"encoder-based methods such as \\citet{zhou2021atlop} long dominated\"\n- 备注: 无问题\n\n### 33. [ruder2017overview] — ✓\n- 真实性: ✓\n- 作者: ✓ Ruder, Sebastian\n- 年份: ✓ 2017\n- 标题: ✓ \"An Overview of Multi-Task Learning in Deep Neural Networks\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 1706.05098\n- 正文用法: ✓ related work: \"negative transfer in multi-task learning\"\n- 备注: 无问题\n\n### 34. [standley2020tasks] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Standley, Trevor et al.\n- 年份: ✓ 2020\n- 标题: ✓ \"Which Tasks Should Be Learned Together in Multi-task Learning?\"\n- Venue: ✓ ICML 2020\n- arXiv ID: N/A\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 35. [yu2020gradient] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Yu, Tianhe et al.\n- 年份: ✓ 2020\n- 标题: ✓ \"Gradient Surgery for Multi-Task Learning\"\n- Venue: ✓ NeurIPS 2020\n- arXiv ID: ✓ 2001.06782\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 36. [wang2023selfconsistency] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Wang, Xuezhi et al.\n- 年份: ✓ 2023\n- 标题: ✓ \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\"\n- Venue: ✓ ICLR 2023\n- arXiv ID: ✓ 2203.11171\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 37. [ouyang2022instructgpt] — ✓\n- 真实性: ✓\n- 作者: ✓ Ouyang, Long et al.\n- 年份: ✓ 2022\n- 标题: ✓ \"Training Language Models to Follow Instructions with Human Feedback\"\n- Venue: ✓ NeurIPS 2022\n- arXiv ID: ✓ 2203.02155\n- 正文用法: ✓ related work/method: RLHF\n- 备注: 无问题\n\n### 38. [schulman2017ppo] — ✓\n- 真实性: ✓\n- 作者: ✓ Schulman, John; Wolski, Filip; Dhariwal, Prafulla; Radford, Alec; Klimov, Oleg\n- 年份: ✓ 2017\n- 标题: ✓ \"Proximal Policy Optimization Algorithms\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 1707.06347\n- 正文用法: ✓ related work: PPO\n- 备注: 无问题\n\n### 39. [zeng2020gain] — ✓\n- 真实性: ✓\n- 作者: ✓ Zeng, Shuang; Xu, Runxin; Chang, Baobao; Li, Lei\n- 年份: ✓ 2020\n- 标题: ✓ \"Double Graph Based Reasoning for Document-level Relation Extraction\"\n- Venue: ✓ EMNLP 2020\n- arXiv ID: N/A\n- 正文用法: ✓ related work: \"graph-based methods such as GAIN\"\n- 备注: 无问题\n\n### 40. [ethayarajh2024kto] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Ethayarajh, Kawin et al.\n- 年份: ✓ 2024\n- 标题: ✓ \"KTO: Model Alignment as Prospect Theoretic Optimization\"\n- Venue: ✓ ICML 2024\n- arXiv ID: ✓ 2402.01306\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 41. [coste2024reward] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Coste, Thomas; Anwar, Usman; Kirk, Robert; Krueger, David\n- 年份: ✓ 2024\n- 标题: ✓ \"Reward Model Ensembles Help Mitigate Overoptimization\"\n- Venue: ✓ ICLR 2024\n- arXiv ID: ✓ 2310.02743\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 42. [he2023debertav3] — ✓\n- 真实性: ✓\n- 作者: ✓ He, Pengcheng; Gao, Jianfeng; Chen, Weizhu\n- 年份: ✓ 2023\n- 标题: ✓ \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\"\n- Venue: ✓ ICLR 2023\n- arXiv ID: ✓ 2111.09543\n- 正文用法: ✓ method: NLI model \"based on DeBERTaV3\"\n- 备注: 无问题\n\n### 43. [dettmers2023qlora] — ✓\n- 真实性: ✓\n- 作者: ✓ Dettmers, Tim; Pagnoni, Artidoro; Holtzman, Ari; Zettlemoyer, Luke\n- 年份: ✓ 2023\n- 标题: ✓ \"QLoRA: Efficient Finetuning of Quantized LLMs\"\n- Venue: ✓ NeurIPS 2023\n- arXiv ID: ✓ 2305.14314\n- 正文用法: ✓ method: \"Quantized LoRA (QLoRA)\"\n- 备注: 无问题\n\n### 44. [hoffmann2022chinchilla] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Hoffmann, Jordan et al.\n- 年份: ✓ 2022\n- 标题: ✓ \"Training Compute-Optimal Large Language Models\"\n- Venue: ✓ NeurIPS 2022\n- arXiv ID: ✓ 2203.15556\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 45. [yuan2023rft] — ✓\n- 真实性: ✓\n- 作者: ✓ Yuan, Zheng et al.\n- 年份: ✓ 2023\n- 标题: ✓ \"Scaling Relationship on Learning Mathematical Reasoning with Large Language Models\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2308.01825\n- 正文用法: ✓ related work: \"subsequent scaling analyses\"\n- 备注: 无问题\n\n### 46. [tamo2026evidencerl] — ✓\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Tamo, J. Ben; Lu, Yuxing; Marteau, Benoit L.; Nnamdi, Micky C.; Wang, May D.\n- 年份: ✓ 2026 (March 2026)\n- 标题: ✓ \"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2603.19532\n- 正文用法: ✓ related work: \"reward-based evidence grounding\"\n- 备注: 无问题。2026 年引用，已验证真实存在。\n\n### 47. [liu2026rift] — ✓ (未被引用)\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Liu, Zehua; Liu, Shuqi; Zhong, Tao; Yuan, Mingxuan\n- 年份: ✓ 2026 (January 2026)\n- 标题: ✓ \"RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2601.09253\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 48. [deng2026trajfusion] — ✓ (未被引用)\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Deng, Jie; Tong, Hanshuang; Li, Jun; Liang, Shining; Wu, Ning; Li, Hongzhi; Xie, Yutao\n- 年份: ✓ 2026 (February 2026)\n- 标题: ✓ \"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2602.04391\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 49. [tian2026mugrpo] — ✓ (未被引用)\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Tian, Minghao; Xie, Yunfei; Wei, Chen\n- 年份: ✓ 2026 (May 2026)\n- 标题: ✓ \"How Off-Policy Can GRPO Be? μ-GRPO for Efficient LLM Reinforcement Learning\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2605.17570\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 50. [ji2026treegrpo] — ✓ (未被引用)\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Ji, Yuxiang; Ma, Ziyu; Wang, Yong; Chen, Guanhua; Chu, Xiangxiang; Wu, Liaoni\n- 年份: ✓ 2026\n- 标题: ✓ \"Tree Search for LLM Agent Reinforcement Learning\"\n- Venue: ✓ ICLR 2026\n- arXiv ID: ✓ 2509.21240\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 51. [deepseek2025r1] — ✓\n- 真实性: ✓\n- 作者: ✓ DeepSeek-AI\n- 年份: ✓ 2025\n- 标题: ✓ \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n- Venue: ✓ arXiv preprint (后发表于 Nature，arXiv 条目可接受)\n- arXiv ID: ✓ 2501.12948\n- 正文用法: ✓ related work: \"DeepSeek-R1 demonstrates its effectiveness at scale\"\n- 备注: 无问题\n\n### 52. [gulcehre2023rest] — ✗\n- 真实性: ✓\n- 作者: ✗ bib 列出 \"Dyer, Chris\" 和 \"Grangier, David\"，**实际应为 \"Doucet, Arnaud\" 和 \"de Freitas, Nando\"**。两个作者名错误。\n- 年份: ✓ 2023\n- 标题: ✓ \"Reinforced Self-Training (ReST) for Language Modeling\"\n- Venue: ✗ 使用 @inproceedings 但 booktitle = \"arXiv preprint arXiv:2308.08998\"，这不是合法的 venue 格式。应改为 @article。\n- arXiv ID: ✓ 2308.08998\n- 正文用法: ✓ related work: \"subsequent scaling analyses\"\n- 备注: **两个严重错误**：(1) 两个作者名错误 (Dyer→Doucet, Grangier→de Freitas)；(2) @inproceedings + arXiv preprint 作为 booktitle 是格式错误，应改为 @article\n\n---\n\n## 未被引用的 bib 条目 (17 条)\n\n以下条目存在于 references.bib 但未在任何 .tex 文件中被 \\cite，不会出现在编译后的论文中：\n\n1. moskovitz2024constrained\n2. dong2023raft\n3. ito2025mogrpo\n4. li2025drift\n5. liu2026gdpo\n6. liu2026rift\n7. deng2026trajfusion\n8. tian2026mugrpo\n9. ji2026treegrpo\n10. standley2020tasks\n11. yu2020gradient\n12. wang2023selfconsistency\n13. ethayarajh2024kto\n14. coste2024reward\n15. hoffmann2022chinchilla\n16. wang2025rullm\n17. zhang2025glidre\n\n---\n\n## 需要修正的条目 (按优先级排序)\n\n### 高优先级 (内容错误，影响论文可信度)\n\n1. **gulcehre2023rest**: 两个作者名错误 + entry type 错误\n   - \"Dyer, Chris\" → \"Doucet, Arnaud\"\n   - \"Grangier, David\" → \"de Freitas, Nando\"\n   - @inproceedings → @article, booktitle → journal\n\n2. **wang2025relprior**: 标题虚构前缀\n   - \"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\" → \"Relation as a Prior: A Novel Paradigm for LLM-based Document-Level Relation Extraction\"\n\n3. **tang2025rsftppo**: venue 名称虚构\n   - \"ICML 2025 Workshop on Practical Aspects of Unlearning and Test-time Adaptation (PUT)\" → \"2nd Workshop on Test-Time Adaptation: Putting Updates to the Test (PUT) @ ICML 2025\"\n\n4. **ma2023dreeam**: venue 错误\n   - \"Findings of the Association for Computational Linguistics: EACL 2023\" → \"Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics\"\n\n### 中优先级 (影响正确性但不致命)\n\n5. **xu2024lmrc**: cite key 导致正文显示错误作者\n   - cite key \"xu2024lmrc\" → 应改为 \"li2024lmrc\" (首作者是 Li)\n   - 正文中 \\citet 会渲染为 \"Li et al.\" (因为 author field 正确)，但读者搜索 \"xu2024\" 找不到此论文\n\n6. **li2026qurl**: venue 需更新\n   - arXiv preprint → ICLR 2026\n\n### 低优先级 (cosmetic / 仅影响未引用条目)\n\n7. **wang2025rear**: cite key 与首作者不一致 (Luo, not Wang)，但 author field 正确，BibTeX 渲染不受影响\n8. **tan2022redocred**: 标题标点 (colon vs dash)\n9. **ito2025mogrpo** / **zhang2025glidre** / **wang2025rullm**: 未引用条目的 cite key 与首作者不一致\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d29da4e-d372-4db6-9c0e-09be33cecf66",
  "isSidechain": false,
  "requestId": "req_011CbR3eGP4cX4umuGtNWxYJ",
  "type": "assistant",
  "uuid": "51f3943d-0a12-4493-8d1b-f1b38d770e57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41",
  "version": "2.1.126",
  "gitBranch": "main",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPuL2GQEWhb5foikNNoX1p",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3448,
      "cache_read_input_tokens": 112469,
      "output_tokens": 11551,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3448,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11551,
          "cache_read_input_tokens": 112469,
          "cache_creation_input_tokens": 3448,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3448
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

_source line 329 · 2026-05-26T10:49:36.950Z_

<details><summary>↩ Tool result · `toolu_01NZZ4qzWB9GvPqMjiiSFwdk`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/ref_audit_worker3.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51f3943d-0a12-4493-8d1b-f1b38d770e57",
  "isSidechain": false,
  "promptId": "8765e186-da5a-48f9-b659-e510c65c176b",
  "type": "user",
  "uuid": "c8d8f5e1-9eda-4621-abeb-07dd464e0dd0",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/ref_audit_worker3.md",
    "content": "# 引用核对清单 — Worker 3\n\n总计: 52 条引用 (35 条在正文中被引用, 17 条仅存在于 bib 文件), 11 条有问题\n\n## 问题汇总\n\n| 严重度 | 数量 | 说明 |\n|--------|------|------|\n| 高危 (内容错误) | 4 | gulcehre2023rest 作者错误, wang2025relprior 标题虚构, tang2025rsftppo 会议名虚构, ma2023dreeam venue 错误 |\n| 中等 (格式/key 问题) | 5 | xu2024lmrc/wang2025rear/wang2025rullm cite key 与首作者不一致, gulcehre2023rest entry type 错误, li2026qurl 缺少 venue 更新 |\n| 低 (仅限未引用条目) | 3 | ito2025mogrpo/zhang2025glidre cite key 错误 (未被引用), tan2022redocred 标题标点 |\n\n## 逐条结果\n\n---\n\n### 1. [autore2024] — ✓\n- 真实性: ✓\n- 作者: ✓ Xue, Lilong; Zhang, Dan; Dong, Yuxiao; Tang, Jie\n- 年份: ✓ 2024\n- 标题: ✓ \"AutoRE: Document-Level Relation Extraction with Large Language Models\"\n- Venue: ✓ ACL 2024 System Demonstrations\n- arXiv ID: ✓ 2403.14888\n- 正文用法: ✓ intro: \"fine-tune LLMs with structured decomposition\"; related work: \"uses QLoRA with relation-head-facts decomposition\"\n- 备注: 无问题\n\n### 2. [xu2025docksrag] — ✓\n- 真实性: ✓\n- 作者: ✓ Xu, Xiaolong et al.\n- 年份: ✓ 2025\n- 标题: ✓ \"DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning\"\n- Venue: ✓ ICML 2025 (PMLR 267)\n- arXiv ID: N/A\n- 正文用法: ✓ intro: \"combine retrieval-augmented generation with structured knowledge\"\n- 备注: 无问题\n\n### 3. [dai2025r1re] — ✓\n- 真实性: ✓\n- 作者: ✓ Dai, Runpeng; Zheng, Tong; Yang, Run; Yu, Kaixian; Zhu, Hongtu\n- 年份: ✓ 2025\n- 标题: ✓ \"R1-RE: Cross-Domain Relation Extraction with RLVR\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2507.04642\n- 正文用法: ✓ related work: \"applications to structured IE include R1-RE\"\n- 备注: 无问题\n\n### 4. [gao2023scaling] — ✓\n- 真实性: ✓\n- 作者: ✓ Gao, Leo; Schulman, John; Hilton, Jacob\n- 年份: ✓ 2023\n- 标题: ✓ \"Scaling Laws for Reward Model Overoptimization\"\n- Venue: ✓ ICML 2023\n- arXiv ID: ✓ 2210.10760\n- 正文用法: ✓ related work: \"capacity-dependent scaling dynamics\"; experiments: reward optimization dynamics\n- 备注: 无问题\n\n### 5. [hu2022lora] — ✓\n- 真实性: ✓\n- 作者: ✓ Hu, Edward J. et al.\n- 年份: ✓ 2022\n- 标题: ✓ \"LoRA: Low-Rank Adaptation of Large Language Models\"\n- Venue: ✓ ICLR 2022\n- arXiv ID: ✓ 2106.09685\n- 正文用法: ✓ method: \"Low-Rank Adaptation (LoRA)\"\n- 备注: 无问题\n\n### 6. [li2026qurl] — ✗\n- 真实性: ✓\n- 作者: ✓ Li, Yuhang; Elangovan, Reena; Dong, Xin; Panda, Priyadarshini; Khailany, Brucek\n- 年份: ✓ 2026\n- 标题: ✓ \"QuRL: Efficient Reinforcement Learning with Quantized Rollout\"\n- Venue: ✗ bib 列为 arXiv preprint，实际已被 **ICLR 2026** 接收\n- arXiv ID: ✓ 2602.13953\n- 正文用法: ✓ experiments: \"resembling the quantized-actor divergence of \\citet{li2026qurl}\"\n- 备注: 应更新 venue 为 ICLR 2026\n\n### 7. [laban2022summac] — ✓\n- 真实性: ✓\n- 作者: ✓ Laban, Philippe; Schnabel, Tobias; Bennett, Paul N.; Hearst, Marti A.\n- 年份: ✓ 2022\n- 标题: ✓ \"SummaC: Re-Visiting NLI-based Models for Inconsistency Detection in Summarization\"\n- Venue: ✓ TACL, vol 10, pp 163-177\n- arXiv ID: N/A\n- 正文用法: ✓ related work: NLI-based faithfulness evaluation\n- 备注: 无问题\n\n### 8. [li2025srvf] — ✓\n- 真实性: ✓\n- 作者: ✓ Li, Yongqi; Miao, Xin; Zhou, Shen; Xu, Mayi; Ren, Yuyang; Qian, Tieyun\n- 年份: ✓ 2025\n- 标题: ✓ \"Enhancing Relation Extraction via Supervised Rationale Verification and Feedback\"\n- Venue: ✓ AAAI 2025\n- arXiv ID: ✓ 2412.07289\n- 正文用法: ✓ related work: \"reward-based evidence grounding\"\n- 备注: 无问题\n\n### 9. [jin2025rl_panacea] — ✓\n- 真实性: ✓\n- 作者: ✓ Jin, Hangzhan; Lv, Sicheng; Wu, Sifan; Hamdaqa, Mohammad\n- 年份: ✓ 2025\n- 标题: ✓ \"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2508.16546\n- 正文用法: ✓ related work: \"catastrophic forgetting in RL alignment\"\n- 备注: 无问题\n\n### 10. [ma2023dreeam] — ✗\n- 真实性: ✓\n- 作者: ✓ Ma, Youmi; Wang, An; Okazaki, Naoaki\n- 年份: ✓ 2023\n- 标题: ✓ \"DREEAM: Guiding Attention with Evidence for Improving Document-Level Relation Extraction\"\n- Venue: ✗ bib 写 \"Findings of the Association for Computational Linguistics: EACL 2023\"，实际是 **EACL 2023 主会议** (ACL Anthology: 2023.eacl-main.145)\n- arXiv ID: ✓ 2302.08675\n- 正文用法: ✓\n- 备注: **venue 错误**。应改为 \"Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics\"\n\n### 11. [moskovitz2024constrained] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Moskovitz, Ted et al.\n- 年份: ✓ 2024\n- 标题: ✓ \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n- Venue: ✓ ICLR 2024\n- arXiv ID: N/A (OpenReview URL 正确)\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite，不会出现在论文中\n\n### 12. [rafailov2023direct] — ✓\n- 真实性: ✓\n- 作者: ✓ Rafailov, Rafael; Sharma, Archit; Mitchell, Eric; Ermon, Stefano; Manning, Christopher D.; Finn, Chelsea\n- 年份: ✓ 2023\n- 标题: ✓ \"Direct Preference Optimization: Your Language Model is Secretly a Reward Model\"\n- Venue: ✓ NeurIPS 2023\n- arXiv ID: ✓ 2305.18290\n- 正文用法: ✓ intro/method: DPO paradigm\n- 备注: 无问题\n\n### 13. [shao2024deepseekmath] — ✓\n- 真实性: ✓\n- 作者: ✓ Shao, Zhihong et al. (bib 中作者名略有缩写但可接受)\n- 年份: ✓ 2024\n- 标题: ✓ \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2402.03300\n- 正文用法: ✓ intro/method: GRPO\n- 备注: 无问题\n\n### 14. [tan2022redocred] — ✓ (微小问题)\n- 真实性: ✓\n- 作者: ✓ Tan, Qingyu; Xu, Lu; Bing, Lidong; Ng, Hwee Tou; Aljunied, Sharifah Mahani\n- 年份: ✓ 2022\n- 标题: ✓ (微小: 官方标题用 dash 不是 colon，但功能上可接受)\n- Venue: ✓ EMNLP 2022\n- arXiv ID: N/A\n- 正文用法: ✓\n- 备注: 官方标题用 dash \"Revisiting DocRED - Addressing...\" 而非 colon \"Revisiting DocRED: Addressing...\"，低优先级\n\n### 15. [xiao2022sais] — ✓\n- 真实性: ✓\n- 作者: ✓ Xiao, Yuxin; Zhang, Zecheng; Mao, Yuning; Yang, Carl; Han, Jiawei\n- 年份: ✓ 2022\n- 标题: ✓ \"SAIS: Supervising and Augmenting Intermediate Steps for Document-Level Relation Extraction\"\n- Venue: ✓ NAACL 2022\n- arXiv ID: N/A\n- 正文用法: ✓\n- 备注: 无问题\n\n### 16. [xie2022eider] — ✓\n- 真实性: ✓\n- 作者: ✓ Xie, Yiqing; Shen, Jiaming; Li, Sha; Mao, Yuning; Han, Jiawei\n- 年份: ✓ 2022\n- 标题: ✓ \"EIDER: Empowering Document-level Relation Extraction with Efficient Evidence Extraction and Inference-stage Fusion\"\n- Venue: ✓ Findings ACL 2022\n- arXiv ID: ✓ 2106.08657\n- 正文用法: ✓\n- 备注: 无问题\n\n### 17. [xu2024lmrc] — ✗\n- 真实性: ✓\n- 作者: ✗ bib 中作者正确列为 Li, Xingzuo et al.，但 **cite key 写 \"xu2024\" 与首作者 Li 不一致**\n- 年份: ✓ 2024\n- 标题: ✓ (bib 加了 \"LMRC:\" 前缀，arXiv 原标题无此前缀，但作为缩写惯例可接受)\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2408.13889\n- 正文用法: ✗ 正文 \"\\citet{xu2024lmrc}\" 渲染为 \"Xu et al. (2024)\"，但首作者是 **Li**，读者看到的引用与实际作者不符\n- 备注: **cite key 命名错误导致正文显示错误作者**。应改 key 为 li2024lmrc，或修正正文中所有引用\n\n### 18. [yao2019docred] — ✓\n- 真实性: ✓\n- 作者: ✓ Yao, Yuan et al.\n- 年份: ✓ 2019\n- 标题: ✓ \"DocRED: A Large-Scale Document-Level Relation Extraction Dataset\"\n- Venue: ✓ ACL 2019\n- arXiv ID: N/A\n- 正文用法: ✓\n- 备注: 无问题\n\n### 19. [zelikman2022star] — ✓\n- 真实性: ✓\n- 作者: ✓ Zelikman, Eric; Wu, Yuhuai; Mu, Jesse; Goodman, Noah D.\n- 年份: ✓ 2022\n- 标题: ✓ \"STaR: Bootstrapping Reasoning With Reasoning\"\n- Venue: ✓ NeurIPS 2022\n- arXiv ID: ✓ 2203.14465\n- 正文用法: ✓ intro/method: STaR as RSFT foundation\n- 备注: 无问题\n\n### 20. [dong2023raft] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Dong, Hanze et al.\n- 年份: ✓ 2023\n- 标题: ✓ \"RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment\"\n- Venue: ✓ TMLR\n- arXiv ID: ✓ 2304.06767\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 21. [ito2025mogrpo] — ✗ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Ichihara, Yuki; Jinnai, Yuu; Morimura, Tetsuro; Sakamoto, Mitsuki; Mitsuhashi, Ryota; Uchibe, Eiji\n- 年份: ✓ 2025\n- 标题: ✓ \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2509.22047\n- 正文用法: N/A (未在正文中被引用)\n- 备注: cite key \"ito2025\" 但首作者是 Ichihara。未被引用所以不影响论文。\n\n### 22. [li2025drift] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Li, Jiazheng; Yan, Hanqi; He, Yulan\n- 年份: ✓ 2025\n- 标题: ✓ \"Drift: Enhancing LLM Faithfulness in Rationale Generation via Dual-Reward Probabilistic Inference\"\n- Venue: ✓ ACL 2025\n- arXiv ID: N/A\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 23. [liu2026gdpo] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Liu, Shih-Yang et al.\n- 年份: ✓ 2026\n- 标题: ✓ \"GDPO: Group Reward-Decoupled Normalization Policy Optimization for Multi-Reward RL Optimization\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2601.05242\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 24. [liu2025drgrpo] — ✓\n- 真实性: ✓\n- 作者: ✓ Liu, Zichen; Chen, Changyu; Li, Wenjun; Qi, Penghui; Pang, Tianyu; Du, Chao; Lee, Wee Sun; Lin, Min\n- 年份: ✓ 2025\n- 标题: ✓ \"Understanding R1-Zero-Like Training: A Critical Perspective\"\n- Venue: ✓ Conference on Language Modeling (COLM 2025)\n- arXiv ID: ✓ 2503.20783\n- 正文用法: ✓ related work: \"length bias\" (paper proposes Dr. GRPO to address length bias)\n- 备注: cite key \"drgrpo\" 基于论文提出的方法名，可接受\n\n### 25. [yu2025dapo] — ✓\n- 真实性: ✓\n- 作者: ✓ Yu, Qiying et al.\n- 年份: ✓ 2025\n- 标题: ✓ \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2503.14476\n- 正文用法: ✓ related work: \"entropy collapse\"\n- 备注: 无问题\n\n### 26. [zhang2024infuse] — ✓\n- 真实性: ✓\n- 作者: ✓ Zhang, Huajian; Xu, Yumo; Perez-Beltrachini, Laura\n- 年份: ✓ 2024\n- 标题: ✓ \"Fine-Grained Natural Language Inference Based Faithfulness Evaluation for Diverse Summarisation Tasks\"\n- Venue: ✓ EACL 2024\n- arXiv ID: N/A\n- 正文用法: ✓ related work: NLI-based faithfulness evaluation\n- 备注: 无问题\n\n### 27. [wang2025rear] — ✗\n- 真实性: ✓\n- 作者: ✓ Luo, Jianwen; Hong, Yu; Yang, Shuai; Yao, Jianmin (作者内容正确)\n- 年份: ✓ 2025\n- 标题: ✓ \"REAR: Reinforced Reasoning Optimization for Event Argument Extraction with Relation-Aware Support\"\n- Venue: ✓ Findings EMNLP 2025\n- arXiv ID: N/A\n- 正文用法: ✗ 正文 \"\\citep{wang2025rear}\" 但首作者是 **Luo**，BibTeX 渲染为 \"Luo et al.\" 是正确的因为 author field 正确，但 cite key 命名不一致\n- 备注: **cite key \"wang2025\" 与首作者 Luo 不一致**。由于 author field 内容正确，BibTeX 渲染不受影响，但 key 命名有误导性。\n\n### 28. [wang2025relprior] — ✗\n- 真实性: ✓\n- 作者: ✓ Pi, Qiankun; Sun, Yepeng; Lu, Jicang; Fan, Qinlong; Huang, Ningbo; Wang, Shiyu (作者内容正确)\n- 年份: ✓ 2025\n- 标题: ✗ bib 标题 \"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\"。**实际 arXiv 标题是 \"Relation as a Prior: A Novel Paradigm for LLM-based Document-Level Relation Extraction\"**。\"RelPrior:\" 前缀是虚构的，\"A Novel Paradigm\" 被省略。\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2511.08143\n- 正文用法: ✓ related work: \"RelPrior leverages relation priors\" (用法合理但论文实际不以 RelPrior 为简称)\n- 备注: **标题部分虚构**。cite key \"wang2025\" 与首作者 Pi 不一致。应修正标题为 \"Relation as a Prior: A Novel Paradigm for {LLM}-based Document-Level Relation Extraction\"\n\n### 29. [zhang2025glidre] — ✗ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Armingaud, Robin; Besançon, Romaric\n- 年份: ✓ 2025\n- 标题: ✓ \"GLiDRE: Generalist Lightweight Model for Document-level Relation Extraction\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2508.00757\n- 正文用法: N/A (未在正文中被引用)\n- 备注: cite key \"zhang2025\" 但作者是 Armingaud 和 Besançon，无 Zhang。未被引用不影响论文。\n\n### 30. [tang2025rsftppo] — ✗\n- 真实性: ✓\n- 作者: ✓ Anil, Gautham Govind; Nagaraj, Dheeraj Mysore; Shanmugam, Karthikeyan; Shakkottai, Sanjay (作者内容正确)\n- 年份: ✓ 2025\n- 标题: ✓ \"Rejection Sampling Based Fine Tuning Secretly Performs PPO\"\n- Venue: ✗ bib 写 \"ICML 2025 Workshop on Practical Aspects of Unlearning and Test-time Adaptation (PUT)\"。**实际 workshop 名为 \"2nd Workshop on Test-Time Adaptation: Putting Updates to the Test (PUT)\"**。\"Practical Aspects of Unlearning and Test-time Adaptation\" 是虚构的。\n- arXiv ID: N/A (OpenReview URL 正确)\n- 正文用法: ✓ related work: \"theoretical connections to PPO\"\n- 备注: **venue 名称虚构**。cite key \"tang2025\" 与首作者 Anil 不一致。由于 author field 正确 BibTeX 渲染不受影响，但 venue 必须修正。\n\n### 31. [wang2025rullm] — ✗ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Zhang, Kunli; Wu, Pengcheng; Yu, Bohan; Li, Yunlong; Kong, Dezhi; Zan, Hongying; Peng, Min; Song, Yu (作者内容正确)\n- 年份: ✓ 2025\n- 标题: ✓ \"Ru-LLM: Logical Rule-Constrained Large Language Models for Document-Level Relation Extraction\"\n- Venue: ✓ NLPCC 2025 (但 entry type 有误)\n- arXiv ID: N/A\n- 正文用法: N/A (未在正文中被引用)\n- 备注: cite key \"wang2025\" 但首作者是 Zhang。@article 应改为 @inproceedings (NLPCC 是会议)。未被引用不影响论文。\n\n### 32. [zhou2021atlop] — ✓\n- 真实性: ✓\n- 作者: ✓ Zhou, Wenxuan; Huang, Kevin; Ma, Tengyu; Huang, Jing\n- 年份: ✓ 2021\n- 标题: ✓ \"Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling\"\n- Venue: ✓ AAAI 2021\n- arXiv ID: ✓ 2010.11304\n- 正文用法: ✓ intro: \"encoder-based methods such as \\citet{zhou2021atlop} long dominated\"\n- 备注: 无问题\n\n### 33. [ruder2017overview] — ✓\n- 真实性: ✓\n- 作者: ✓ Ruder, Sebastian\n- 年份: ✓ 2017\n- 标题: ✓ \"An Overview of Multi-Task Learning in Deep Neural Networks\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 1706.05098\n- 正文用法: ✓ related work: \"negative transfer in multi-task learning\"\n- 备注: 无问题\n\n### 34. [standley2020tasks] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Standley, Trevor et al.\n- 年份: ✓ 2020\n- 标题: ✓ \"Which Tasks Should Be Learned Together in Multi-task Learning?\"\n- Venue: ✓ ICML 2020\n- arXiv ID: N/A\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 35. [yu2020gradient] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Yu, Tianhe et al.\n- 年份: ✓ 2020\n- 标题: ✓ \"Gradient Surgery for Multi-Task Learning\"\n- Venue: ✓ NeurIPS 2020\n- arXiv ID: ✓ 2001.06782\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 36. [wang2023selfconsistency] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Wang, Xuezhi et al.\n- 年份: ✓ 2023\n- 标题: ✓ \"Self-Consistency Improves Chain of Thought Reasoning in Language Models\"\n- Venue: ✓ ICLR 2023\n- arXiv ID: ✓ 2203.11171\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 37. [ouyang2022instructgpt] — ✓\n- 真实性: ✓\n- 作者: ✓ Ouyang, Long et al.\n- 年份: ✓ 2022\n- 标题: ✓ \"Training Language Models to Follow Instructions with Human Feedback\"\n- Venue: ✓ NeurIPS 2022\n- arXiv ID: ✓ 2203.02155\n- 正文用法: ✓ related work/method: RLHF\n- 备注: 无问题\n\n### 38. [schulman2017ppo] — ✓\n- 真实性: ✓\n- 作者: ✓ Schulman, John; Wolski, Filip; Dhariwal, Prafulla; Radford, Alec; Klimov, Oleg\n- 年份: ✓ 2017\n- 标题: ✓ \"Proximal Policy Optimization Algorithms\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 1707.06347\n- 正文用法: ✓ related work: PPO\n- 备注: 无问题\n\n### 39. [zeng2020gain] — ✓\n- 真实性: ✓\n- 作者: ✓ Zeng, Shuang; Xu, Runxin; Chang, Baobao; Li, Lei\n- 年份: ✓ 2020\n- 标题: ✓ \"Double Graph Based Reasoning for Document-level Relation Extraction\"\n- Venue: ✓ EMNLP 2020\n- arXiv ID: N/A\n- 正文用法: ✓ related work: \"graph-based methods such as GAIN\"\n- 备注: 无问题\n\n### 40. [ethayarajh2024kto] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Ethayarajh, Kawin et al.\n- 年份: ✓ 2024\n- 标题: ✓ \"KTO: Model Alignment as Prospect Theoretic Optimization\"\n- Venue: ✓ ICML 2024\n- arXiv ID: ✓ 2402.01306\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 41. [coste2024reward] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Coste, Thomas; Anwar, Usman; Kirk, Robert; Krueger, David\n- 年份: ✓ 2024\n- 标题: ✓ \"Reward Model Ensembles Help Mitigate Overoptimization\"\n- Venue: ✓ ICLR 2024\n- arXiv ID: ✓ 2310.02743\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 42. [he2023debertav3] — ✓\n- 真实性: ✓\n- 作者: ✓ He, Pengcheng; Gao, Jianfeng; Chen, Weizhu\n- 年份: ✓ 2023\n- 标题: ✓ \"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\"\n- Venue: ✓ ICLR 2023\n- arXiv ID: ✓ 2111.09543\n- 正文用法: ✓ method: NLI model \"based on DeBERTaV3\"\n- 备注: 无问题\n\n### 43. [dettmers2023qlora] — ✓\n- 真实性: ✓\n- 作者: ✓ Dettmers, Tim; Pagnoni, Artidoro; Holtzman, Ari; Zettlemoyer, Luke\n- 年份: ✓ 2023\n- 标题: ✓ \"QLoRA: Efficient Finetuning of Quantized LLMs\"\n- Venue: ✓ NeurIPS 2023\n- arXiv ID: ✓ 2305.14314\n- 正文用法: ✓ method: \"Quantized LoRA (QLoRA)\"\n- 备注: 无问题\n\n### 44. [hoffmann2022chinchilla] — ✓ (未被引用)\n- 真实性: ✓\n- 作者: ✓ Hoffmann, Jordan et al.\n- 年份: ✓ 2022\n- 标题: ✓ \"Training Compute-Optimal Large Language Models\"\n- Venue: ✓ NeurIPS 2022\n- arXiv ID: ✓ 2203.15556\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 45. [yuan2023rft] — ✓\n- 真实性: ✓\n- 作者: ✓ Yuan, Zheng et al.\n- 年份: ✓ 2023\n- 标题: ✓ \"Scaling Relationship on Learning Mathematical Reasoning with Large Language Models\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2308.01825\n- 正文用法: ✓ related work: \"subsequent scaling analyses\"\n- 备注: 无问题\n\n### 46. [tamo2026evidencerl] — ✓\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Tamo, J. Ben; Lu, Yuxing; Marteau, Benoit L.; Nnamdi, Micky C.; Wang, May D.\n- 年份: ✓ 2026 (March 2026)\n- 标题: ✓ \"EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2603.19532\n- 正文用法: ✓ related work: \"reward-based evidence grounding\"\n- 备注: 无问题。2026 年引用，已验证真实存在。\n\n### 47. [liu2026rift] — ✓ (未被引用)\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Liu, Zehua; Liu, Shuqi; Zhong, Tao; Yuan, Mingxuan\n- 年份: ✓ 2026 (January 2026)\n- 标题: ✓ \"RIFT: Repurposing Negative Samples via Reward-Informed Fine-Tuning\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2601.09253\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 48. [deng2026trajfusion] — ✓ (未被引用)\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Deng, Jie; Tong, Hanshuang; Li, Jun; Liang, Shining; Wu, Ning; Li, Hongzhi; Xie, Yutao\n- 年份: ✓ 2026 (February 2026)\n- 标题: ✓ \"Beyond Rejection Sampling: Trajectory Fusion for Scaling Mathematical Reasoning\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2602.04391\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 49. [tian2026mugrpo] — ✓ (未被引用)\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Tian, Minghao; Xie, Yunfei; Wei, Chen\n- 年份: ✓ 2026 (May 2026)\n- 标题: ✓ \"How Off-Policy Can GRPO Be? μ-GRPO for Efficient LLM Reinforcement Learning\"\n- Venue: ✓ arXiv preprint\n- arXiv ID: ✓ 2605.17570\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 50. [ji2026treegrpo] — ✓ (未被引用)\n- 真实性: ✓ (2026 年论文，已通过 WebSearch 验证存在)\n- 作者: ✓ Ji, Yuxiang; Ma, Ziyu; Wang, Yong; Chen, Guanhua; Chu, Xiangxiang; Wu, Liaoni\n- 年份: ✓ 2026\n- 标题: ✓ \"Tree Search for LLM Agent Reinforcement Learning\"\n- Venue: ✓ ICLR 2026\n- arXiv ID: ✓ 2509.21240\n- 正文用法: N/A (未在正文中被引用)\n- 备注: bib 中存在但未被 \\cite\n\n### 51. [deepseek2025r1] — ✓\n- 真实性: ✓\n- 作者: ✓ DeepSeek-AI\n- 年份: ✓ 2025\n- 标题: ✓ \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\"\n- Venue: ✓ arXiv preprint (后发表于 Nature，arXiv 条目可接受)\n- arXiv ID: ✓ 2501.12948\n- 正文用法: ✓ related work: \"DeepSeek-R1 demonstrates its effectiveness at scale\"\n- 备注: 无问题\n\n### 52. [gulcehre2023rest] — ✗\n- 真实性: ✓\n- 作者: ✗ bib 列出 \"Dyer, Chris\" 和 \"Grangier, David\"，**实际应为 \"Doucet, Arnaud\" 和 \"de Freitas, Nando\"**。两个作者名错误。\n- 年份: ✓ 2023\n- 标题: ✓ \"Reinforced Self-Training (ReST) for Language Modeling\"\n- Venue: ✗ 使用 @inproceedings 但 booktitle = \"arXiv preprint arXiv:2308.08998\"，这不是合法的 venue 格式。应改为 @article。\n- arXiv ID: ✓ 2308.08998\n- 正文用法: ✓ related work: \"subsequent scaling analyses\"\n- 备注: **两个严重错误**：(1) 两个作者名错误 (Dyer→Doucet, Grangier→de Freitas)；(2) @inproceedings + arXiv preprint 作为 booktitle 是格式错误，应改为 @article\n\n---\n\n## 未被引用的 bib 条目 (17 条)\n\n以下条目存在于 references.bib 但未在任何 .tex 文件中被 \\cite，不会出现在编译后的论文中：\n\n1. moskovitz2024constrained\n2. dong2023raft\n3. ito2025mogrpo\n4. li2025drift\n5. liu2026gdpo\n6. liu2026rift\n7. deng2026trajfusion\n8. tian2026mugrpo\n9. ji2026treegrpo\n10. standley2020tasks\n11. yu2020gradient\n12. wang2023selfconsistency\n13. ethayarajh2024kto\n14. coste2024reward\n15. hoffmann2022chinchilla\n16. wang2025rullm\n17. zhang2025glidre\n\n---\n\n## 需要修正的条目 (按优先级排序)\n\n### 高优先级 (内容错误，影响论文可信度)\n\n1. **gulcehre2023rest**: 两个作者名错误 + entry type 错误\n   - \"Dyer, Chris\" → \"Doucet, Arnaud\"\n   - \"Grangier, David\" → \"de Freitas, Nando\"\n   - @inproceedings → @article, booktitle → journal\n\n2. **wang2025relprior**: 标题虚构前缀\n   - \"RelPrior: Relation as a Prior for LLM-based Document-Level Relation Extraction\" → \"Relation as a Prior: A Novel Paradigm for LLM-based Document-Level Relation Extraction\"\n\n3. **tang2025rsftppo**: venue 名称虚构\n   - \"ICML 2025 Workshop on Practical Aspects of Unlearning and Test-time Adaptation (PUT)\" → \"2nd Workshop on Test-Time Adaptation: Putting Updates to the Test (PUT) @ ICML 2025\"\n\n4. **ma2023dreeam**: venue 错误\n   - \"Findings of the Association for Computational Linguistics: EACL 2023\" → \"Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics\"\n\n### 中优先级 (影响正确性但不致命)\n\n5. **xu2024lmrc**: cite key 导致正文显示错误作者\n   - cite key \"xu2024lmrc\" → 应改为 \"li2024lmrc\" (首作者是 Li)\n   - 正文中 \\citet 会渲染为 \"Li et al.\" (因为 author field 正确)，但读者搜索 \"xu2024\" 找不到此论文\n\n6. **li2026qurl**: venue 需更新\n   - arXiv preprint → ICLR 2026\n\n### 低优先级 (cosmetic / 仅影响未引用条目)\n\n7. **wang2025rear**: cite key 与首作者不一致 (Luo, not Wang)，但 author field 正确，BibTeX 渲染不受影响\n8. **tan2022redocred**: 标题标点 (colon vs dash)\n9. **ito2025mogrpo** / **zhang2025glidre** / **wang2025rullm**: 未引用条目的 cite key 与首作者不一致\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "51f3943d-0a12-4493-8d1b-f1b38d770e57",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41",
  "version": "2.1.126",
  "gitBranch": "main"
}
```

</details>

---


### Runtime record

_source line 330 · 2026-05-26T10:49:36.979Z_

```json
{
  "parentUuid": "c8d8f5e1-9eda-4621-abeb-07dd464e0dd0",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5822ceaa-6e75-4c1e-a4e0-21e657c40b94",
  "timestamp": "2026-05-26T10:49:36.979Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41",
  "version": "2.1.126",
  "gitBranch": "main"
}
```

---


### Runtime record

_source line 331_

```json
{
  "type": "last-prompt",
  "leafUuid": "5822ceaa-6e75-4c1e-a4e0-21e657c40b94",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41"
}
```

---


### Runtime record

_source line 332_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit all 52 references in faith-evidence-ie paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41"
}
```

---


### Assistant

_source line 333 · 2026-05-26T10:49:47.155Z_

审计报告已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/ref_audit_worker3.md`。

**结果概要：52 条引用全部验证，11 条有问题，0 条虚构。**

**高优先级修正（4 条）：**
1. **gulcehre2023rest** — 两个作者名错误（Dyer→Doucet, Grangier→de Freitas）+ @inproceedings 应为 @article
2. **wang2025relprior** — 标题虚构了 "RelPrior:" 前缀，真实标题是 "Relation as a Prior: A Novel Paradigm for..."
3. **tang2025rsftppo** — venue 名称虚构（"Practical Aspects of Unlearning..." → 实际是 "2nd Workshop on Test-Time Adaptation: Putting Updates to the Test"）
4. **ma2023dreeam** — venue 错误：不是 Findings EACL 2023，是 EACL 2023 主会议

**中优先级（2 条）：**
5. **xu2024lmrc** — cite key "xu" 但首作者是 Li，\citet 渲染不受影响但 key 误导
6. **li2026qurl** — 已被 ICLR 2026 接收，应更新 venue

**所有 2026 年引用（7 条）均已验证为真实存在的论文。** 另有 17 条 bib 条目未在正文中被 \cite，不会出现在编译后的 PDF 中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5822ceaa-6e75-4c1e-a4e0-21e657c40b94",
  "isSidechain": false,
  "requestId": "req_011CbR3t67Ze9kXcHJEzwKrd",
  "type": "assistant",
  "uuid": "111494ae-4def-4551-92de-891666c59670",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/docs/paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41",
  "version": "2.1.126",
  "gitBranch": "main",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASvfkcu4ecdqmcKmK9sGp2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11709,
      "cache_read_input_tokens": 115917,
      "output_tokens": 456,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11709,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 456,
          "cache_read_input_tokens": 115917,
          "cache_creation_input_tokens": 11709,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11709
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

_source line 334_

```json
{
  "type": "last-prompt",
  "leafUuid": "111494ae-4def-4551-92de-891666c59670",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41"
}
```

---


### Runtime record

_source line 335_

```json
{
  "type": "ai-title",
  "aiTitle": "Audit all 52 references in faith-evidence-ie paper",
  "sessionId": "7ad27970-2427-4427-8982-3e07c0bbdf41"
}
```

---
