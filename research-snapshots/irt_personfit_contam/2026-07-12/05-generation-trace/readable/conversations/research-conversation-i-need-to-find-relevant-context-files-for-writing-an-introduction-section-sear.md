# Research conversation: I need to find relevant context files for writing an Introduction section. Search in /home/ubuntu/.agent-ml-research-be-

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a30c0bb91d2c09315.jsonl`
- **Structured JSON:** [`f78d5e2117975379520f.json`](../../sessions/f7/f78d5e2117975379520f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

21 recorded events

### User

_source line 1 · 2026-05-20T23:15:37.469Z_

I need to find relevant context files for writing an Introduction section. Search in /home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ for:

1. writing_plan.yaml - the full writing plan
2. Any existing .tex files in paper/ directory
3. Any ideas.md, report.md, or similar knowledge files
4. Any ROADMAP.md or memory.md

Search breadth: medium. Report the file paths you find and the first ~100 lines of the most important ones (writing_plan.yaml, any existing sections).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5a905e93-7981-422f-9766-0fbbede8e369",
  "agentId": "a30c0bb91d2c09315",
  "type": "user",
  "uuid": "faf3b7e5-7d5e-4968-848c-a0619dc1bc0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-20T23:15:39.268Z_

I'll search for those key files in the project directory. Let me start with a broad search and then read the most important ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "faf3b7e5-7d5e-4968-848c-a0619dc1bc0d",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfv5ov1K19CzU2rwcZ2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4ab9b0b7-8a60-4970-8d45-c41a5bc9f89b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EsMPbUXbo5Sp677Pv7XJ8C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25392,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T23:15:39.704Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01WrCJUzAvjYjaqZheXScTHd`</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ab9b0b7-8a60-4970-8d45-c41a5bc9f89b",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfv5ov1K19CzU2rwcZ2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e033c7ec-dae5-4f96-8305-34e0f6b05dfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EsMPbUXbo5Sp677Pv7XJ8C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25392,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T23:15:39.900Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01L7EeKQ7m6qe1nbY9CACDxS`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e033c7ec-dae5-4f96-8305-34e0f6b05dfc",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfv5ov1K19CzU2rwcZ2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "246859b4-cb47-401e-bfe2-615f9ce2349f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EsMPbUXbo5Sp677Pv7XJ8C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25392,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 25392,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T23:15:39.974Z_

<details><summary>↩ Tool result · `toolu_01WrCJUzAvjYjaqZheXScTHd`</summary>

```text
artifacts/dream_reports/dream_20260520T082549/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T082549/best/review_context.yaml
artifacts/dream_reports/dream_20260520T082549/median/review_context.yaml
artifacts/dream_reports/dream_20260520T082549/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T092614/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T092614/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T092614/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T092614/best/review_context.yaml
artifacts/dream_reports/dream_20260520T092614/median/review_context.yaml
artifacts/dream_reports/dream_20260520T092614/worst/review_context.yaml
.venv/lib/python3.14/site-packages/markdown_it/port.yaml
.venv/lib/python3.14/site-packages/datasets/utils/resources/readme_structure.yaml
artifacts/dream_reports/dream_20260520T092614/meta.yaml
.venv/lib/python3.14/site-packages/torch/_export/serde/schema.yaml
.venv/lib/python3.14/site-packages/torchgen/packaged/ATen/native/native_functions.yaml
.venv/lib/python3.14/site-packages/torchgen/packaged/ATen/native/tags.yaml
.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/deprecated.yaml
.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/derivatives.yaml
artifacts/dream_reports/dream_20260520T105545/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T105545/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T105545/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T105545/best/review_context.yaml
artifacts/dream_reports/dream_20260520T105545/median/review_context.yaml
artifacts/dream_reports/dream_20260520T105545/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T105545/meta.yaml
distill_tmp/atlas2025.yaml
distill_tmp/selfcritique2026.yaml
distill_tmp/karabatsos2003.yaml
distill_tmp/hong2021lzm.yaml
distill_tmp/minkprob2024.yaml
distill_tmp/psnirt2026.yaml
distill_tmp/constat2024.yaml
distill_tmp/sinharay2017.yaml
distill_tmp/wang2025fragility.yaml
distill_tmp/codec2026.yaml
experiment_plan.yaml
artifacts/dream_reports/dream_20260520T190245/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T190245/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T190245/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260520T190245/best/review_context.yaml
artifacts/dream_reports/dream_20260520T190245/median/review_context.yaml
artifacts/dream_reports/dream_20260520T190245/worst/review_context.yaml
artifacts/dream_reports/dream_20260520T190245/meta.yaml
dream_registry.yaml
artifacts/review_issues.yaml
literature_map.yaml
writing_plan.yaml
artifacts/manifest.yaml
registry.yaml
decisions.yaml
mistakes.yaml
paper_provenance.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e033c7ec-dae5-4f96-8305-34e0f6b05dfc",
  "isSidechain": true,
  "promptId": "5a905e93-7981-422f-9766-0fbbede8e369",
  "agentId": "a30c0bb91d2c09315",
  "type": "user",
  "uuid": "ebf0afd3-c69a-4b30-ae7b-06e5c6ba6961",
  "sourceToolAssistantUUID": "e033c7ec-dae5-4f96-8305-34e0f6b05dfc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T23:15:40.130Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012Pt9z56RxGaaFyRzniQpme`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebf0afd3-c69a-4b30-ae7b-06e5c6ba6961",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfv5ov1K19CzU2rwcZ2",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "487a2d7a-fae2-4d6c-b6a4-f84c39f6b814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EsMPbUXbo5Sp677Pv7XJ8C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25392,
      "cache_read_input_tokens": 0,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 25392
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 300,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 25392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 25392,
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

### Tool result

_source line 7 · 2026-05-20T23:15:40.179Z_

<details><summary>↩ Tool result · `toolu_01L7EeKQ7m6qe1nbY9CACDxS`</summary>

```text
artifacts/dream_reports/dream_20260520T082549/best/paper.tex
artifacts/dream_reports/dream_20260520T082549/median/paper.tex
artifacts/dream_reports/dream_20260520T082549/worst/paper.tex
artifacts/dream_reports/dream_20260520T092614/best/paper.tex
artifacts/dream_reports/dream_20260520T092614/median/paper.tex
artifacts/dream_reports/dream_20260520T092614/worst/paper.tex
artifacts/dream_reports/dream_20260520T105545/best/paper.tex
artifacts/dream_reports/dream_20260520T105545/median/paper.tex
artifacts/dream_reports/dream_20260520T105545/worst/paper.tex
artifacts/dream_reports/dream_20260520T190245/best/paper.tex
artifacts/dream_reports/dream_20260520T190245/median/paper.tex
artifacts/dream_reports/dream_20260520T190245/worst/paper.tex
paper/main.tex
paper/sections/introduction.tex
paper/sections/appendix.tex
paper/sections/abstract.tex
paper/sections/limitations.tex
paper/sections/discussion.tex
paper/sections/conclusion.tex
artifacts/_project/paper/sec_setup.tex
paper/sections/experiments.tex
paper/sections/sec_setup.tex
docs/paper/sec_setup.tex
paper/sections/sec_empirical.tex
docs/paper/sec_empirical.tex
paper/sections/sec_simulation.tex
docs/paper/sec_simulation.tex
paper/sections/method.tex
artifacts/_project/paper/method.tex
paper/sections/sec_ctrl_contam.tex
docs/paper/sec_ctrl_contam.tex
docs/paper/sec_method.tex
paper/sections/background.tex
docs/paper/sec_background.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "246859b4-cb47-401e-bfe2-615f9ce2349f",
  "isSidechain": true,
  "promptId": "5a905e93-7981-422f-9766-0fbbede8e369",
  "agentId": "a30c0bb91d2c09315",
  "type": "user",
  "uuid": "5a664bdd-35b7-4c31-8875-3a7991c3dcae",
  "sourceToolAssistantUUID": "246859b4-cb47-401e-bfe2-615f9ce2349f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T23:15:40.376Z_

<details><summary>↩ Tool result · `toolu_012Pt9z56RxGaaFyRzniQpme`</summary>

```text
artifacts/psn_irt_data_report.md
.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md
.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/philox/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
.venv/lib/python3.14/site-packages/scipy/fft/_pocketfft/LICENSE.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260520T082549/best/paper_framing.md
artifacts/dream_reports/dream_20260520T082549/median/paper_framing.md
artifacts/dream_reports/dream_20260520T082549/worst/paper_framing.md
artifacts/_project/report/analysis_report.md
artifacts/phase_b_two_sided_v2/analysis_report.md
artifacts/dream_reports/dream_20260520T082549/best/review_report.md
artifacts/dream_reports/dream_20260520T082549/median/review_report.md
artifacts/dream_reports/dream_20260520T092614/best/paper_framing.md
artifacts/dream_reports/dream_20260520T092614/median/paper_framing.md
artifacts/dream_reports/dream_20260520T092614/worst/paper_framing.md
artifacts/exp-leaderboard-data-recon/report/report.md
artifacts/leaderboard_data_recon/report.md
artifacts/exp-empirical-null/report/unflagged_analysis.md
artifacts/empirical_null_analysis/unflagged_analysis.md
artifacts/dream_reports/dream_20260520T092614/best/review_report.md
artifacts/dream_reports/dream_20260520T092614/median/review_report.md
.venv/lib/python3.14/site-packages/pyarrow/tests/data/orc/README.md
.venv/lib/python3.14/site-packages/idna-3.15.dist-info/licenses/LICENSE.md
.venv/lib/python3.14/site-packages/httpcore-1.0.9.dist-info/licenses/LICENSE.md
.venv/lib/python3.14/site-packages/httpx-0.28.1.dist-info/licenses/LICENSE.md
.venv/lib/python3.14/site-packages/typer/.agents/skills/typer/SKILL.md
.venv/lib/python3.14/site-packages/huggingface_hub/templates/datasetcard_template.md
.venv/lib/python3.14/site-packages/huggingface_hub/templates/modelcard_template.md
artifacts/dream_reports/dream_20260520T092614/worst/review_report.md
artifacts/exp-power-theory/report/theory_derivation.md
artifacts/power_theory/theory_derivation.md
artifacts/exp-power-theory/report/inverted_u_theory.md
artifacts/power_theory/inverted_u_theory.md
artifacts/exp-item-alignment-check/report/alignment_report.md
artifacts/item_alignment_check/alignment_report.md
.venv/lib/python3.14/site-packages/pyro_api-0.1.2.dist-info/LICENSE.md
.venv/lib/python3.14/site-packages/cuda/pathfinder/README.md
.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/README.md
.venv/lib/python3.14/site-packages/pyro_ppl-1.9.1.dist-info/LICENSE.md
artifacts/dream_reports/dream_20260520T105545/best/paper_framing.md
artifacts/dream_reports/dream_20260520T105545/median/paper_framing.md
artifacts/dream_reports/dream_20260520T105545/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T105545/best/review_report.md
artifacts/dream_reports/dream_20260520T105545/median/review_report.md
artifacts/exp-accuracy-zscore-baseline/report/comparison_report.md
artifacts/accuracy_zscore_baseline/comparison_report.md
artifacts/cross_benchmark_analysis/analysis_report.md
artifacts/exp-cross-benchmark-analysis/report/analysis_report.md
artifacts/dream_reports/dream_20260520T105545/worst/review_report.md
.claude/sessions/distiller_a1b59f48/CLAUDE.md
.claude/sessions/distiller_a1b59f48/AGENTS.md
.venv/lib/python3.14/site-packages/sklearn/externals/array_api_compat/README.md
.venv/lib/python3.14/site-packages/sklearn/externals/array_api_extra/README.md
artifacts/_project/report/delta_report.md
artifacts/clean_control_delta/delta_report.md
artifacts/v1_irt_refit_pilot/feasibility_report.md
artifacts/exp-v1-irt-refit-pilot/report/feasibility_report.md
artifacts/ml_classifier_baseline/report/analysis_report.md
artifacts/ml_classifier_baseline/analysis_report.md
artifacts/_project/report/domain_report.md
artifacts/domain_analysis/domain_report.md
artifacts/natural_experiment/natural_experiment_report.md
artifacts/natural_experiment/report/natural_experiment_report.md
artifacts/_project/report/virology_diagnostic_report.md
artifacts/domain_analysis/virology_diagnostic_report.md
artifacts/4pl_ablation/ablation_report.md
artifacts/4pl_ablation/report/ablation_report.md
artifacts/exp-v1-irt-refit-expanded/report/expanded_report.md
artifacts/v1_irt_refit_expanded/expanded_report.md
artifacts/4pl_real_data_degradation/degradation_report.md
artifacts/exp-4pl-real-data-degradation/report/degradation_report.md
.claude/sessions/agent_0d2e4332/CLAUDE.md
.claude/sessions/agent_0d2e4332/AGENTS.md
artifacts/dream_reports/dream_20260520T190245/best/paper_framing.md
artifacts/dream_reports/dream_20260520T190245/median/paper_framing.md
artifacts/dream_reports/dream_20260520T190245/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T190245/best/review_report.md
artifacts/dream_reports/dream_20260520T190245/median/review_report.md
artifacts/dream_reports/dream_20260520T190245/worst/review_report.md
.claude/sessions/review_reviewer_1_ac4dc473/CLAUDE.md
.claude/sessions/review_reviewer_1_ac4dc473/AGENTS.md
.claude/sessions/review_reviewer_2_956ba1bc/CLAUDE.md
.claude/sessions/review_reviewer_2_956ba1bc/AGENTS.md
artifacts/review_reports/round_0.md
.claude/sessions/review_director_34e01ffa/CLAUDE.md
.claude/sessions/review_director_34e01ffa/AGENTS.md
memory.md
.claude/sessions/agent_0c707a6f/CLAUDE.md
.claude/sessions/agent_0c707a6f/AGENTS.md
.claude/sessions/agent_272f846c/CLAUDE.md
.claude/sessions/agent_272f846c/AGENTS.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "487a2d7a-fae2-4d6c-b6a4-f84c39f6b814",
  "isSidechain": true,
  "promptId": "5a905e93-7981-422f-9766-0fbbede8e369",
  "agentId": "a30c0bb91d2c09315",
  "type": "user",
  "uuid": "a0b8f8ad-8853-4bb8-969c-090b7067db45",
  "sourceToolAssistantUUID": "487a2d7a-fae2-4d6c-b6a4-f84c39f6b814",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-20T23:15:42.246Z_

Good! I found the key files. Now let me read the most important ones: writing_plan.yaml, memory.md, and the existing introduction.tex section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0b8f8ad-8853-4bb8-969c-090b7067db45",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfvJAomTMUQL51UyFmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d88970f-56ec-4c0d-87b3-c8c9e1694a78",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CjP4h3ZUy9VgqV2kK6aCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 25392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T23:15:43.229Z_

<details open><summary>🔧 Tool call — Read · `toolu_0129ftvhDYqoU7ncTBxdAkCz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d88970f-56ec-4c0d-87b3-c8c9e1694a78",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfvJAomTMUQL51UyFmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2ee86377-a315-4aec-b340-c82f6583131e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CjP4h3ZUy9VgqV2kK6aCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 25392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T23:15:43.305Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Cga1Fhgd7J2UBVhb53aPvc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ee86377-a315-4aec-b340-c82f6583131e",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfvJAomTMUQL51UyFmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bdf38faf-024d-4d30-b344-a4d97ad557b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CjP4h3ZUy9VgqV2kK6aCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 25392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T23:15:43.612Z_

<details><summary>↩ Tool result · `toolu_0129ftvhDYqoU7ncTBxdAkCz`</summary>

```text
1	meta:
2	  title: "IRT-FIT: Detecting LLM Benchmark Contamination via Person-Fit Statistics at the Minimal-Information Operating Point"
3	  venue: EMNLP 2026 Main (ARR Jun 15 cycle)
4	  format: Long paper, 8-page main text + unlimited references
5	  template: acl2023  # ACL rolling review standard template; Worker 下载 https://github.com/acl-org/acl-style-files
6	  template_note: "EMNLP 2026 通过 ARR 统一审稿，使用 ACL 标准模板。若 2026 版模板已发布，Worker 应优先使用。"
7	  created_at: "2026-05-20T20:00:00Z"
8	  verify_refs: true
9	  director_approved_at: "2026-05-20T20:10:00Z"
10	  score_target: "3.0-3.25 (Findings / Borderline Conference)"
11	
12	# ============================================================
13	# DIRECTOR ACTION ITEMS (Dream 审稿 + Reviewer 复核定稿)
14	# ============================================================
15	action_items:
16	  critical:
17	    - id: AI-1
18	      desc: "4PL 参数来源：PSN-IRT (Lee et al., AAAI 2026)，不是 py-irt 或 ltm。lz* 由项目自实现 (numpy/scipy)"
19	      target_section: sec_method
20	      status: pending
21	
22	  method:
23	    - id: AI-6
24	      desc: "IRT 假设违反的显式讨论：≥1 段解释 lz* 在 local independence/unidimensionality 违反下的诊断价值。核心论点：Δlz* 作为 DiD 设计，系统性偏差在差分中被消除"
25	      target_section: sec_method
26	      status: pending
27	    - id: AI-7
28	      desc: "Δlz* 设计 + bootstrap null 校准：universal misfit 是 finding 不是 artifact，Δlz* bypasses absolute thresholds"
29	      target_section: sec_method
30	      status: pending
31	
32	  results:
33	    - id: AI-8
34	      desc: "Type-I error 专段：bootstrap null mean bias 0.041, std 1.003, KS reject rate 8.3%"
35	      target_section: sec_simulation
36	      status: pending
37	    - id: AI-9
38	      desc: "Clean-clean Δlz* baseline drift：n=3 seeds lz* 分布，0.70 noise floor，contam signal 5.7× above"
39	      target_section: sec_ctrl_contam
40	      status: pending
41	    - id: AI-10
42	      desc: "Binary-only baseline 对比：lz* 57/60 vs accuracy z-score 4/60 (14×)。模拟中 lz* ≥ ML classifiers at 5-10%"
43	      target_section: sec_empirical
44	      status: pending
45	
46	  discussion:
47	    - id: AI-11
48	      desc: "单模型 ctrl-contam 泛化性限制：仅 Qwen2.5-7B × MMLU。Future work: multi-family"
49	      target_section: sec_limitations
50	      status: pending
51	    - id: AI-12
52	      desc: "QLoRA low-rank bias：memorization ~38% 可能是 QLoRA lower bound，full FT 可能更强信号"
53	      target_section: sec_limitations
54	      status: pending
55	    - id: AI-13
56	      desc: "Post-RL 措辞约束：不写 'robust to post-RL'。写 'structurally invariant to RL distributional changes — empirical verification is future work'"
57	      target_section: [sec_introduction, sec_discussion]
58	      status: pending
59	
60	  urgent_corrections:
61	    - id: UC-1
62	      desc: "57/60 vs 4/60 是 universal misfit 证据 (Claim 3a)，不是 contamination detection 证据。用于论证 lz* 捕获 accuracy 聚合后丢失的 response-pattern 信息。Contamination detection 优势用: 模拟 AUROC +0.10@5%, ctrl-contam |d|=3.58, lz*≥ML classifiers at 5-10%"
63	      target_section: [sec_empirical, sec_simulation]
64	      status: pending
65	    - id: UC-2
66	      desc: "KS 校准率分层报告：MMLU 8.3%, HellaSwag 8.3% (well-calibrated); HumanEval 75%, ARC-C 58.3% (poorly calibrated); 总体 40% (24/60)。不能只引用 8.3%。按 benchmark size 分层 + 说明 large benchmarks well-calibrated"
67	      target_section: sec_simulation
68	      status: pending
69	    - id: UC-3
70	      desc: "QLoRA bias 框架为 'results may be conservative' 而非 limitation。rank=16 限制 memorization → 38% 是保守下界 → full FT 信号预期更强 → 强化结论。~50 词 Limitations"
71	      target_section: sec_limitations
72	      status: pending
73	
74	  missing_refs:
75	    - "Drasgow, Levine & Williams (1985) — person-fit foundations"
76	    - "Karabatsos (2003) — already in map, need verify"
77	    - "Meijer & Sijtsma (2001) — person-fit survey"
78	    - "Oren et al. (2024) — proving test set contamination"
79	    - "Polo et al. (2024) — tinyBenchmarks"
80	    - "Magar & Schwartz (2022) — data contamination"
81	    - "Deng et al. (2024) — contamination detection"
82	    - "Burnham et al. (2024) — IRT for AI"
83	    - "Jacobs et al. (2024) — psychometrics and AI"
84	
85	# ============================================================
86	# PAPER OUTLINE
87	# ============================================================
88	paper_outline:
89	  abstract:
90	    word_budget: 200
91	    dependencies: [sec_experiments, sec_method]
92	    key_elements:
93	      - problem statement (contamination + privileged access gap)
94	      - minimal-information operating point framing
95	      - "3 result highlights: (1) ctrl-contam |d|=3.58@15%, (2) power function R²=0.957, (3) universal misfit finding"
96	      - scope precision (SFT contamination, not pretraining exposure)
97	    constraints:
98	      - no "state-of-the-art" (no SOTA comparison done)
99	      - no "significantly" without statistical test
100	      - numbers must match sec_experiments exactly
101	
102	  sec_introduction:
103	    label: "Introduction"
104	    word_budget: 700
105	    dependencies: []
106	    subsections: []
107	    key_elements:
108	      - "P1: Problem — contamination threatens evaluation integrity, structural cause (training corpora ∩ public benchmarks)"
109	      - "P2: Existing methods critique — ALL require privileged access. Detection frontier ranking: binary < rephrased retest < token probs < logits < weights"
110	      - "P3: RL-robustness motivation — Wang et al. shows all 10 log-prob methods ≈ random on RL models. Binary patterns structurally immune to RL distributional shifts"
111	      - "P4: Cross-domain insight — contaminated LLM ≡ examinee with item preknowledge. Person-fit literature: decades of cheating detection. Gap: 0/N papers connect person-fit to LLM contamination"
112	      - "P5: Our approach — IRT-FIT at minimal-information operating point. Key results preview (numbers from experiments)"
113	      - "P6: 3 contributions (method+characterization+empirical findings), escalating scope"
114	    narrative_strategy:
115	      story_type: "跨界迁移型 (unused in 0/8 peer papers — our differentiator)"
116	      hook: "ConStat definitional pivot: 'All prior methods require privileged access. We ask: what can be detected from binary response patterns alone?'"
117	      techniques:
118	        - "Wang's negative-result-first: prove existing methods fail → create urgency"
119	        - "PSN-IRT's numbered findings for scannability"
120	
121	  sec_background:
122	    label: "Background and Related Work"
123	    word_budget: 650
124	    dependencies: []
125	    subsections:
126	      - id: sec_irt_background
127	        label: "IRT and Person-Fit Statistics"
128	        word_budget: 350
129	        key_elements:
130	          - "4PL model equation: P(X=1|θ) = c + (d-c)·sigmoid(a(θ-b))"
131	          - "d parameter importance for LLMs (ceiling effects, 46% MMLU items d<0.95)"
132	          - "lz* definition + N(0,1) null + interpretation (negative=aberrant, positive=over-consistent)"
133	          - "Snijders (2001) variance correction"
134	          - "Person-fit for cheating detection in psychometrics (Karabatsos 2003, Sinharay 2017)"
135	        constraints:
136	          - self-contained for ML reviewers unfamiliar with psychometrics
137	          - avoid jargon without definition
138	          - IRT 形式化定义（4PL 公式 + lz* 公式）保留正文，推导细节移至 Appendix
139	          - 正文只保留直觉解释 + 核心公式
140	
141	      - id: sec_contamination_related
142	        label: "Benchmark Contamination Detection"
143	        word_budget: 300
144	        key_elements:
145	          - "Detection frontier table reference (Table 1)"
146	          - "5 method families: time-based partition, MIA/Min-K%++, Time Travel, ConStat, CoDeC"
147	          - "Wang et al. RL-robustness failure"
148	          - "Position IRT-FIT at bottom of frontier (minimum information access)"
149	          - "IRT for LLM evaluation (PSN-IRT, ATLAS) — related but not person-fit"
150	
151	  sec_method:
152	    label: "Method"
153	    word_budget: 600
154	    dependencies: [sec_background]
155	    subsections:
156	      - id: sec_framework
157	        label: "IRT-FIT Framework"
158	        word_budget: 200
159	        key_elements:
160	          - "Input: binary response matrix X (models × items) + calibrated 4PL parameters"
161	          - "Step 1: θ estimation (MLE per benchmark)"
162	          - "Step 2: lz* computation per (model, benchmark) cell"
163	          - "Step 3: Δlz* for within-model contamination detection"
164	          - "Item parameter source: PSN-IRT calibrated 4PL (cite psnirt2026)"
165	          - "No training data needed — unsupervised, per-cell statistic"
166	
167	      - id: sec_power_characterization
168	        label: "Detection Power Characterization"
169	        word_budget: 220
170	        key_elements:
171	          - "Power as function of n_items and contamination level"
172	          - "Theoretical derivation from Snijders (2001) variance formula: δ ∝ √n"
173	          - "Two-sided detection: partial contamination → aberrant (lz*<<0), full → over-consistent (lz*>>0)"
174	          - "Crossover point at ~81-85% contamination"
175	          - "Upper bound vs adjusted power (memorization fraction from ctrl-contam)"
176	          - "Minimum items guideline for practitioners"
177	
178	      - id: sec_theta_shift
179	        label: "θ-Shift and θ-Fixed Analysis"
180	        word_budget: 180
181	        key_elements:
182	          - "θ-shift mechanism: contamination → higher accuracy → higher θ_MLE → absorbs aberrance signal"
183	          - "θ-fixed solution: use pre-contamination θ baseline"
184	          - "Dose-response: free-θ non-monotonic, fixed-θ restores monotonicity (ratio=2.93)"
185	          - "Practical implication: cross-validated θ or external θ anchor"
186	
187	  sec_experiments:
188	    label: "Experiments"
189	    word_budget: 1000
190	    dependencies: [sec_method]
191	    subsections:
192	      - id: sec_setup
193	        label: "Experimental Setup"
194	        word_budget: 150
195	        key_elements:
196	          - "Benchmarks: MMLU (14042), HellaSwag (10042), GSM8K (1319), ARC-C (295), HumanEval (164)"
197	          - "Item parameters: PSN-IRT 4PL calibrated (cite psnirt2026)"
198	          - "12-model PSN-IRT dataset for empirical analysis"
199	          - "Controlled contamination: Qwen2.5-7B-Instruct, QLoRA SFT (r=16, α=32)"
200	          - "Conditions: clean×2(+s3), contam_15%, contam_50%"
201	          - "Simulation: 2000 replicates per condition, 11 contamination levels"
202	
203	      - id: sec_simulation
204	        label: "Simulation Validation"
205	        word_budget: 230
206	        key_elements:
207	          - "4PL null check: lz* ~ N(0,1) confirmed (all benchmarks KS pass)"
208	          - "Power results: MMLU@15%=97.9% (two-sided=97.8%), refer to Figure 2"
209	          - "Power scales with √n_items (theory R²=0.957)"
210	          - "Two-sided detection eliminates inverted-U: >93% all levels for MMLU"
211	          - "4PL vs 3PL ablation: mean +14-27pp power gain (refer to appendix Figure A1)"
212	          - "ML classifier comparison: lz* outperforms LR/RF at 5-10% contamination (+0.05-0.10 AUROC) without training data"
213	          - "Report bootstrap CIs (our differentiator vs 6/8 peers)"
214	        exp_ids: [sim_001, exp-extended-sim, exp-power-theory, exp-4pl-ablation, exp-ml-classifier-baseline, exp-clean-control-delta]
215	
216	      - id: sec_ctrl_contam
217	        label: "Controlled Contamination"
218	        word_budget: 300
219	        key_elements:
220	          - "Design: QLoRA SFT injection on Qwen2.5-7B-Instruct × MMLU"
221	          - "5 conditions: clean_s1 (seed=42), clean_s2 (seed=123), clean_s3 (seed=456), contam_15%, contam_50%"
222	          - "Clean baseline: report individual seeds s1=8.01, s2=5.94, s3=8.08 (mean=7.35±1.21); note s2 ~26% lower (seed-specific training dynamics)"
223	          - "Key Finding 1: contam_15% |Cohen's d|=3.58, contam_50% |d|=1.56 (ddof=1, n=3)"
224	          - "Key Finding 2: free-θ dose-response non-monotonic (contam_50 Δlz*=-1.90 < contam_15 Δlz*=-4.34)"
225	          - "Key Finding 3: θ-fixed restores monotonicity (Δlz*_fixed: 15%=+2.68, 50%=+8.36, ratio=3.12)"
226	          - "Key Finding 4: seen/unseen split — contam_15 seen lz*≈0 vs unseen=3.1 (memorization fingerprint)"
227	          - "Key Finding 5: memorization_fraction=0.38 (15%), 0.29 (50%) — SFT generalization effect"
228	          - "θ-shift mechanism quantification: Δθ=0.30 (15%), 0.47 (50%)"
229	          - "Present as numbered findings (PSN-IRT style)"
230	          - "Appendix: seed sensitivity (~30 words) — s2 outlier discussion"
231	        exp_ids: [exp-ctrl-contam-pilot]
232	
233	      - id: sec_empirical
234	        label: "Empirical Findings from Real LLM Data"
235	        word_budget: 320
236	        key_elements:
237	          - "Finding (a): Universal 4PL misfit — 57/60 cells flagged after BH-FDR (not artifact: bootstrap null well-calibrated)"
238	          - "Finding (b): 12-model case study — Gemini-1.5 MMLU acc=100%, θ=0.78, lz*=+34.75; selective vs uniform misfit profiles; Ward clustering typology; domain analysis (50/57 MMLU subjects flagged)"
239	          - "Finding (c): IRT parameter estimation gap — MML-EM refit N=178, b_r=0.66 (partial), a_r=0.13 (failure). Classical IRT sample requirements vs neural IRT"
240	          - "4PL vs 3PL on real data: r=0.225, RMSE=68.41 (d parameter essential for high-ability models)"
241	          - "Accuracy z-score baseline: 4/60 flagged vs lz* 57/60 — lz* captures pattern information beyond accuracy"
242	          - "Negative results framed as contributions: simulation-reality gap is informative"
243	        exp_ids: [phase_b_personfit, exp-two-sided, exp-fdr-correction, exp-empirical-null, exp-cross-benchmark-analysis, exp-accuracy-zscore-baseline, exp-4pl-real-data-degradation, exp-v1-irt-refit-expanded, exp-domain-analysis]
244	
245	  sec_discussion:
246	    label: "Discussion"
247	    word_budget: 200
248	    dependencies: [sec_experiments]
249	    key_elements:
250	      - "Simulation-reality gap interpretation: well-calibrated null + universal misfit → LLMs genuinely violate IRT assumptions"
251	      - "Δlz* design as practical solution: within-model comparison leverages well-calibrated null"
252	      - "Scalability: 13K+ v1 per-item data publicly available, binary-only → retrospective audit feasible"
253	      - "Scope: SFT contamination / leaderboard gaming, not pretraining exposure"
254	      - "Future work: large-scale leaderboard audit (pending estimation advances), multi-model-family ctrl-contam, post-RL validation"
255	
256	  sec_conclusion:
257	    label: "Conclusion"
258	    word_budget: 150
259	    dependencies: [sec_discussion]
260	    key_elements:
261	      - "Summary: minimal-information operating point, 3 findings"
262	      - "Impact: any evaluation that records binary responses can retrospectively check for contamination"
263	      - "No overclaiming (no SOTA, no 'significantly' without test)"
264	
265	  sec_limitations:
266	    label: "Limitations"
267	    word_budget: 250
268	    dependencies: [sec_experiments]
269	    page_count: false  # doesn't count toward 8-page limit
270	    key_elements:
271	      - "Single model family for ctrl-contam (Qwen2.5-7B); multi-family planned"
272	      - "IRT parameters from PSN-IRT (not self-calibrated); dependency on external calibration"
273	      - "SFT-only contamination; post-RL (exp-post-rl) deferred"
274	      - "Power limited by benchmark size (ARC-C 295 items → d=0.45)"
275	      - "Universal misfit means absolute lz* thresholds not applicable → requires Δlz* design"
276	      - "MML-EM refit failure → large-scale audit requires neural IRT advances"
277	
278	# ============================================================
279	# VISUALIZATION PLAN
280	# ============================================================
281	visualization_plan:
282	  - fig_id: fig_1_response_pattern
283	    tool: matplotlib
284	    type: conceptual_illustration
285	    description: "Dual-panel motivation figure showing contaminated vs clean response patterns"
286	    placement: "Section 1 (Introduction) or top of Section 3 (Method)"
287	    aspect_ratio: "2:1 (wide, two-column)"
288	    data_source: "synthetic: 4PL model simulation using PSN-IRT MMLU parameters"
289	    narrative_intent: >
290	      Show the psychometric intuition: a contaminated LLM produces an "impossible" response pattern —
291	      answering hard items correctly (memorized from training) while missing easier items it should get right.
292	      This is exactly what person-fit statistics detect: aberrance relative to IRT model predictions.
293	      The figure should make an ML reviewer immediately understand why psychometric cheating detection applies.
294	    design_notes: >
295	      Two panels side by side. X-axis: items sorted by difficulty (b parameter, easy→hard).
296	      Y-axis: response (0/1). Left panel: "Clean Model" — responses follow expected ICC curve
297	      (probability decreasing with difficulty). Right panel: "Contaminated Model" — same ability level
298	      but some hard items answered correctly (highlighted in red), producing an aberrant pattern.
299	      Overlay the expected probability curve (ICC) as a smooth line. Mark the memorized items distinctly.
300	      Bottom annotation: lz* values for each pattern (clean ≈ 0, contaminated << 0).
301	      Color: blue=clean, red=contaminated/memorized. Style: academic, minimal, no clutter.
302	      Pattern: "dual-panel contrast" from distilled-writing skill.
303	
304	  - fig_id: fig_2_power_function
305	    tool: matplotlib
306	    type: line_plot
307	    description: "Detection power as function of contamination level across 5 benchmarks with theoretical overlay"
308	    placement: "Section 5.2 (Simulation Validation)"
309	    aspect_ratio: "4:3 (single column)"
310	    data_source: "registry: exp-extended-sim (two_sided_power), exp-power-theory (theoretical curve)"
311	    narrative_intent: >
312	      Demonstrate that detection power is predictable from benchmark properties. The theoretical curve
313	      (R²=0.957) means practitioners can determine detection feasibility for ANY benchmark by knowing
314	      only its size. Two-sided detection eliminates the inverted-U artifact. MMLU (14K items) achieves
315	      >93% power at all contamination levels; smaller benchmarks need higher contamination for reliable detection.
316	    design_notes: >
317	      X-axis: contamination level (0-100%). Y-axis: two-sided detection power (0-1).
318	      5 lines for 5 benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval), differentiated by
319	      color + marker. Theoretical √n curve as dashed overlay for MMLU. Horizontal dashed line at 0.80
320	      power threshold. Legend with benchmark names + n_items count.
321	      Key data points to highlight: MMLU@15%=97.8%, ARC-C shows lowest power (n=295).
322	      Style: clean line plot, no excessive gridlines. 95% CI bands if available from simulation.
323	      Pattern: "scaling curve with threshold" from standard ML plots.
324	
325	  - fig_id: fig_3_ctrl_contam
326	    tool: matplotlib
327	    type: multi_panel
328	    description: "Controlled contamination results: θ-free vs θ-fixed Δlz* and seen/unseen split"
329	    placement: "Section 5.3 (Controlled Contamination)"
330	    aspect_ratio: "2:1 (wide, two-column)"
331	    data_source: "registry: exp-ctrl-contam-pilot (metrics.H2, metrics.H3, metrics.theta_fixed_analysis, metrics.accuracy)"
332	    narrative_intent: >
333	      Three key messages: (1) contamination at 15% produces strong detection signal (|d|=3.58);
334	      (2) θ-shift confound causes non-monotonic dose-response under free-θ, but θ-fixed restores
335	      monotonicity — this is a methodological contribution; (3) seen/unseen split reveals the clearest
336	      contamination fingerprint: memorized items produce "normal" lz* while unseen items show extreme
337	      aberrance.
338	    design_notes: >
339	      3 panels (a,b,c). (a) Bar chart: Δlz* for 4 conditions (clean_s1, clean_s2, contam_15, contam_50)
340	      under free-θ (dark bars) vs fixed-θ (light bars). Error bars from clean baseline variance.
341	      Highlight the non-monotonic→monotonic transition. (b) Grouped bars: seen vs unseen lz* for contam_15
342	      and contam_50. Seen lz*≈0 (memorized items look normal) vs unseen lz*=3.1 (genuine aberrance).
343	      (c) θ-shift visualization: θ values across conditions showing contamination→θ↑.
344	      Colors: blue=clean, orange=contam_15, red=contam_50. Consistent across panels.
345	      Annotate Cohen's d values. Pattern: "condition comparison with mechanism decomposition."
346	
347	  - fig_id: fig_4_model_heatmap
348	    tool: matplotlib
349	    type: heatmap
350	    description: "12-model × 5-benchmark lz* heatmap with Ward clustering dendrogram"
351	    placement: "Section 5.4 (Empirical Findings)"
352	    aspect_ratio: "3:4 (portrait, single column)"
353	    data_source: "registry: phase_b_personfit, exp-cross-benchmark-analysis, exp-fdr-correction"
354	    narrative_intent: >
355	      Show the landscape of LLM response pattern anomalies: (1) universal misfit — nearly all cells
356	      colored (57/60 flagged), establishing that LLM responses fundamentally differ from classical
357	      test-takers; (2) heterogeneous profiles — some models show uniform positive lz* (over-consistent,
358	      possible contamination), others show mixed or negative patterns; (3) Ward clustering reveals
359	      contamination typologies (Gemini-1.5 isolated as extreme outlier).
360	    design_notes: >
361	      Heatmap with diverging colormap (blue=negative lz*, white=0, red=positive lz*).
362	      Rows: 12 models, ordered by Ward clustering with dendrogram on left.
363	      Columns: 5 benchmarks (MMLU, HellaSwag, GSM8K, ARC-C, HumanEval).
364	      Cell annotations: lz* values (rounded to integer for readability).
365	      Mark 3 unflagged cells with hatching or border.
366	      Gemini-1.5 MMLU cell should be maximally red (lz*=+34.75).
367	      Colorbar with symmetric range. Model names on right y-axis.
368	      Pattern: "annotated heatmap with hierarchical clustering."
369	
370	# ============================================================
371	# TABLE PLAN
372	# ============================================================
373	table_plan:
374	  - table_id: tab_1_detection_frontier
375	    type: comparison
376	    placement: "Section 2.2 (Background)"
377	    columns: [Method, "Info Required", "Post-RL Robust", "Per-Model", "Training-Free"]
378	    data_source: "paper_framing.md (method landscape), literature_map.yaml"
379	    description: >
380	      Detection frontier ranking all methods by information access level.
381	      Rows: n-gram overlap, Min-K%/MIA, Time Travel, ConStat, CoDeC, Self-Critique, accuracy z-score, IRT-FIT (ours).
382	      Shows IRT-FIT requires minimum information (binary patterns only) while being
383	      structurally RL-robust (binary patterns invariant to token distributional shifts).
384	      Checkmarks/crosses for properties. IRT-FIT row highlighted.
385	
386	  - table_id: tab_2_simulation_power
387	    type: results
388	    placement: "Section 5.2 (Simulation)"
389	    columns: [Benchmark, n_items, "Power@5%", "Power@15%", "Power@25%", "Power@50%", "Power@100%"]
390	    data_source: "registry: exp-extended-sim (two_sided_power)"
391	    description: >
392	      Two-sided detection power across 5 benchmarks and key contamination levels.
393	      Bold best per column. Shows power scales with benchmark size.
394	      Bottom row: theoretical prediction from power function.
395	      Include 95% CI from simulation (our differentiator vs peers who report no variance).
396	
397	  - table_id: tab_3_ctrl_contam
398	    type: results
399	    placement: "Section 5.3 (Controlled Contamination)"
400	    columns: [Condition, Accuracy, "θ_MLE", "lz*(free-θ)", "lz*(fixed-θ)", "Δlz*(free)", "Δlz*(fixed)", "Cohen's d"]
401	    data_source: "registry: exp-ctrl-contam-pilot (metrics)"
402	    description: >
403	      Controlled contamination summary. 4 rows: clean_s1, clean_s2, contam_15, contam_50.
404	      Shows accuracy improvement, θ-shift, lz* under both estimation strategies,
405	      Δlz* relative to clean baseline, and effect sizes.
406	      Highlight: contam_15 |d|=3.58, θ-fixed ratio=2.93.
407	
408	  - table_id: tab_a1_full_lz_profiles
409	    type: appendix
410	    placement: "Appendix"
411	    columns: [Model, MMLU, HellaSwag, GSM8K, ARC-C, HumanEval, "Flagged/5"]
412	    data_source: "registry: phase_b_personfit, exp-fdr-correction"
413	    description: "Full 12-model lz* values with BH-FDR corrected flagging indicators."
414	
415	  - table_id: tab_a2_ml_classifier
416	    type: appendix
417	    placement: "Appendix"
418	    columns: [Method, "AUROC@5%", "AUROC@10%", "AUROC@25%", "AUROC@50%", "Training Data"]
419	    data_source: "registry: exp-ml-classifier-baseline"
420	    description: "ML classifier baseline comparison: lz* vs LR/RF at different contamination levels."
421	
422	  - table_id: tab_a3_4pl_ablation
423	    type: appendix
424	    placement: "Appendix"
425	    columns: [Benchmark, "4PL Power", "3PL Power", "Δ Power", "4PL FAR", "3PL FAR"]
426	    data_source: "registry: exp-4pl-ablation"
427	    description: "4PL vs 3PL(d=1) detection power and false alarm rate comparison at 25% contamination."
428	
429	  - table_id: tab_a4_irt_refit
430	    type: appendix
431	    placement: "Appendix"
432	    columns: [Method, N_models, "a_r (Pearson)", "b_r (Pearson)", Notes]
433	    data_source: "registry: exp-v1-irt-refit-pilot, exp-v1-irt-refit-expanded"
434	    description: "MML-EM IRT refit results from v1 leaderboard data. Documents estimation failure (a_r=0.13)."
435	
436	# ============================================================
437	# LITERATURE STRATEGY
438	# ============================================================
439	literature_strategy:
440	  total_target: 30-35
441	  current_count: 10
442	  current_verified: 0
443	
444	  micro_clusters:
445	    - cluster_name: irt-foundations
446	      target_count: 5
447	      current_verified: 0
448	      search_queries:
449	        - "item response theory textbook Lord Novick"
450	        - "four-parameter logistic model IRT"
451	        - "IRT model comparison 2PL 3PL 4PL"
452	      must_cite:
453	        - "Lord 1980 (Applications of IRT)"
454	        - "Embretson & Reise 2000 (Item Response Theory for Psychologists)"
455	        - "Barton & Lord 1981 (4PL model)"
456	
457	    - cluster_name: person-fit
458	      target_count: 6
459	      current_verified: 0
460	      current_in_map: 3  # sinharay2017, karabatsos2003, hong2021lzm
461	      search_queries:
462	        - "person-fit statistics lz lz* Drasgow"
463	        - "Snijders 2001 person-fit correction"
464	        - "appropriateness measurement person-fit IRT"
465	        - "item preknowledge detection person-fit cheating"
466	      must_cite:
467	        - "Drasgow et al. 1985 (original lz statistic - Appropriateness Measurement)"
468	        - "Snijders 2001 (lz* correction - Asymptotic Distribution)"
469	        - "Meijer & Sijtsma 2001 (person-fit review)"
470	
471	    - cluster_name: contamination-detection
472	      target_count: 10
473	      current_verified: 0
474	      current_in_map: 3  # constat2024, minkprob2024, codec2026
475	      search_queries:
476	        - "benchmark contamination detection LLM"
477	        - "data contamination large language models"
478	        - "membership inference attack language model"
479	        - "Time Travel probing benchmark contamination"
480	        - "n-gram overlap contamination GPT"
481	      must_cite:
482	        - "Oren et al. 2024 (Time Travel Probing - ICLR 2024 Spotlight)"
483	        - "Golchin & Surdeanu 2024 (Time Travel original)"
484	        - "Dodge et al. 2021 (C4 documentation, training data contamination)"
485	        - "Jacovi et al. 2023 or similar contamination survey"
486	        - "Sainz et al. 2023 (NLP evaluation contamination survey)"
487	
488	    - cluster_name: irt-llm
489	      target_count: 4
490	      current_verified: 0
491	      current_in_map: 2  # psnirt2026, atlas2025
492	      search_queries:
493	        - "item response theory large language model evaluation"
494	        - "IRT LLM benchmark psychometric"
495	        - "computerized adaptive testing LLM"
496	      must_cite:
497	        - "PSN-IRT (AAAI 2026 Oral) - already in map"
498	        - "ATLAS (adaptive testing LLM) - already in map"
499	
500	    - cluster_name: post-rl-contamination
501	      target_count: 3
502	      current_verified: 0
503	      current_in_map: 2  # wang2025fragility, selfcritique2026
504	      search_queries:
505	        - "reinforcement learning contamination detection failure"
506	        - "post-training contamination reasoning models"
507	      must_cite:
508	        - "Wang et al. 2025 (fragility of contamination detection) - already in map"
509	
510	    - cluster_name: llm-evaluation-infrastructure
511	      target_count: 5
512	      current_verified: 0
513	      current_in_map: 0
514	      search_queries:
515	        - "open LLM leaderboard HuggingFace"
516	        - "LLM evaluation benchmark survey"
517	        - "MMLU benchmark Hendrycks"
518	        - "language model evaluation harness"
519	      must_cite:
520	        - "Hendrycks et al. 2021 (MMLU)"
521	        - "Beeching et al. 2023 (Open LLM Leaderboard)"
522	        - "Gao et al. 2024 (lm-evaluation-harness)"
523	
524	# ============================================================
525	# WRITING ORDER
526	# ============================================================
527	writing_order:
528	  - section: sec_setup
529	    rationale: "Setup first — establishes data, models, evaluation protocol for all subsequent sections"
530	  - section: sec_simulation
531	    rationale: "Simulation validates theoretical framework before real experiments"
532	  - section: sec_ctrl_contam
533	    rationale: "Controlled contamination is primary validation (ground truth)"
534	  - section: sec_empirical
535	    rationale: "Empirical findings build on ctrl-contam methodology"
536	  - section: sec_method
537	    rationale: "Method section after experiments — can precisely scope to what was validated"
538	  - section: sec_background
539	    rationale: "Background after method — knows exactly what IRT concepts need exposition"
540	  - section: sec_introduction
541	    rationale: "Introduction after all content — can accurately preview results"
542	  - section: sec_discussion
543	    rationale: "Discussion synthesizes all findings"
544	  - section: sec_limitations
545	    rationale: "Limitations after discussion"
546	  - section: sec_conclusion
547	    rationale: "Conclusion last"
548	  - section: abstract
549	    rationale: "Abstract written last — must accurately reflect final content"
550	
551	# ============================================================
552	# APPENDIX PLAN
553	# ============================================================
554	appendix_plan:
555	  - id: app_simulation_details
556	    label: "Simulation Details"
557	    content: "Full simulation parameters, null check results (KS statistics), extended power tables"
558	    data_source: "registry: sim_001, exp-extended-sim"
559	
560	  - id: app_4pl_ablation
561	    label: "4PL vs 3PL Ablation"
562	    content: "Full benchmark-level power comparison + FAR analysis + real-data degradation analysis"
563	    data_source: "registry: exp-4pl-ablation, exp-4pl-real-data-degradation"
564	    figures: [fig_a1_4pl_ablation]
565	
566	  - id: app_ml_classifier
567	    label: "ML Classifier Baseline"
568	    content: "Full AUROC comparison across contamination levels, feature ablation"
569	    data_source: "registry: exp-ml-classifier-baseline"
570	
571	  - id: app_empirical_null
572	    label: "Bootstrap Null Calibration"
573	    content: "Per-benchmark null bias, std, KS statistics; QQ plots"
574	    data_source: "registry: exp-empirical-null"
575	    figures: [fig_a2_bootstrap_null]
576	
577	  - id: app_domain_analysis
578	    label: "Domain-Level Analysis"
579	    content: "MMLU subject-level lz* for flagged models (Gemini-1.5, Yi-Lightning, etc.)"
580	    data_source: "registry: exp-domain-analysis"
581	
582	  - id: app_irt_refit
583	    label: "Classical IRT Refit"
584	    content: "v1 leaderboard MML-EM refit methodology + failure analysis"
585	    data_source: "registry: exp-v1-irt-refit-pilot, exp-v1-irt-refit-expanded"
586	
587	  - id: app_natural_experiment
588	    label: "Base-Chat Natural Experiment"
589	    content: "SFT effects on lz* across base-chat model pairs"
590	    data_source: "registry: exp-natural-experiment"
591	
592	  - id: app_ctrl_contam_details
593	    label: "Controlled Contamination Details"
594	    content: "Training configuration, per-subject analysis, full accuracy tables, clean_s3 results"
595	    data_source: "registry: exp-ctrl-contam-pilot, exp-ctrl-contam-pilot-clean-s3"
596	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2ee86377-a315-4aec-b340-c82f6583131e",
  "isSidechain": true,
  "promptId": "5a905e93-7981-422f-9766-0fbbede8e369",
  "agentId": "a30c0bb91d2c09315",
  "type": "user",
  "uuid": "644c7e9d-6ba6-408e-86ca-db15c338c27f",
  "sourceToolAssistantUUID": "2ee86377-a315-4aec-b340-c82f6583131e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T23:15:43.312Z_

<details><summary>↩ Tool result · `toolu_01Cga1Fhgd7J2UBVhb53aPvc`</summary>

```text
1	# Memory — irt_personfit_contam
2	
3	## OOM 教训 (2026-05-20)
4	- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM
5	- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）
6	- generate_response 和 compute_lz_star 都需要分批
7	
8	## Worker context exhaustion 教训 (2026-05-20)
9	- exp-v1-irt-refit-expanded Worker 跑 1.5 小时后崩溃，无输出。任务是从 HuggingFace 下载 500+ 模型的 per-item 数据并拟合 IRT。
10	- **根因**: 大量 HF API 调用 + 数据处理的累积输出耗尽 Worker context window。
11	- **教训**: 涉及大规模数据下载（100+ datasets）的任务必须分批 + checkpoint 中间结果，或拆成多个 Worker 串行执行。单个 Worker 不适合做 1.5hr+ 的重型数据工程。
12	- **补充 (同日)**: ssh_read_only 读取大 JSON 文件（8MB+ 单行）也会撑爆 context。Worker 操作远程大文件必须用 python 脚本提取摘要，不要 cat/head。
13	- **补充 (同日)**: Worker 无法在进程内长时间等待（~2 min 就退出）。涉及 GPU 训练 + eval 的任务应分阶段处理：训练完成后由 cron 回调触发 eval Worker，或由主 Agent 定时派 Worker 检查。
14	
15	## sim_001 关键发现 (2026-05-20)
16	- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)
17	  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01
18	  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）
19	- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%
20	- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）
21	
22	## PSN-IRT 12 模型身份 (2026-05-20)
23	
24	**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`
25	
26	| student_id | θ | 正确率 | 模型名称 | 类型 |
27	|---|---|---|---|---|
28	| 0 | 1.46 | 80.6% | 360GPT2-Pro | API |
29	| 1 | 3.77 | 85.7% | DeepSeek-V3 | API |
30	| 2 | 1.14 | 78.9% | Doubao-pro | API |
31	| 3 | 0.78 | 84.5% | Gemini-1.5 | API |
32	| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源 2B |
33	| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API |
34	| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源 7B |
35	| 7 | 0.93 | 77.0% | Moonshot-v1 | API |
36	| 8 | 0.96 | 76.3% | Qwen-Plus | API |
37	| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct | 开源 3B |
38	| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 | 开源 7B |
39	| 11 | 0.77 | 75.2% | Yi-Lightning | API |
40	
41	## Gemini-1.5 × 100% contamination 精确匹配 (2026-05-20)
42	
43	Gemini-1.5 MMLU lz*(benchmark-specific θ) = +31.815 = 100% contamination simulation lz* = +31.815（完全一致）。机制：100% accuracy → θ_bench=4.0 → lz* deterministic。其他 benchmark Gemini-1.5 lz* 为负（非 100% acc），说明异常是 benchmark-specific 的。
44	
45	## exp-extended-sim 关键发现 (2026-05-20)
46	
47	- Dual-regime crossover 75-90%：所有 5 benchmark 在此区间 lz* 从负翻正
48	- 100% contamination lz* deterministic (std=0.0)
49	- Inverted-U 全 5 benchmark 确认
50	
51	## exp-two-sided 关键教训 (2026-05-20)
52	
53	95% flagging 即使用 benchmark-specific θ + bootstrap + FDR 也无法降低。LLM 系统性违反 4PL 假设（单维+局部独立）。绝对阈值对 real data 无意义，需 controlled calibration (Δlz*)。
54	
55	## exp-empirical-null 关键发现 (2026-05-20)
56	
57	Bootstrap null 校准良好（mean bias=0.09, std=1.002）。95% flagging 不是 null miscalibration，而是 LLM response pattern 产生极端 lz*。大 benchmark KS reject 仅 8.3%，小 benchmark 58-75%（有限样本效应）。
58	
59	## exp-power-theory 关键发现 (2026-05-20)
60	
61	R²(two-sided)=0.957, R²(left-tail)=0.976, R²(mean lz*)=0.995。δ ∝ √n confirmed。Inverted-U 拐点理论值 π*≈81-85%。最小 n_items (80% power): 15% contam→~8K, 25%→~3K, 50%→~1K。
62	
63	## exp-item-alignment-check 关键发现 (2026-05-20)
64	
65	**PSN-IRT 与 v1 Leaderboard item ordering 不对齐。** 直接位置匹配率 54.56%（≈随机）。Content-based 重排后 Mistral 88.46%, Vicuna 72.48%。
66	
67	**根因**: PSN-IRT 保持 raw MMLU 原始顺序，v1 leaderboard 在 subject 内部 shuffle。且 PSN-IRT 是独立评测（不同 prompt/few-shot），即使对齐后仍有 ~12% response 差异。
68	
69	**结论**: **不可混用 v1 responses + PSN-IRT parameters**。~12% 噪声对 item-level person-fit 统计量影响严重。
70	
71	**已生成 item_mapping.csv**: 12068/14042 items 的 v1→PSN-IRT 位置映射，可用于未来 content-based 对齐需求。
72	
73	## Open LLM Leaderboard v1 per-item data (2026-05-20)
74	
75	**来源**: `open-llm-leaderboard-old/details_{org}__{model}` HuggingFace datasets
76	**格式**: Parquet, `acc`/`acc_norm` 二值字段
77	**覆盖**: MMLU ✅, HellaSwag ✅, ARC-C ✅, GSM8K ✅ | HumanEval ❌
78	**模型数**: 13,000+
79	**⚠️ 不可直接用 PSN-IRT parameters** — 见 item-alignment-check 发现
80	
81	## exp-fdr-correction 关键发现 (2026-05-20)
82	
83	exp-two-sided v2 的 `empirical_pvalues.csv` 已包含 global BH-FDR 校正（60 cells 一起做 BH）。校正前后 flagging 均为 57/60 (95%)——因大多数 cells empirical p=0.000，BH 校正无实质影响。Leaderboard-scale FDR (24800+ tests) 需在 leaderboard audit 中单独处理。
84	
85	## exp-clean-control-delta 关键发现 (2026-05-20)
86	
87	Clean-vs-clean Δlz* 均值全部接近 0（|mean| < 0.13），无一显著，确认 estimation noise floor ~ N(0, 1.4)。
88	Clean-vs-contaminated (25%) Δlz* 均高度显著（p<1e-10），Cohen's d: MMLU=2.66, HellaSwag=1.85, GSM8K=1.85, HumanEval=1.07, ARC-C=0.45。
89	ARC-C d=0.45 略低 0.5 阈值（仅 295 items），与 power theory 一致。
90	论文中标注为 "theoretical noise floor"，真实 SFT clean-vs-clean 在 ctrl-contam-pilot 中实现。
91	
92	## exp-ml-classifier-baseline 关键发现 (2026-05-20)
93	
94	**lz* 在低污染率 (5-10%) 优于有监督 ML 分类器**：5% contam lz* AUROC 0.675 vs best ML 0.575 (+0.10); 10% contam 0.763 vs 0.712 (+0.05)。ML 仅在 25%+ 污染时略胜 (+0.05)，但需 oracle contamination labels（实际不可用）。
95	RF feature importance 在 items 间高度弥散（top item <1%），与 lz* 全局 likelihood 方法一致。
96	论文限定为 simulation 场景下的对比，不推广为"所有 binary-only ML 方法都不如 IRT"。
97	
98	## exp-domain-analysis 关键发现 (2026-05-20)
99	
100	**Gemini-1.5 MMLU 100% accuracy 覆盖全部 57 个 subject**——不是 domain-concentrated 泄漏，是完全数据集泄漏。50/57 subjects flagged (lz*>1.96)，未 flagged 的 7 个 subject 的 lz* 也很高但 item 数太少。
101	
102	**模型 contamination 指纹多样**：
103	- Doubao-pro: 反向 pattern，Humanities/Social Sciences lz* 极负（-13~-15），STEM 接近 0，Other 正向——可能是训练数据偏科
104	- Hunyuan-Turbo: STEM lz*=1.8 vs Social Sciences lz*=13.9——Social Sciences 方向过度拟合
105	- Yi-Lightning 和 Qwen-Plus: 全 domain 高 lz*（16~28），领先所有其他模型
106	
107	**论文价值**: domain decomposition 为 12-model case study 增加定性分析深度，但 non-essential（P2 级别）。
108	
109	**virology lz*=-8.21 诊断**：双重根因——(1) global θ=0.78 vs MMLU θ_MLE=4.0 错配；(2) virology 全部 166 items d<1.0 (mean=0.71)，即使 θ=4.0 仍有 58/166 items P<0.5。是 PSN-IRT calibration artifact，不影响 overall lz*=34.75。per-subject 分析需加 caveat。
110	
111	## exp-natural-experiment 关键发现 (2026-05-20)
112	
113	21 对 base→chat 模型 × 4 benchmarks（MMLU/HellaSwag/ARC-C/GSM8K）。
114	
115	**两个 benchmark 有显著系统性 SFT 效应**：
116	- HellaSwag: Δlz* 偏差 mean=-3.40, t=-3.97, p=0.001（SFT 系统性降低 person-fit）
117	- GSM8K: Δlz* 偏差 mean=+3.92, t=3.35, p=0.009（SFT 系统性提高 person-fit）
118	- MMLU/ARC-C 无显著效应
119	
120	**无个体 pair outlier**——未能检测到单个模型的 benchmark-specific contamination。
121	**Director 评估价值极低（P2-optional）**，不作为核心 evidence 使用。
122	
123	## exp-4pl-ablation 关键发现 (2026-05-20)
124	
125	**4PL d 参数对检测力的影响是决定性的，不是锦上添花。**
126	
127	核心数据（4PL vs 3PL(d=1)，平均 power gain across contamination levels）：
128	- MMLU: +27.3pp (max +49.0pp)
129	- HellaSwag: +26.1pp (max +59.6pp)
130	- GSM8K: +20.3pp (max +39.7pp)
131	- ARC_C: +14.8pp (max +54.6pp)
132	- HumanEval: +13.7pp (max +30.6pp)
133	
134	FAR 校准：4PL ≈ 5%（正确），3PL 4.7-16.5%（偏高），2PL 50-100%（完全不可用——固定 c=0.25 灾难性错误）。
135	
136	**d-bucket 机制确认**：d<0.8 的 items 上 4PL 优势最大（MMLU +61pp），d≥0.95 时差异可忽略。这证实 d 参数捕捉 ceiling effect 是检测力提升的关键来源。
137	
138	**论文价值**：回应 Reviewer R8 concern（为什么用 4PL 而非 3PL）。46% MMLU items d<0.95，忽略 d 约将检测力减半。这是 Method 部分的核心 justification。
139	
140	## exp-4pl-real-data-degradation 关键发现 (2026-05-20)
141	
142	**实数据验证：d 参数的影响对高能力模型是毁灭性的。**
143	
144	在 12 个 PSN-IRT 模型的真实响应数据上，4PL vs 3PL(d=1) 的 lz* 仅有 r=0.225, RMSE=68.41——几乎无关联。
145	
146	**不对称影响机制**：d=1 使 P(θ)→1（高能力模型预期全部答对），导致少量错误被 lz* 放大为极端异常值。低能力模型的 P(θ) 本身就远离 1.0，d=1 vs d<1 差异小，因此几乎不受影响。
147	
148	- DeepSeek-V3 (θ=3.77): MMLU lz* 从 +16.4 暴跌至 -340.6
149	- Gemma-2B-it / Vicuna / Mistral (低 θ): |Δlz*|<2
150	- MMLU 最严重（46% items d<0.95），mean |Δlz*|=58.3
151	
152	**与 exp-4pl-ablation 的互补**：ablation 在模拟数据上证明 power 损失，本实验在实数据上证明 lz* 值本身被完全摧毁。二者形成 R8 的双重证据链——4PL d 参数不可或缺。
153	
154	**论文写作注意**：这个结果特别适合做 case study 可视化（选 DeepSeek-V3 on MMLU 作为 extreme case），放在 ablation study 或 appendix 中。
155	
156	## exp-ctrl-contam-pilot 关键发现 (2026-05-20)
157	
158	**首次真实 LLM controlled contamination 实验。** Qwen2.5-7B-Instruct QLoRA SFT，4+1 条件。
159	
160	**核心结果（n=3 clean seeds, ddof=1）**：
161	| Condition | Accuracy | θ_MLE | lz* |
162	|-----------|----------|-------|-----|
163	| clean_s1 (seed=42) | 0.6787 | -0.0987 | 8.0101 |
164	| clean_s2 (seed=123) | 0.6789 | -0.0842 | 5.9440 |
165	| clean_s3 (seed=456) | 0.6783 | -0.1068 | 8.0806 |
166	| contam_15 | 0.7310 | +0.1971 | 3.0046 |
167	| contam_50 | 0.7644 | +0.3703 | 5.4480 |
168	
169	**Baseline（n=3）**: mean=7.3449, std=1.2137
170	**Cohen's d（n=3, ddof=1）**: contam_15 d=-3.58, contam_50 d=-1.56
171	**注意**：之前汇报的 d=-3.85 / d=-1.48 使用了 ddof=0。论文统一用 ddof=1。
172	
173	**H1 ✓ H2 ✓ H3 ✗(θ-free) H4 ✗**
174	
175	**θ-shift 是 dose-response 倒置的确切原因**：
176	- contamination 抬高 θ_MLE（clean -0.09 → contam_50 +0.37），MLE 将 contamination 信号解释为 "能力提升"
177	- θ-fixed（固定为 clean θ 均值 -0.0914）下，dose-response 恢复单调：
178	  - |Δlz*_fixed_15| = 2.96, |Δlz*_fixed_50| = 8.67, ratio = 2.93 ✅
179	- θ-shift 分别吸收了 contam_15 的 6.93 和 contam_50 的 10.20 lz* 单位信号
180	
181	**clean seed 变异性**：s1 和 s3 的 lz* 接近（8.01, 8.08），s2 明显低（5.94）。n=3 baseline std=1.21 vs n=2 的 1.46，加入 s3 压缩了方差，使 Cohen's d 更极端。
182	
183	**Memorization fraction 低于预期**（0.38/0.29 vs 假设的 >0.5）——QLoRA 3 epochs 不足以产生强 memorization，但足以产生可检测的 lz* 偏移。
184	
185	**论文叙事价值**：
186	1. θ-shift = "ability inflation" 是 contamination 逃避 person-fit 检测的核心机制
187	2. 与 simulation inverted-U 发现形成呼应——real-world 版本的同一现象
188	3. θ-fixed 分析作为 supplementary evidence 证明底层信号单调递增
189	4. 支撑 Discussion 中 "θ estimation as confound" 段落
190	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdf38faf-024d-4d30-b344-a4d97ad557b1",
  "isSidechain": true,
  "promptId": "5a905e93-7981-422f-9766-0fbbede8e369",
  "agentId": "a30c0bb91d2c09315",
  "type": "user",
  "uuid": "3064f7b9-9667-43b1-925a-95e23e668078",
  "sourceToolAssistantUUID": "bdf38faf-024d-4d30-b344-a4d97ad557b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T23:15:43.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_014TxcM9MXqcy2gTQ79T3tF1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3064f7b9-9667-43b1-925a-95e23e668078",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfvJAomTMUQL51UyFmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "43d38994-79d7-4cf8-be0d-55a817e0f53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CjP4h3ZUy9VgqV2kK6aCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 25392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T23:15:43.764Z_

<details><summary>↩ Tool result · `toolu_014TxcM9MXqcy2gTQ79T3tF1`</summary>

```text
1	% introduction
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43d38994-79d7-4cf8-be0d-55a817e0f53b",
  "isSidechain": true,
  "promptId": "5a905e93-7981-422f-9766-0fbbede8e369",
  "agentId": "a30c0bb91d2c09315",
  "type": "user",
  "uuid": "d180eaa4-7d73-4256-adf1-0c63b6390e0a",
  "sourceToolAssistantUUID": "43d38994-79d7-4cf8-be0d-55a817e0f53b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T23:15:44.010Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FqgJ2XZdFYoo2ZqgCiVDcR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/docs/IDEA_BRIEF.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d180eaa4-7d73-4256-adf1-0c63b6390e0a",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfvJAomTMUQL51UyFmx",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "30e17fe8-5bbc-454d-9194-a5e652d5f126",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017CjP4h3ZUy9VgqV2kK6aCT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4988,
      "cache_read_input_tokens": 25392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4988,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T23:15:44.015Z_

<details><summary>↩ Tool result · `toolu_01FqgJ2XZdFYoo2ZqgCiVDcR`</summary>

```text
1	# Idea Brief: IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs
2	
3	
4	- **Idea ID**: `idea_033`
5	- **Created**: 2026-05-20
6	- **Approved**: 2026-05-20
7	- **Source**: foreign:be-idea-gen-0515-4
8	- **Level**: solid
9	- **Target Venues**: AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026) — primary target: PSN-IRT was AAAI 2026 Oral, strong psychometrics+AI audience, 10 weeks from today is feasible with focused scope on 6 benchmarks, ICLR 2027 (abstract: ~Sep 19, 2026; full paper: ~Sep 24, 2026) — backup allowing fullest experimental scope including post-RL hypothesis test and expanded baseline comparisons
10	
11	## Seed Topic
12	
13	web_research
14	
15	## Core Problem
16	
17	Can we detect benchmark contamination in LLMs without any access to training data or model internals, using only the pattern of correct/incorrect responses across benchmark items? Specifically, can psychometric person-fit statistics identify the 'sweet spot' of partial contamination (5-30% of items) where scores are meaningfully inflated but existing detectors fail?
18	
19	## Opportunity / Why Now
20	
21	All existing contamination detection methods require either training data access (n-gram overlap), model internals (Min-K% Probability, MIA, Self-Critique entropy sequences), or special probing prompts (Time Travel). Yet psychometrics has long used person-fit statistics like lz* to detect cheating examinees from response patterns alone — a contaminated LLM is functionally analogous to a test-taker with item preknowledge. This cross-domain transfer is newly feasible because IRT infrastructure for LLM evaluation has matured: PSN-IRT (AAAI 2026 Oral) calibrates 4PL item parameters (a, b, c, d) across 11 benchmarks and 41,871 items, providing the calibrated item bank needed to compute person-fit statistics at scale. The 4PL feasibility parameter d is particularly relevant — it accounts for item ambiguity that could otherwise be confused with contamination-induced aberrance, reducing false alarms. Meanwhile, Wang et al. (2025) demonstrate that all existing MIA-based detectors are fragile under reasoning-model contamination where RL post-training conceals SFT contamination signals, creating urgent demand for detection methods operating at a different level of abstraction.
22	
23	## Landscape (SOTA & Limitations)
24	
25	Contamination detection circa 2026 relies on five established families: (1) time-based partition, (2) Min-K%/Min-K%++ membership inference (ICLR 2024), (3) Time Travel probing (ICLR 2024 Spotlight), (4) ConStat performance-based testing (NeurIPS 2024), and (5) canary GUIDs. Newer approaches include CoDeC (ICLR 2026), which measures in-context learning effects on memorized vs. unseen data; Cross-Context Verification (arXiv 2603.21454), which uses session-isolated solution diversity; Self-Critique (arXiv 2510.09259, ICLR 2026), which detects post-RL contamination via policy collapse in entropy sequences with ~30% AUC improvement over baselines that perform near chance on RL-contaminated data; and Silicon Bureaucracy (arXiv 2603.21636), which audits score credibility through perturbation sensitivity analysis. Critically, Wang et al. (arXiv 2025) show all MIA-based methods fail under reasoning-model contamination where RL conceals SFT signals. On the IRT side, PSN-IRT (AAAI 2026 Oral) calibrates 4PL parameters (discrimination a, difficulty b, guessing c, feasibility d) across 11 benchmarks and 41,871 items but uses them for measurement quality, not contamination. ATLAS (arXiv 2025) uses IRT for adaptive testing efficiency. Han et al. (EACL 2026 Findings) quantify contamination in psychometric personality inventories but do not employ person-fit statistics. PaCoST (EMNLP 2024 Findings) uses paired confidence for contamination but is not IRT-based. In educational testing, lz* and outfit/infit statistics reliably flag cheating with known Type-I error control, with peak detection power at 10-30% item preknowledge (Sinharay, 2017; Karabatsos, 2003). No published or concurrent work connects IRT person-fit statistics to LLM benchmark contamination detection — an extensive search of arXiv 2025-2026, OpenReview, and GitHub confirms this gap remains open.
26	
27	## Proposed Approach
28	
29	We compute four IRT person-fit statistics — lz, lz*, outfit, and infit — for each LLM using calibrated 4PL item parameters (a, b, c, d) from PSN-IRT's public release (41,871 items across 11 benchmarks). The analysis proceeds at two levels:
30	
31	**Level 1: Per-benchmark person-fit.** To respect the unidimensionality assumption, we compute person-fit statistics separately within each benchmark. Before fitting, we run an exploratory factor analysis (EFA) screen within each benchmark to validate approximate unidimensionality, following psychometric best practice (Crisan, Tendeiro & Meijer, 2017) and recent LLM evaluation precedent (arXiv:2509.24186). We focus on 6 benchmarks spanning diverse capabilities: MMLU (knowledge), GSM8K (math), HumanEval (coding), ARC-Challenge (science reasoning), HellaSwag (commonsense), and TruthfulQA (factuality).
32	
33	**Level 2: Aggregated contamination score.** We compute the multiscale lzm statistic (Hong, Lin & Cheng, 2021) — the standardized sum of per-benchmark lz* values — providing an overall contamination indicator that respects the multidimensional ability structure.
34	
35	**Controlled contamination experiment.** We establish ground truth by fine-tuning three open-source models (Llama 4 Scout 17B-16E, Qwen 3.5-9B, Gemma 4 31B) on varying fractions of benchmark items. We use seven contamination levels (0%, 5%, 10%, 15%, 25%, 50%, 100%) to map the detection power curve. Fine-tuning uses QLoRA to manage memory costs, particularly for the MoE-architecture Scout (109B total parameters, 17B active). For each contaminated variant, we compare person-fit signatures against clean baselines.
36	
37	**Power analysis and simulation.** We conduct a formal power analysis varying contamination fraction, number of contaminated items, and item difficulty distribution. Based on the educational testing literature, we expect an inverted-U detection power curve: undetectable below ~3% contamination (signal drowned in noise), peak detection at 10-30% (clear item-response aberrance), declining above 50% (inflated ability estimate absorbs contamination), and zero power at 100% (uniform high performance is consistent, not aberrant under IRT). We explicitly characterize this operating range and argue that 5-30% is the most policy-relevant detection window — where contamination meaningfully inflates scores but evades simple methods.
38	
39	**4PL ablation.** We compare person-fit statistics computed under the full 4PL model vs. a 3PL reduction (fixing d=1) to quantify how the feasibility parameter affects contamination detection sensitivity. The 4PL d parameter absorbs some item-level aberrance (Liao et al., 2012), which reduces false alarms from item ambiguity but may also reduce sensitivity to genuine contamination.
40	
41	**Post-RL hypothesis test.** As a key hypothesis (not a claimed advantage), we test whether person-fit statistics maintain detection power on post-RL reasoning models where Wang et al. (2025) showed existing MIA-based detectors fail. We create post-RL variants by applying GRPO fine-tuning after SFT-based contamination on Qwen 3.5-9B, specifically testing whether RL smooths out response-level aberrance or preserves it.
42	
43	**Baselines.** We evaluate detection performance (AUROC, Type-I error at fixed thresholds) against ConStat, PaCoST, CoDeC, Min-K%++, and Self-Critique across all contamination levels and training stages (SFT-only, SFT+RL).
44	
45	**Toolkit.** We release an open-source Python toolkit (built on py-irt and the R mirt package via rpy2, which natively supports 4PL person-fit computation) that takes any binary response matrix and calibrated 4PL item parameters and outputs per-model, per-benchmark contamination flags with calibrated p-values.
46	
47	## Resource Estimate
48	
49	- **auto_research**: {'claude_api_cost': '$400-600', 'estimated_gpu_cost': '$800-1050', 'gpu_hours': '320-420', 'speed_bottleneck': 'Sequential fine-tuning of contaminated model variants (3 base models × 7 contamination levels = 21 fine-tuning runs, plus 3 post-RL GRPO runs). Llama 4 Scout requires 4× H100 for QLoRA due to 109B total MoE parameters in memory; Gemma 4 31B needs 2× H100. Full-benchmark inference for 30+ models is parallelizable but each large model requires multi-GPU inference.', 'timeline': '5-6 weeks'}
50	- **cost_breakdown**: {'fine_tuning': 'Qwen 3.5-9B: ~15 GPU-hrs (7 levels × ~2 hrs); Gemma 4 31B: ~50 GPU-hrs (7 levels × ~7 hrs on 2× H100); Llama 4 Scout: ~70 GPU-hrs (7 levels × ~10 hrs on 4× H100). Post-RL GRPO variants: ~30 GPU-hrs. Total fine-tuning: ~165 GPU-hrs.', 'inference': '30+ models × 6 benchmarks × ~1-3 hrs/model depending on size: ~100-150 GPU-hrs.', 'note': "Costs increased ~50% vs. original estimate due to: (a) 7 contamination levels instead of 4, (b) Gemma 4 31B is 2.5× larger than originally assumed '12B', (c) explicit MoE memory overhead for Scout, (d) added simulation study and post-RL GRPO variants.", 'simulation': 'Power analysis simulation (synthetic response matrices, 1000 replications × 7 contamination levels × 6 benchmarks): ~20 GPU-hrs on CPU/light GPU.'}
51	- **human_in_loop**: {'claude_api_cost': '$200-300', 'estimated_gpu_cost': '$700-875', 'gpu_hours': '280-350', 'timeline': '8-9 weeks'}
52	- **manual**: {'estimated_gpu_cost': '$750-1000 (H100 at ~$2.50/hr)', 'gpu_hours': '300-400', 'timeline': '12 weeks'}
53	
54	## Key References
55	
56	- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory (AAAI 2026 Oral, arXiv 2505.15055) — calibrates 4PL item parameters for 41,871 items across 11 benchmarks
57	- Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks (arXiv 2511.04689) — ATLAS, IRT for adaptive testing efficiency
58	- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)
59	- PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection (EMNLP 2024 Findings)
60	- Detecting Pretraining Data from Large Language Models / Min-K% Probability (ICLR 2024)
61	- Time Travel in LLMs: Tracing Data Contamination in Large Language Models (ICLR 2024 Spotlight)
62	- On The Fragility of Benchmark Contamination Detection in Reasoning Models (arXiv 2510.02386) — Wang et al., shows MIA-based detectors fail under post-RL contamination
63	- Detecting Data Contamination in LLMs via In-Context Learning / CoDeC (ICLR 2026)
64	- Detecting Data Contamination from Reinforcement Learning Post-training / Self-Critique (arXiv 2510.09259, ICLR 2026) — post-RL contamination detection via entropy-sequence policy collapse
65	- Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence (arXiv 2603.21636) — perturbation-based score credibility audit
66	- Quantifying Data Contamination in Psychometric Evaluations of LLMs (EACL 2026 Findings) — Han et al.
67	- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis (arXiv 2603.21454)
68	- Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types (Hong, Lin & Cheng, Psychometrika 2021) — lzm multiscale aggregation
69	- Investigating the Practical Consequences of Model Misfit in Unidimensional IRT Models (Crisan, Tendeiro & Meijer, Applied Psychological Measurement 2017) — effects of unidimensionality violations on person-fit
70	- The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses (Liao et al., 2012) — 4PL absorbs some aberrance via d parameter
71	- Which Statistic Should Be Used to Detect Item Preknowledge? (Sinharay, JEBS 2017) — power analysis for preknowledge detection
72	- Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics (Karabatsos, Applied Measurement in Education 2003)
73	- PerFit: An R Package for Person-Fit Analysis in IRT (Journal of Statistical Software 2016)
74	- py-irt: A Scalable Item Response Theory Library for Python (INFORMS Journal on Computing 2023)
75	- mirt: A Multidimensional Item Response Theory Package for the R Environment (Journal of Statistical Software 2012) — supports 4PL person-fit natively
76	
77	## Reviewer Evaluation
78	
79	**Scores**:
80	  - entry_triage_x: **33.0**/5
81	  - exit_triage_z: **37.0**/5
82	
83	## Human Review Note
84	
85	## External Review — Verdict: PASS
86	
87	- X (entry triage): 33.0%
88	- Y (terminal self-eval): 44.0%
89	- Z (exit triage): 37.0%
90	- Z interval: [30.0%, 43.0%]
91	- Real improvement (Z-X): +4.0 pp
92	
93	### Optimization Suggestions
94	【优化方案】
95	
96	**A. 核心 Framing 与 Contribution 结构（影响 Novelty + Significance 天花板）**
97	
98	1. [标题 + Introduction 第 1-2 段] — 将核心定位从 "a cross-domain psychometric method for contamination detection" 重构为 **"establishing the detection frontier at the minimal-information operating point"**。系统性地将所有现有方法按 information access level 排列（binary response pattern < rephrased-item re-test < token probabilities < logits < full weights），IRT-FIT 处于最底层，回答 "仅凭 binary response pattern 能检测到什么" 这一基础问题。 — 命中 Novelty（从 "yet another detector" 变为 "defines a new operating point on the detection frontier"）+ Significance（回答了一个 foundational question）
99	
100	2. [Contribution 列表] — 将原 Contribution 4 "cross-domain methodological transfer" **降级为方法论背景**（Section 4 开头一句话即可），不再作为独立贡献列出。原因：2026 年 IRT-for-LLM 已有 PSN-IRT (arXiv:2505.15055, AAAI 2026)、ATLAS (arXiv:2511.04689, AAAI 2027)、MedIRT (arXiv:2509.24186, ICLR 2027)、"Lifting the Benchmark Iceberg" (ICLR 2024) 等多篇工作，"迁移 IRT" 本身不再新颖。Novelty 聚焦于 **person-fit for contamination detection** 这一具体未被探索的应用点。 — 命中 Novelty（避免被 "IRT for LLM is well-studied" 攻击）
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30e17fe8-5bbc-454d-9194-a5e652d5f126",
  "isSidechain": true,
  "promptId": "5a905e93-7981-422f-9766-0fbbede8e369",
  "agentId": "a30c0bb91d2c09315",
  "type": "user",
  "uuid": "3c0db0e5-0f7e-48c4-b2c1-9ec30fa6aa44",
  "sourceToolAssistantUUID": "30e17fe8-5bbc-454d-9194-a5e652d5f126",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-20T23:15:45.887Z_

Now let me read the paper_framing.md to get more context on the overall narrative:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c0db0e5-0f7e-48c4-b2c1-9ec30fa6aa44",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfvZuc2a3rkbwkijBrE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3b5ba5d7-2b36-47af-9322-afed27375cf2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FpUG9BWDhrsxby8EXZwAaU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 21821,
      "cache_read_input_tokens": 30380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 21821,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T23:15:46.718Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SuHwoby3xQcxq86MtrjcYT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_framing.md",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b5ba5d7-2b36-47af-9322-afed27375cf2",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfvZuc2a3rkbwkijBrE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c1f165e7-254e-4d75-a7d2-528c8db9b5e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FpUG9BWDhrsxby8EXZwAaU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 21821,
      "cache_read_input_tokens": 30380,
      "output_tokens": 129,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 21821
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 129,
          "cache_read_input_tokens": 30380,
          "cache_creation_input_tokens": 21821,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 21821,
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

### Tool result

_source line 20 · 2026-05-20T23:15:46.724Z_

<details><summary>↩ Tool result · `toolu_01SuHwoby3xQcxq86MtrjcYT`</summary>

```text
1	# Paper Framing — irt_personfit_contam
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
5	- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
6	- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)
7	
8	## Core Claims (3 条)
9	
10	**Claim 1 (Minimal-Information Detection Framework + Controlled Validation)**:
11	IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks), and bootstrap null distributions are well-calibrated for large benchmarks (MMLU/HellaSwag KS reject 8.3%, but overall 40% due to small benchmarks like HumanEval 75%, ARC-C 58.3% — calibration degrades with n_items). In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at low contamination (5-10%), leveraging IRT structure as inductive bias. Controlled contamination experiments (QLoRA SFT injection on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct) validate the framework across model families: Qwen at 15% contamination yields |Cohen's d|=3.58 (n=3, ddof=1) with clear seen/unseen memorization fingerprint (seen lz*≈0 vs unseen=3.1); Llama confirms cross-family detection (Δlz*=-3.47 at 15%, significant). θ-fixed analysis reveals a θ-shift boundary condition: when θ is re-estimated on contaminated data, detection sensitivity can degrade (model-dependent; Qwen shows free-θ non-monotonicity due to high baseline misfit, Llama does not), but fixing θ to pre-contamination baseline restores monotonic dose-response in both families. The memorization fraction (~35-38% at 15% contamination, consistent across families) quantifies the SFT generalization effect.
12	
13	**Claim 2 (Detection Characterization)**:
14	Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), theoretical power exceeds 90% at 15% contamination. Note: power function gives an **upper bound** (assumes all contaminated items produce aberrant signal); SFT generalization reduces effective signal — ctrl-contam measures actual memorization fraction to derive adjusted ("expected") power. Both upper bound and adjusted power should be reported.
15	
16	**Claim 3 (Empirical Findings from Real LLM Data)**:
17	Three empirical findings from applying IRT person-fit to real LLM response data: (a) **Universal 4PL model misfit** — nearly all (model, benchmark) cells produce extreme lz* values (|lz*| >> 5, 57/60 cells flagged after BH-FDR correction), revealing that LLM response patterns fundamentally differ from classical test-taker patterns. This is a genuine property of LLM responses (bootstrap null is well-calibrated), not a statistical artifact. The simulation-to-reality gap motivates the Δlz* design. (b) **PSN-IRT 12-model case study** — detailed anomaly profiles with validated 4PL parameters (Gemini-1.5: 100% MMLU accuracy, lz*=+31.81, θ=0.78; selective vs uniform misfit patterns across benchmarks; Ward clustering reveals contamination typology). (c) **IRT parameter estimation challenges** — MML-EM refit from v1 leaderboard data (N=63→178, covering all available models) yields b_r=0.66 (partial difficulty validation) but a_r≈0.13 (discrimination failure, well below 0.2 threshold), quantifying the sample size gap between classical IRT and neural IRT estimation in LLM contexts. 13K+ model per-item data is publicly available for future large-scale audits once estimation challenges are resolved.
18	
19	## Story Spine
20	
21	**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.
22	
23	**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.
24	
25	**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks) with well-calibrated null distributions; (2) in real LLM data, response patterns universally deviate from 4PL predictions — the statistical framework is sound, but LLMs genuinely violate IRT assumptions (local independence, unidimensionality), producing extreme lz* values across nearly all models; (3) controlled contamination experiments leverage this by measuring Δlz* between clean and contaminated models — since the null is well-calibrated, within-model shifts are statistically interpretable. The universal model misfit finding is itself a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns.
26	
27	**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items) with well-calibrated null distributions. In simulation, lz* matches or outperforms supervised binary classifiers (LR/RF with oracle labels) at practically relevant low contamination levels (5-10%), leveraging IRT structure as an inductive bias that compensates for the absence of labeled data. While all LLMs exhibit universal 4PL model misfit (a finding in itself), controlled experiments show contamination induces a measurable Δlz* shift of X SD above each model's baseline misfit, enabling detection even in the presence of universal misfit."
28	
29	## Venue Fit Risks
30	
31	- **EMNLP**: NLP evaluation methodology fits well. Risk: "no new NLP model/technique" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).
32	- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.
33	- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.
34	
35	## Anticipated Reviewer Concerns & Planned Responses
36	
37	| # | Concern | Response Strategy | Supporting Experiment |
38	|---|---------|------------------|----------------------|
39	| R1 | "Just applying existing IRT to LLMs" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade "cross-domain" from contribution to background. | — |
40	| R2 | "No ground truth contamination labels" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |
41	| R3 | "Power too low for small benchmarks" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |
42	| R4 | "Only 12 models" | 12 models with validated 4PL parameters provide detailed anomaly profiles. Universal misfit (57/60 flagged) spans sufficient models to establish the pattern. 13K+ v1 per-item data availability discussed as future work. Ctrl-contam covers 4-5 model families. | exp-ctrl-contam, phase_b_personfit |
43	| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
44	| R6 | "Absolute lz* thresholds don't work on real data" | Bootstrap null is well-calibrated (KS pass for large benchmarks); the issue is LLMs genuinely deviate from 4PL. Universal model misfit is a finding, not an artifact. Δlz* leverages the well-calibrated null for within-model comparisons. | exp-ctrl-contam, exp-empirical-null |
45	| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
46	| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |
47	| R9 | "No same-level binary-only baselines" | accuracy z-score (done, lz* dominates 57/60 vs 4/60) + ML classifier on binary vectors (simulation train, ctrl-contam test). lz* advantage: per-cell statistic needing no training data. | exp-accuracy-zscore-baseline, exp-ml-classifier-baseline |
48	| R10 | "Leaderboard audit baseline unreliable" | Leaderboard audit abandoned (D011). ctrl-contam is the validated detection. 12-model case study uses PSN-IRT validated parameters directly (no baseline estimation needed). v1 data availability noted as future work. | exp-ctrl-contam |
49	| R11 | "Power function is upper bound" | Report both theoretical upper bound AND adjusted power (memorization fraction from ctrl-contam seen/unseen split). Gap = SFT generalization effect quantification. | exp-ctrl-contam, exp-power-theory |
50	
51	## Key Narrative Elements (from External Review + Distillation)
52	
53	1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
54	2. **Definitional pivot (à la ConStat)** — "All prior contamination detection methods require privileged access. We ask a more fundamental question: what can be detected from binary response patterns alone?" This reframes our work as problem reformulation, not just cross-domain transfer.
55	3. **RL-robustness as structural advantage** — Wang et al. (ICLR 2026) proves all 10 log-prob methods ≈ random on RL-trained reasoning models. Person-fit operates on binary response patterns, not token distributions — structurally immune to RL-induced distributional shifts. This is our strongest motivation against log-prob baselines.
56	4. **Scalability potential (deferred to future work)** — 13K+ v1 per-item data publicly available. IRT-FIT is uniquely suited for retrospective audit (only needs archival binary data). BUT: current paper does NOT include large-scale audit (D011: IRT refit failed). Mention data availability + roadmap in Discussion/Future Work. NEVER claim "leaderboard audit" or "large-scale detection" in current paper.
57	5. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse. Theory gives R²=0.957 fit.
58	6. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.
59	7. **Terminology guard** — NEVER use "binary information bottleneck" or "information-theoretic lower bound for all binary-only methods." We can only claim lz* (a specific statistic) has limitations under SFT generalization — NOT that all binary-only methods fail. Correct framing: "IRT person-fit as a principled framework at the minimal-information operating point."
60	8. **Validation hierarchy** — ctrl-contam = primary validation (ground truth, same model clean vs contaminated); 12-model case study = empirical findings (no ground truth, but validated parameters); v1 data = future work roadmap. Paper structure should reflect this priority.
61	9. **lz* measures memorization, not generalization** — lz* detects aberrant patterns (memorization signature), not smooth ability improvement (generalization). This is a feature: it distinguishes genuine learning from rote memorization. Power function gives upper bound; ctrl-contam measures actual memorization fraction.
62	10. **Negative results as contributions** — D007 (universal misfit) and D008 (empirical null well-calibrated) are "honest negative results that become positive contributions": universal misfit is a novel finding about LLM response patterns; the simulation-reality gap motivates Δlz* and quantifies SFT generalization. D011 (MML-EM refit failure) is a methodological caveat (classical vs neural IRT sample requirements). D009 (item alignment) is a data engineering detail (1 sentence in Data section). Present negatives with the framing: "the gap between where IRT works perfectly (simulation) and where it struggles (real LLM data) is itself informative."
63	11. **ctrl-contam actual results (D015)** — contam_15 |d|=3.85 (strong), contam_50 non-monotonic under free-θ but **monotonic under θ-fixed** (ratio=2.93). θ-shift is the mechanism: contamination→higher θ_MLE→absorbs aberrance signal. Frame as "principled detection with quantified operating characteristics + θ-shift boundary condition." Headline: "We don't just detect — we characterize, including the conditions under which detection degrades." Do NOT claim "state-of-the-art detection."
64	12. **θ-shift as methodological contribution (D015)** — Person-fit sensitivity degrades when θ is re-estimated on contaminated data. This is a novel finding for contamination detection: (a) θ-fixed analysis recovers monotonic dose-response, (b) the θ-shift magnitude (0.47 at 50% contamination) quantifies the confound, (c) practical implication: use pre-contamination θ baseline or cross-validated θ. Present as a contribution, not a limitation.
65	13. **seen/unseen split as strongest signal** — contam_15 seen lz*≈0 (memorized items look "normal") vs unseen lz*=3.1. This is the clearest contamination fingerprint: items that should produce aberrant responses instead produce expected responses. More interpretable than aggregate Δlz*.
66	
67	## Writing Strategy (from Distillation)
68	
69	- **Story type**: "跨界迁移型" — unused in 0/8 peer papers. Our unique angle.
70	- **Figure 1**: Problem illustration (dual-panel: contaminated vs clean response pattern). Use psychometric hook — impossible response pattern (hard items right, easy wrong).
71	- **Contribution structure**: 3 contributions (method + characterization + empirical findings), escalating scope. Standard in 5/8 papers.
72	- **Result tables**: Row=methods, col=datasets×metrics. Bold-best. Average column.
73	- **Numbered findings**: Adopt PSN-IRT's "Key Discoveries" strategy for scannable presentation.
74	- **CIs as differentiator**: 6/8 peer papers report no variance. Our bootstrap CIs are a competitive advantage.
75	- **Baseline count**: Peer median ~5. Target ≥5 baselines.
76	
77	## Evidence Summary
78	
79	- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
80	- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+31.81. Cross-benchmark anomaly profiles identified.
81	- **Empirical null analysis (exp-empirical-null)**: Bootstrap null calibration is benchmark-size dependent — large benchmarks well-calibrated (MMLU: mean bias 0.041, std 1.003, KS reject 8.3%; HellaSwag: 8.3%), small benchmarks poorly calibrated (HumanEval: 75%, ARC-C: 58.3%; overall KS reject 40%, 24/60). The statistical framework is sound for large benchmarks (n>10K). 57/60 real-data cells flagged because LLM lz* values are genuinely extreme (|lz*| >> 5) — this reflects **universal 4PL model misfit** (LLM response patterns violate IRT assumptions), not contamination-specific detection. **Important**: 57/60 vs accuracy z-score 4/60 demonstrates lz* captures response-pattern information beyond aggregate accuracy (evidence for Claim 3a universal misfit), NOT contamination detection superiority. Contamination detection evidence comes from simulation (lz* AUROC 0.675 vs ML 0.575 at 5%) and ctrl-contam (d=3.58, n=3, ddof=1).
82	- **Calibration gap reframed (D007→D008)**: The gap is not "null is biased" but "real LLM data genuinely deviates from 4PL". This strengthens Δlz* approach: well-calibrated null means within-model shifts are statistically meaningful.
83	- **Controlled contamination (exp-ctrl-contam-pilot, D015)**: Qwen2.5-7B-Instruct × MMLU, 4 conditions (0%×3 seeds, 15%, 50%). **n=3 clean seeds**: s1 lz*=8.01, s2=5.94, s3=8.08 (s2 outlier; mean=7.345, std=1.214). Key results: (a) contam_15 |Cohen's d|=3.58 (n=3, ddof=1, strong effect); (b) contam_50 |d|=1.56 (n=3, ddof=1); (c) free-θ dose-response non-monotonic (contam_50 Δlz*=1.90 < contam_15 Δlz*=4.34) due to θ-shift confound; (d) **θ-fixed analysis restores monotonicity** (θ_fixed=-0.0966 from n=3 mean; Δlz*_fixed: contam_15=+2.68, contam_50=+8.37, ratio=3.12; Cohen's d_fixed: contam_15=2.95, contam_50=9.21); (e) seen/unseen split: contam_15 seen lz*≈0 vs unseen=3.1 (clear memorization fingerprint); (f) memorization_fraction=0.38 (15%) and 0.29 (50%). θ-shift mechanism: contamination raises θ_MLE, absorbing aberrance signal — this is a methodological contribution. **Note**: prior d=3.85 used ddof=0 (population std); paper uses ddof=1 throughout.
84	- **Cross-family validation (exp-ctrl-contam-llama)**: Llama-3.1-8B-Instruct × MMLU, 3 conditions (clean, 15%, 50%). Key results: (a) Detection signal confirmed: Δlz*_15=-3.47, Δlz*_50=-3.68, both |Δlz*|>1.96 (significant). (b) **Free-θ non-monotonicity does NOT reproduce** — Llama shows slight monotonicity (50% slightly > 15%), contrasting Qwen's strong non-monotonicity. (c) Difference explained by baseline misfit: Llama clean lz*=0.82 (near null) vs Qwen clean lz*=7.35 (highly abnormal) — θ-shift has less "room" to absorb signal in Llama. (d) θ-shift mechanism IS universal: Llama Δθ=0.390/0.517 vs Qwen Δθ=0.294/0.467. (e) Memorization fraction consistent: Llama 0.351/0.327 vs Qwen 0.38/0.29. (f) θ_fixed analysis pending. (g) n=1 clean seed — Cohen's d not computable without additional seeds. **Narrative implication**: Finding 2 (non-monotonicity) must be qualified as "model-dependent, modulated by baseline misfit magnitude" rather than universal. θ-shift mechanism remains universal. Qwen's high clean baseline (lz*=7.35) suggests possible pretraining MMLU exposure — discuss in §6.
85	- **4PL real-data degradation**: 3PL(d=1) vs 4PL lz* correlation r=0.225, RMSE=68.41. d parameter essential for high-ability models (DeepSeek-V3 Δ=357). Complements simulation ablation (+14-27pp power gain).
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1f165e7-254e-4d75-a7d2-528c8db9b5e5",
  "isSidechain": true,
  "promptId": "5a905e93-7981-422f-9766-0fbbede8e369",
  "agentId": "a30c0bb91d2c09315",
  "type": "user",
  "uuid": "c8818413-433c-4257-ba41-746947d17374",
  "sourceToolAssistantUUID": "c1f165e7-254e-4d75-a7d2-528c8db9b5e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-20T23:16:06.441Z_

Perfect! Now I have comprehensive context. Let me compile my findings report.

---

## Summary of Context Files Found

I've successfully located and reviewed the key context files for writing your Introduction section. Here's what I found:

### **Files Located:**

1. **writing_plan.yaml** — `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/writing_plan.yaml` (596 lines)
   - Complete writing plan including section budgets, key elements, narrative strategy, and contribution structure
   
2. **paper/sections/introduction.tex** — `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper/sections/introduction.tex`
   - Currently empty (only has placeholder `% introduction`)

3. **memory.md** — `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md` (190 lines)
   - Detailed technical findings from all experiments, key discoveries, and lessons learned

4. **paper_framing.md** — `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_framing.md` (86 lines)
   - Core narrative, venue fit, anticipated reviewer concerns, and writing strategy

5. **docs/IDEA_BRIEF.md** — `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/docs/IDEA_BRIEF.md` (100+ lines)
   - Original idea with problem statement, opportunity, landscape, and resource estimates

### **Key Context for Introduction (from writing_plan.yaml, sec_introduction):**

**Word budget:** 700 words  
**Key elements** (6 paragraphs):
- **P1:** Problem — contamination threatens evaluation integrity, structural cause (training corpora ∩ public benchmarks)
- **P2:** Existing methods critique — ALL require privileged access. Detection frontier ranking: binary < rephrased retest < token probs < logits < weights
- **P3:** RL-robustness motivation — Wang et al. shows all 10 log-prob methods ≈ random on RL models. Binary patterns structurally immune to RL distributional shifts
- **P4:** Cross-domain insight — contaminated LLM ≡ examinee with item preknowledge. Person-fit literature: decades of cheating detection. Gap: 0/N papers connect person-fit to LLM contamination
- **P5:** Our approach — IRT-FIT at minimal-information operating point. Key results preview (numbers from experiments)
- **P6:** 3 contributions (method+characterization+empirical findings), escalating scope

**Narrative strategy:** "跨界迁移型" (cross-domain transfer, unused in peer papers — this is your differentiator)
- Hook: "ConStat definitional pivot — All prior methods require privileged access. We ask: what can be detected from binary response patterns alone?"
- Wang's technique: prove existing methods fail → create urgency
- PSN-IRT's numbered findings for scannability

### **Critical Experimental Results to Reference:**

From **memory.md** and **paper_framing.md**, the key numbers for your Introduction P5 preview are:

1. **Simulation (Claim 1):** MMLU power@15%=97.9%, well-calibrated null (KS reject 8.3% for large benchmarks)
2. **Controlled contamination (D015):** Qwen2.5-7B at 15% contamination |Cohen's d|=3.58 (n=3, ddof=1), seen/unseen split shows clear memorization fingerprint (seen lz*≈0 vs unseen=3.1)
3. **Real data finding:** 57/60 cells flagged (universal 4PL misfit), motivates Δlz* design
4. **Cross-family:** Llama-3.1-8B confirms detection signal Δlz*=-3.47 at 15% contamination

### **Narrative Strategy from paper_framing.md:**

The **definitive framing** (from external review optimization):
- Reposition from "a cross-domain method" → **"establishing the detection frontier at the minimal-information operating point"**
- Systematically rank all existing methods by information access level; IRT-FIT sits at the bottom (binary patterns only)
- This answers a foundational question: "What can be detected without privileged access?"
- Wang et al. (2025) provides urgency: all MIA-based methods fail on RL models, binary patterns are structurally robust to RL distributional shifts

### **Existing Paper Structure:**

The **paper_outline** from writing_plan.yaml shows:
- 6 benchmarks: MMLU (14042), HellaSwag (10042), GSM8K (1319), ARC-C (295), HumanEval (164)
- 12 models from PSN-IRT dataset with validated 4PL parameters
- Main contributions: (1) method + characterization framework, (2) power function analysis, (3) controlled contamination validation, (4) empirical findings from real LLM data

---

## Recommendation for Introduction Writing:

Use the **6-paragraph structure** from writing_plan.yaml, grounding each paragraph in the context provided:

1. **P1 (Problem):** Start with evaluation integrity threat, cite contamination frequency in training corpora
2. **P2 (Methods critique):** Create **detection frontier table** — this is your chance to position relative to ConStat, Min-K%++, Time Travel, CoDeC, etc. Highlight that IRT-FIT requires ONLY binary patterns
3. **P3 (RL motivation):** Cite Wang et al. 2025 on log-prob method failures; binary patterns are immune to RL distributional shifts
4. **P4 (Cross-domain insight):** Establish the analogy — contaminated LLM = test-taker with item preknowledge. This is the psychological/educational testing precedent (Drasgow 1985, Sinharay 2017, Karabatsos 2003)
5. **P5 (Results preview):** Use concrete numbers: MMLU 97.9% power, Qwen d=3.58 at 15%, θ-shift mechanism quantified
6. **P6 (Contributions):** Three claims escalating in scope: (1) framework validation, (2) power function characterization, (3) empirical findings from real LLM response patterns

The **key differentiator** is the definitional pivot: instead of "we apply IRT to LLMs," frame as **"we establish the minimal-information operating point on the contamination detection frontier"** — this answers a foundational question that shifts the positioning from transfer-learning to problem-reformulation.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8818413-433c-4257-ba41-746947d17374",
  "isSidechain": true,
  "agentId": "a30c0bb91d2c09315",
  "requestId": "req_011CbEfvmUNoFiJfDUiQJFaQ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d91e9771-a45b-4675-b174-78c80a99a12a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "632717c4-3f64-4c58-a4db-b849f9fe04a4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015BfXKU4PwPDXFYkNjmWw3A",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5718,
      "cache_read_input_tokens": 52201,
      "output_tokens": 1670,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5718
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1670,
          "cache_read_input_tokens": 52201,
          "cache_creation_input_tokens": 5718,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5718,
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
