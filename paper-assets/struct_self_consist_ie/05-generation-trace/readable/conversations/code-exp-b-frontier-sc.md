# code exp b frontier sc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 119
- **Recorded user turns:** 0
- **Tool calls:** 59
- **Original source:** `logs/chats/worker_code_exp_b_frontier_sc_20260520T181716.jsonl`
- **Structured JSON:** [`49d956942b2767013dae.json`](../../sessions/49/49d956942b2767013dae.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

119 recorded events

### Tool call

_source line 1 · 2026-05-20T18:25:10.636072+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T18:25:10.636401+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T18:25:10.636556+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenRouter model ID GPT-5.5 Claude Opus 4.6 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenRouter model ID GPT-5.5 Claude Opus 4.6 2026"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T18:25:10.636718+00:00_

Web search results for query: "OpenRouter model ID GPT-5.5 Claude Opus 4.6 2026"

Links: [{"title":"Claude Opus 4.6 - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/anthropic/claude-opus-4.6"},{"title":"Models | OpenRouter","url":"https://openrouter.ai/models"},{"title":"Hermes Agent + GPT-5.5 — OpenAI's Latest Model with Hermes | OpenClaw Launch","url":"https://openclawlaunch.com/guides/hermes-agent-gpt-5-5"},{"title":"GPT-5.5 vs Claude Opus 4.6 (Fast) - AI Model Comparison | OpenRouter","url":"https://openrouter.ai/compare/openai/gpt-5.5/anthropic/claude-opus-4.6-fast"},{"title":"Claude Opus 4.7 - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/anthropic/claude-opus-4.7"},{"title":"Anthropic API and Models | OpenRouter","url":"https://openrouter.ai/anthropic"},{"title":"Anthropic | OpenRouter","url":"https://openrouter.ai/provider/anthropic"},{"title":"Integration with Claude Code | OpenRouter | OpenRouter | Documentation","url":"https://openrouter.ai/docs/cookbook/coding-agents/claude-code-integration"},{"title":"How to Run Claude Code with Cheaper Models: OpenRouter, NVIDIA NIM, and Ollama | MindStudio","url":"https://www.mindstudio.ai/blog/claude-code-cheaper-models-openrouter-nvidia-nim-ollama"},{"title":"Claude Opus 4.5 - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/anthropic/claude-opus-4.5"}]

Based on the search results, here's what I found about these models on OpenRouter:

## GPT-5.5
GPT-5.5 is available in OpenRouter using the model ID openai/gpt-5.5. GPT-5.5 is OpenAI's flagship model as of 2026, succeeding the GPT-4o line.

## Claude Opus 4.6
Opus 4.6 is Anthropic's strongest model for coding and long-running professional tasks. The model ID on OpenRouter is **anthropic/claude-opus-4.6**. It was released on Feb 4, 2026 with pricing of $5 per million input tokens, $25 per million output tokens.

The search results confirm both models are available on OpenRouter in 2026, with the specific m
…[truncated 203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T18:25:10.636878+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore project structure and code patterns",
  "prompt": "I need to understand the project structure and existing code patterns for an NER experiment project. Please explore:\n\n1. The directory structure under /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ — especially `artifacts/`, `src/`, and any existing experiment scripts\n2. Look for existing NER prompt templates or UIE JSON schema definitions used in the project\n3. Check if there's any FewNERD data locally (test.json or similar)\n4. Look for existing experiment scripts that use OpenAI SDK or API calls for reference on the project's coding patterns\n5. Check for any existing majority vote / self-consistency implementation code\n6. Look at how the project structures its entity types (the 8 FewNERD coarse types)\n\nSearch breadth: very thorough. Report file paths, key code snippets, and patterns found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Explore project structure and code patterns",
    "prompt": "I need to understand the project structure and existing code patterns for an NER experiment project. Please explore:\n\n1. The directory structure under /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ — especially `artifacts/`, `src/`, and any existing experiment scripts\n2. Look for existing NER prompt templates or UIE JSON schema definitions used in the project\n3. Check if there's any FewNERD data locally (test.json or similar)\n4. Look for existing experiment scripts that use OpenAI SDK or API calls for reference on the project's coding patterns\n5. Check for any existing majority vote / self-consistency implementation code\n6. Look at how the project structures its entity types (the 8 FewNERD coarse types)\n\nSearch breadth: very thorough. Report file paths, key code snippets, and patterns found."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-20T18:25:10.637057+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.py\" -o -name \"*.json\" -o -name \"*.txt\" -o -name \"*.md\" | head -100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.py\" -o -name \"*.json\" -o -name \"*.txt\" -o -name \"*.md\" | head -100"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-20T18:25:10.637252+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/j_calibration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/adalp_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/dals_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_n16_readiness_check_20260515T100959_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_exp_027_merge_analyze_20260517T053441_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_sampling_and_main_20260514T042643_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_ssh_download-fig10-oracle-scaling_20260520T133635_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_exp_qwen25_7b_fewnerd_v3_20260519T112555_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_exp017_lp_range_20260515T154349_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_exp021_within_rho_20260517T203007_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_exp_017_llama_conll_inference_202605
…[truncated 13366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T18:25:10.637411+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "tree -L 3 -d /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type d | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "tree -L 3 -d /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie 2>/dev/null || find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type d | head -50"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T18:25:10.637549+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/results
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/results/figures
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context/history
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context/history/director
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context/history/agent
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context/history/reviewer
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/share
/home/ubuntu/.
…[truncated 3873 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T18:25:10.637700+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 2 -type d | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 2 -type d | sort"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-20T18:25:10.637854+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/bin
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/include
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/share
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/3seed_summary
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/__pycache__
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/a2_degen_regression
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/a4_pareto_diversity
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b1_scd_prep
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b2_oof
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b2_v2_multi_domain
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b2_v3_domain_invariant
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b2_v4_inverse_freq
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b2_verifier
/home/ubuntu/.agent-ml-research-idea
…[truncated 14378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T18:25:10.637999+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code -type f -name \"*.py\" 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code -type f -name \"*.py\" 2>/dev/null | head -30"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T18:25:10.638117+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/aggregate_scaling_results.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/plot_scaling_curve.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/exp_b3_prompted_diversity.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/analysis_mbr_selection.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/generate_scale_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/zeroshot_prompts.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T18:25:10.638275+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data -type f 2>/dev/null | head -20"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-20T18:25:10.638390+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/qwen_scierc_3seed_em_voting.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/bootstrap_ci_summary.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T18:25:10.638514+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*{prompt,ner,uie,schema,few*,entity,fewnerd}*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*{prompt,ner,uie,schema,few*,entity,fewnerd}*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T18:25:10.638631+00:00_

.venv/lib/python3.14/site-packages/pip/__pip-runner__.py
.venv/lib/python3.14/site-packages/pip/_internal/cli/spinners.py
.venv/lib/python3.14/site-packages/pip/_vendor/pygments/scanner.py
.venv/lib/python3.14/site-packages/pip/_vendor/rich/_spinners.py
.venv/lib/python3.14/site-packages/pip/_vendor/rich/containers.py
.venv/lib/python3.14/site-packages/pip/_vendor/rich/prompt.py
.venv/lib/python3.14/site-packages/pip/_vendor/rich/spinner.py
.venv/lib/python3.14/site-packages/PIL/ContainerIO.py
.venv/lib/python3.14/site-packages/numpy/random/tests/test_generator_mt19937.py
.venv/lib/python3.14/site-packages/numpy/random/tests/test_generator_mt19937_regressions.py
.venv/lib/python3.14/site-packages/fontTools/varLib/avarPlanner.py
.venv/lib/python3.14/site-packages/matplotlib/container.py
.venv/lib/python3.14/site-packages/matplotlib/tests/test_container.py
artifacts/hidden_state_probe/extract_hidden_states_fewnerd.py
artifacts/hidden_state_probe/hidden_state_probe_fewnerd.py
artifacts/entity_construction.py
artifacts/entity_construction_fair.py
code/zeroshot_prompts.py
code/generate_scale_table.py
b2_entity_verifier.py
code/exp_b3_prompted_diversity.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T18:25:10.638755+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*{prompt,ner,uie,schema,test,data}*.json",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*{prompt,ner,uie,schema,test,data}*.json",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T18:25:10.638883+00:00_

logs/workers/worker_code_data_eval_modules_20260514T042533_result.json
logs/workers/worker_data_scierc_prep_20260514T052927_result.json
logs/workers/worker_research_e4_dataset_survey_20260514T092619_result.json
artifacts/dream_reports/dream_20260514T093336/best/experiment_data.json
artifacts/dream_reports/dream_20260514T093336/median/experiment_data.json
artifacts/dream_reports/dream_20260514T093336/worst/experiment_data.json
logs/workers/worker_code_conll2003_data_prep_20260514T100814_result.json
logs/workers/worker_code_wnut17_data_prep_20260514T100828_result.json
artifacts/dream_reports/dream_20260514T105303/best/experiment_data.json
logs/workers/worker_code_data_format_fix_20260514T113420_result.json
artifacts/dream_reports/dream_20260514T105303/median/experiment_data.json
checkpoints/exp_001_ner_n16_scierc_PENDING_20260514T114210.json
checkpoints/exp_002_ner_conll2003_PENDING_20260514T114215.json
checkpoints/exp_003_ner_wnut17_PENDING_20260514T114217.json
artifacts/dream_reports/dream_20260514T105303/worst/experiment_data.json
checkpoints/exp_007_ner_multi_model_PENDING_20260514T114220.json
checkpoints/exp_007_ner_llama_PREPARING_20260514T114221.json
checkpoints/exp_001_ner_n16_scierc_QUEUED_20260514T114257.json
checkpoints/exp_002_ner_conll2003_QUEUED_20260514T114258.json
checkpoints/exp_003_ner_wnut17_QUEUED_20260514T114258.json
checkpoints/exp_007_ner_multi_model_QUEUED_20260514T114259.json
logs/workers/worker_code_check_dataset_and_logprob_readiness_20260514T114258_result.json
checkpoints/exp_001_ner_n16_scierc_RUNNING_20260514T115007.json
checkpoints/exp_002_ner_conll2003_RUNNING_20260514T115032.json
logs/workers/worker_gpu_exp_002_ner_conll2003_20260514T114609_result.json
checkpoints/exp_001_ner_n16_scierc_RUNNING_20260514T115541.json
checkpoints/exp_001_ner_n16_scierc_DONE_20260514T115545.json
logs/workers/worker_gpu_exp_001_ner_n16_scierc_20260514T114538_result.json
checkpoints/exp_002_ner_conll2003_RUNNING_20260514T120258.json
checkpoints/exp_003_ner_w
…[truncated 4902 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T18:25:10.639024+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "openai|OpenAI|api_call|completion|gpt",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code",
  "type": "py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "tool_args": {
    "pattern": "openai|OpenAI|api_call|completion|gpt",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code",
    "type": "py"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T18:25:10.639163+00:00_

Found 1 file
code/zeroshot_prompts.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T18:25:10.639309+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "majority_vote|voting|ensemble|consistency|self_consistency",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "tool_args": {
    "pattern": "majority_vote|voting|ensemble|consistency|self_consistency",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T18:25:10.639453+00:00_

Found 172 files
artifacts/exp_asb_adaptive_budget/data/run_asb.py
artifacts/experiments/asb/run_asb.py
artifacts/exp_backup3_distill_verifier/intermediate/run_distill_verifier.py
artifacts/experiments/distill_verifier/run_distill_verifier.py
artifacts/experiments/het_temp/run_het_temp.py
artifacts/experiments/lsc/run_lsc.py
artifacts/exp_lsc_latent_sc/data/run_lsc.py
artifacts/run_lsc.py
artifacts/run_mrsc.py
artifacts/experiments/mrsc/run_mrsc.py
artifacts/experiments/esj/run_esj.py
code/exp_b3_prompted_diversity.py
artifacts/b2_v4_inverse_freq/b2_v4_inverse_freq.py
artifacts/b2_oof/b2_oof_evaluation.py
artifacts/b2_v3_domain_invariant/b2_v3_domain_invariant.py
artifacts/b2_v2_multi_domain/b2_v2_multi_domain.py
artifacts/k_robustness/robustness_analysis.py
artifacts/e2v2_regime_weights/e2v2_regime_weights.py
artifacts/e2v2_regime_weights/intermediate/e2v2_regime_weights.py
artifacts/e1v2_signal_routing/e1v2_signal_routing.py
artifacts/exp_e1v2_signal_routing/data/e1v2_signal_routing.py
artifacts/n_inverse_scaling/run_analysis.py
artifacts/e2_ensemble/run_e2_ensemble.py
b2_entity_verifier.py
e1_signal_routing.py
artifacts/construction_variants.py
artifacts/_project/intermediate/compute_signals.py
artifacts/compute_signals.py
artifacts/entity_construction_fair.py
artifacts/entity_construction.py
artifacts/selective_prediction.py
artifacts/lp_alignment_gated_selection.py
artifacts/ccs_selection.py
artifacts/bootstrap_selection_test.py
artifacts/evaluation.py
artifacts/exp_019_trained_verifier/train_verifier.py
artifacts/exp-019/intermediate/train_verifier.py
artifacts/analyze_ood_signals.py
artifacts/evaluate_verifier.py
artifacts/re_conditional_analysis.py
artifacts/n8_bootstrap_ci.py
.venv/lib/python3.14/site-packages/mpl_toolkits/mplot3d/tests/test_legend3d.py
.venv/lib/python3.14/site-packages/mpl_toolkits/mplot3d/axes3d.py
.venv/lib/python3.14/site-packages/matplotlib/tests/test_legend.py
.venv/lib/python3.14/site-packages/matplotlib/tests/test_fontconfig_pattern
…[truncated 8020 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T18:25:10.639603+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "class.*NER|def.*ner|extract.*entity|entity_types|coarse|fine",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code",
  "type": "py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "tool_args": {
    "pattern": "class.*NER|def.*ner|extract.*entity|entity_types|coarse|fine",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code",
    "type": "py",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-20T18:25:10.639719+00:00_

Found 5 files
code/exp_b3_prompted_diversity.py
code/plot_scaling_curve.py
code/generate_scale_table.py
code/aggregate_scaling_results.py
code/analysis_mbr_selection.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T18:25:10.639839+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 1 -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 1 -type f -name \"*.py\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T18:25:10.639949+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/e1_signal_routing.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/analysis_r21_q1_alignment.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/b2_entity_verifier.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T18:25:10.640065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/zeroshot_prompts.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/zeroshot_prompts.py"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T18:25:10.640235+00:00_

1	"""Zero-shot NER prompt templates for Qwen2.5-72B baseline evaluation.
2	
3	Output format is compatible with the existing pipeline (sampling.py):
4	  {"entities": [{"text": "...", "type": "...", "start": &lt;int>, "end": &lt;int>}],
5	   "relations": [], "events": []}
6	"""
7	
8	# ---------------------------------------------------------------------------
9	# Entity type definitions per dataset
10	# ---------------------------------------------------------------------------
11	
12	DATASET_ENTITY_TYPES = {
13	    "conll2003": {
14	        "types": ["PER", "ORG", "LOC", "MISC"],
15	        "descriptions": {
16	            "PER": "Person names (e.g., John Smith, Obama)",
17	            "ORG": "Organizations (e.g., Google, United Nations)",
18	            "LOC": "Locations (e.g., France, Mount Everest)",
19	            "MISC": "Miscellaneous named entities not fitting PER/ORG/LOC (e.g., English, World Cup)",
20	        },
21	    },
22	    "fewnerd": {
23	        "types": ["person", "organization", "location", "building", "art", "product", "event", "other"],
24	        "descriptions": {
25	            "person": "Person names",
26	            "organization": "Organizations, companies, teams",
27	            "location": "Geographic locations, countries, cities",
28	            "building": "Buildings, facilities, landmarks",
29	            "art": "Artworks, songs, films, books",
30	            "product": "Commercial products, software, vehicles",
31	            "event": "Events, competitions, wars, festivals",
32	            "other": "Other named entities not fitting the above categories",
33	        },
34	    },
35	    "scierc": {
36	        "types": ["Generic", "Material", "Method", "Metric", "OtherScientificTerm", "Task"],
37	        "descriptions": {
38	            "Generic": "Generic references to scientific concepts (coreference)",
39	            "Material": "Data, datasets, corpora, resources",
40	            "Method": "Algorithms, models, systems, tools",
41	           
…[truncated 5191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T18:25:10.640395+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*fewnerd*\" -o -name \"*test.json\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*fewnerd*\" -o -name \"*test.json\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T18:25:10.640525+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_exp_qwen25_7b_fewnerd_v3_20260519T112555_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_llama_fewnerd_inference_status_v3_20260519T024716_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_exp_fewnerd_dals_multiseed_20260518T070429_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_llama_fewnerd_completion_check_20260519T010728_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_audit_recompute_tab_fewnerd_all_20260518T041428_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_llama_fewnerd_merge_prep_20260518T222902_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_exp_exp_020_fewnerd_smoke_20260516T103407_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_exp_hidden_probe_fewnerd_20260518T105429.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_llama_fewnerd_progress_check_20260519T002618_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_exp_qwen_fewnerd_seed456_20260518T092846.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_verify_7b_fewnerd_running_20260519T114923.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_fewnerd_seed42_reanalyze_20260518T210539_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_gpu_exp_14b_inferen
…[truncated 1098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T18:25:10.640661+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/entity_construction.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/entity_construction.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T18:25:10.640797+00:00_

1	"""Entity-Level Majority Vote Construction for NER and RE.
2	
3	Core hypothesis: the correct analogy for self-consistency on structured output
4	is entity-level majority vote construction, not instance-level best-of-N selection.
5	"""
6	
7	import json
8	import math
9	import os
10	import sys
11	import numpy as np
12	from collections import defaultdict
13	
14	# ---------------------------------------------------------------------------
15	# Metrics (mirroring unified_metrics.py)
16	# ---------------------------------------------------------------------------
17	
18	def compute_prf(pred_set, gold_set):
19	    if not gold_set and not pred_set:
20	        return 1.0, 1.0, 1.0
21	    if not pred_set:
22	        return 0.0, 0.0, 0.0
23	    if not gold_set:
24	        return 0.0, 0.0, 0.0
25	    tp = len(pred_set & gold_set)
26	    if tp == 0:
27	        return 0.0, 0.0, 0.0
28	    p = tp / len(pred_set)
29	    r = tp / len(gold_set)
30	    f = 2 * p * r / (p + r)
31	    return p, r, f
32	
33	
34	def entity_set(entities):
35	    return {(e["start"], e["end"], e["type"]) for e in entities}
36	
37	
38	def relation_set(relations):
39	    return {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
40	            for r in relations}
41	
42	
43	# ---------------------------------------------------------------------------
44	# Construction
45	# ---------------------------------------------------------------------------
46	
47	def entity_majority_vote(samples, threshold, weights=None):
48	    """Collect entities across N samples, keep those above threshold."""
49	    entity_counts = defaultdict(float)
50	    N = len(samples)
51	    for i, sample in enumerate(samples):
52	        w = weights[i] if weights is not None else 1.0
53	        for e in sample.get("entities", []):
54	            key = (e["start"], e["end"], e["type"])
55	            entity_counts[key] += w
56	
57	    total_weight = sum(weights) if weights is not None else N
58	    constructed = set
…[truncated 3351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T18:25:10.640949+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T18:25:10.641109+00:00_

1	"""Consistency metrics for structured information extraction with self-consistency.
2	
3	Implements three complementary consistency measures over N sampled extractions:
4	1. Fleiss' Kappa (surface matching) — treats N samples as N raters on entity presence
5	2. Structural soft Jaccard — span-level soft overlap with Hungarian matching
6	3. Oracle best-of-N — upper-bound F1 by selecting the best sample per instance
7	
8	Key dependencies: numpy, scipy (linear_sum_assignment).
9	"""
10	
11	from __future__ import annotations
12	
13	from itertools import combinations
14	from typing import TYPE_CHECKING
15	
16	import numpy as np
17	from scipy.optimize import linear_sum_assignment
18	
19	if TYPE_CHECKING:
20	    pass
21	
22	# ---------------------------------------------------------------------------
23	# Type aliases (mirrors shared data format)
24	# ---------------------------------------------------------------------------
25	Entity = dict       # {"text", "type", "start", "end"}
26	Relation = dict     # {"head", "tail", "type", ...}
27	Event = dict        # {"trigger": {...}, "arguments": [...]}
28	Extraction = dict   # {"entities", "relations", "events"}
29	
30	
31	# ===================================================================
32	# 1. Fleiss' Kappa — surface‐level entity agreement
33	# ===================================================================
34	
35	def _extract_surface_keys(sample: Extraction, subtask: str) -> set[tuple]:
36	    """Extract surface-level keys from a sample for Fleiss' Kappa computation."""
37	    if subtask == "ner":
38	        return {(e["text"], e["type"]) for e in sample.get("entities", [])}
39	    elif subtask == "re":
40	        return {(r["head"], r["tail"], r["type"]) for r in sample.get("relations", [])}
41	    elif subtask == "eae":
42	        keys: set[tuple] = set()
43	        for ev in sample.get("events", []):
44	            t = ev.get("trigger", {})
45	            for arg in ev.get("arguments", []):
46	                k
…[truncated 3767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-20T18:25:10.641291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/evaluation.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/evaluation.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T18:25:10.641428+00:00_

1	"""Evaluation module for structured self-consistency IE experiments.
2	
3	Provides strict-match NER/EAE evaluation, per-instance F1 computation,
4	correlation analysis, and summary report generation.
5	"""
6	
7	from __future__ import annotations
8	
9	import statistics
10	from typing import Any
11	
12	from scipy.stats import kendalltau, spearmanr
13	
14	
15	# ---------------------------------------------------------------------------
16	# NER evaluation (strict match)
17	# ---------------------------------------------------------------------------
18	
19	def entity_strict_match(
20	    pred_entities: list[dict],
21	    gold_entities: list[dict],
22	) -> tuple[int, int, int]:
23	    """Compute strict entity match counts.
24	
25	    Strict match requires exact span (start, end) AND exact type.
26	
27	    Args:
28	        pred_entities: Predicted entity dicts with keys text, type, start, end.
29	        gold_entities: Gold entity dicts with the same schema.
30	
31	    Returns:
32	        (tp, fp, fn) counts.
33	    """
34	    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
35	    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
36	    tp = len(pred_set & gold_set)
37	    fp = len(pred_set - gold_set)
38	    fn = len(gold_set - pred_set)
39	    return tp, fp, fn
40	
41	
42	def compute_ner_f1(
43	    predictions: list[dict],
44	    golds: list[dict],
45	) -> dict[str, float]:
46	    """Compute micro-averaged NER precision, recall, and F1.
47	
48	    Args:
49	        predictions: List of Extraction dicts (one per instance).
50	        golds: List of Extraction dicts (one per instance), aligned with predictions.
51	
52	    Returns:
53	        Dict with keys "precision", "recall", "f1".
54	    """
55	    total_tp = total_fp = total_fn = 0
56	    for pred, gold in zip(predictions, golds):
57	        tp, fp, fn = entity_strict_match(
58	            pred.get("entities", []),
59	            gold.get("entities", []),
60	        )
61	  
…[truncated 1617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-20T18:25:10.641574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/entity_construction.py",
  "offset": "150",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/entity_construction.py",
    "offset": "150",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T18:25:10.641725+00:00_

150	
151	def best_of_n_sj(inst):
152	    best_idx, best_val = 0, -float("inf")
153	    for i, s in enumerate(inst["samples"]):
154	        val = s.get("cumulative_logprob", None)
155	        if val is not None and math.isfinite(val) and val > best_val:
156	            best_val = val
157	            best_idx = i
158	    return best_idx
159	
160	
161	# ---------------------------------------------------------------------------
162	# Main experiment
163	# ---------------------------------------------------------------------------
164	
165	THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
166	
167	DATASETS = {
168	    "scierc": "/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
169	    "conll": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16/samples.jsonl",
170	    "fewnerd": "/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl",
171	}
172	
173	OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/entity_construction"
174	
175	
176	def bootstrap_ci(values, n_boot=2000, ci=0.95, seed=42):
177	    arr = np.array(values)
178	    n = len(arr)
179	    if n == 0:
180	        return 0.0, 0.0, 0.0
181	    rng = np.random.RandomState(seed)
182	    boot_means = np.array([arr[rng.randint(0, n, n)].mean() for _ in range(n_boot)])
183	    boot_means.sort()
184	    lo = boot_means[int((1 - ci) / 2 * n_boot)]
185	    hi = boot_means[int((1 + ci) / 2 * n_boot)]
186	    return float(arr.mean()), float(lo), float(hi)
187	
188	
189	def run_dataset(name, path):
190	    print(f"\n{'='*70}")
191	    print(f"Dataset: {name} ({path})")
192	    print(f"{'='*70}")
193	
194	    data = load_data(path, gold_filter=True)
195	    print(f"Loaded {len(data)} instances (gold-filtered)")
196	
197	    n_samples = len(data[0]["samples"])
198	    print(f"Samples per instance: {n_samples}")
199	
200	    has_relations = any(len(inst["gold"].get("relations", [])) > 0 for inst in data)
201	    print(f"Has relations: {h
…[truncated 6434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T18:25:10.641892+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*sampling*\" -o -name \"*inference*\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*sampling*\" -o -name \"*inference*\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T18:25:10.642020+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_sampling_and_main_20260514T042643_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_ssh_7b-zs-inference-5090c_20260520T064018.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_submit_4b_conll_scs_inference_cuda2_20260515T193149.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_exp_017_llama_conll_inference_20260517T113609_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_ssh_14b-early-inference_20260520T111801.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_llama_fewnerd_inference_status_v3_20260519T024716_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_exec_exp021_merge_inference_20260516T203650.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_llama_scierc_seed456_inference_20260518T191311.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_ssh_b7-adaptive-sampling-budget_20260520T090154.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_code_scierc_4b_merge_inference_v2_20260515T194913_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_analysis_conll_4b_inference_v2_check_20260515T194957.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_ssh_prepare-14b-inference-v2_20260520T070610.log
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/workers/worker_ssh_7b-zs-inference-5090c_20260520T064018_result.
…[truncated 1104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T18:25:10.642185+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "def.*extract|def.*parse|def.*sample|def.*api|requests|json.loads",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code",
  "type": "py",
  "output_mode": "content",
  "head_limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "tool_args": {
    "pattern": "def.*extract|def.*parse|def.*sample|def.*api|requests|json.loads",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code",
    "type": "py",
    "output_mode": "content",
    "head_limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T18:25:10.642313+00:00_

code/analysis_mbr_selection.py:30:def load_data(path, max_samples=8, gold_filter=False):
code/analysis_mbr_selection.py:34:            obj = json.loads(line)
code/analysis_mbr_selection.py:48:def text_type_set(sample):
code/analysis_mbr_selection.py:53:def span_set(sample):
code/analysis_mbr_selection.py:67:def mbr_scores(samples):
code/analysis_mbr_selection.py:77:def entity_f1(pred_sample, gold):
code/analysis_mbr_selection.py:92:def degeneracy_ratio(samples):
code/exp_b3_prompted_diversity.py:150:            obj = json.loads(line)
code/exp_b3_prompted_diversity.py:174:    def do_sample(template_name, n_samples, temperature, seed_val):
code/exp_b3_prompted_diversity.py:220:    def write_instances(samples_list, greedy_list, path, extra_fn=None):
code/exp_b3_prompted_diversity.py:292:def entity_set(sample):
code/exp_b3_prompted_diversity.py:318:def weighted_construction(samples, threshold, weights=None):
code/exp_b3_prompted_diversity.py:333:def get_lp_weights(samples):
code/exp_b3_prompted_diversity.py:339:def get_vc_weights(samples):
code/exp_b3_prompted_diversity.py:433:    single = [json.loads(l) for l in open(sp) if l.strip()]
code/exp_b3_prompted_diversity.py:434:    multi = [json.loads(l) for l in open(mp) if l.strip()]
code/exp_b3_prompted_diversity.py:484:        ti = [json.loads(l) for l in open(tp) if l.strip()]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T18:25:10.642444+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/analysis_mbr_selection.py",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/analysis_mbr_selection.py",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T18:25:10.642576+00:00_

1	#!/usr/bin/env python3
2	"""MBR (Minimum Bayes Risk) selection for NER: select sample with highest
3	average entity-set Jaccard overlap with other samples."""
4	
5	import json
6	import sys
7	from collections import defaultdict
8	
9	BASE = "/root/autodl-tmp/struct_self_consist_ie"
10	
11	DATASETS = {
12	    "SciERC": {
13	        "path": f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
14	        "max_samples": 8,
15	        "gold_filter": True,
16	    },
17	    "CoNLL": {
18	        "path": f"{BASE}/output/exp_002_conll_n16_r1024/samples.jsonl",
19	        "max_samples": 8,
20	        "gold_filter": False,
21	    },
22	    "FewNERD": {
23	        "path": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
24	        "max_samples": 8,
25	        "gold_filter": True,
26	    },
27	}
28	
29	
30	def load_data(path, max_samples=8, gold_filter=False):
31	    instances = []
32	    with open(path) as f:
33	        for line in f:
34	            obj = json.loads(line)
35	            if gold_filter and len(obj["gold"]["entities"]) == 0:
36	                continue
37	            samples = obj["samples"][:max_samples]
38	            instances.append({
39	                "id": obj["id"],
40	                "gold": obj["gold"],
41	                "samples": samples,
42	                "greedy": obj["greedy"],
43	                "logprobs": obj.get("logprobs", [])[:max_samples],
44	            })
45	    return instances
46	
47	
48	def text_type_set(sample):
49	    """Entity set as {(text, type)} for MBR overlap computation."""
50	    return frozenset((e["text"], e["type"]) for e in sample.get("entities", []))
51	
52	
53	def span_set(sample):
54	    """Entity set as {(start, end, type)} for F1 evaluation."""
55	    return set((e["start"], e["end"], e["type"]) for e in sample.get("entities", []))
56	
57	
58	def jaccard(set_a, set_b):
59	    if len(set_a) == 0 and len(set_b) == 0:
60	        return 1.0
61	    union = len(set_a | set_b)
62	    if union == 0:
63	        return 1.0
6
…[truncated 1095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-20T18:25:10.642734+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts -maxdepth 2 -name \"*.py\" -type f | grep -E \"(run_|sampling|data_utils)\" | head -15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts -maxdepth 2 -name \"*.py\" -type f | grep -E \"(run_|sampling|data_utils)\" | head -15"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T18:25:10.642852+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_lsc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/a2_degen_regression/run_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_mrsc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_mvp_pilot.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/e2_ensemble/run_e2_ensemble.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_inverse_scaling/run_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-20T18:25:10.642978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T18:25:10.643143+00:00_

1	"""Multi-sample inference module for structured IE with vLLM + XGrammar constrained decoding.
2	
3	Provides VLLMSampler for batch sampling, prompt construction for UIE tasks,
4	and a full pipeline that produces SampledInstance dicts.
5	"""
6	
7	from __future__ import annotations
8	
9	import json
10	import os
11	from typing import Any
12	
13	
14	# ---------------------------------------------------------------------------
15	# UIE JSON schema for XGrammar constrained decoding
16	# ---------------------------------------------------------------------------
17	
18	UIE_JSON_SCHEMA: dict[str, Any] = {
19	    "type": "object",
20	    "properties": {
21	        "entities": {
22	            "type": "array",
23	            "items": {
24	                "type": "object",
25	                "properties": {
26	                    "text": {"type": "string"},
27	                    "type": {"type": "string"},
28	                    "start": {"type": "integer"},
29	                    "end": {"type": "integer"},
30	                },
31	                "required": ["text", "type", "start", "end"],
32	            },
33	        },
34	        "relations": {
35	            "type": "array",
36	            "items": {
37	                "type": "object",
38	                "properties": {
39	                    "head": {"type": "string"},
40	                    "tail": {"type": "string"},
41	                    "type": {"type": "string"},
42	                    "head_start": {"type": "integer"},
43	                    "head_end": {"type": "integer"},
44	                    "tail_start": {"type": "integer"},
45	                    "tail_end": {"type": "integer"},
46	                },
47	                "required": ["head", "tail", "type", "head_start", "head_end",
48	                             "tail_start", "tail_end"],
49	            },
50	        },
51	        "events": {
52	            "type": "array",
53	            "items": {
54	                "type": "object",
55	             
…[truncated 6000 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-20T18:25:10.643308+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-20T18:25:10.643447+00:00_

1	"""Data processing utilities for structured self-consistency IE experiments.
2	
3	Handles loading, converting, and splitting datasets into the unified UIE JSON format.
4	Supported datasets: SciERC (fully implemented), ACE05 (interface only).
5	"""
6	
7	from __future__ import annotations
8	
9	import json
10	import os
11	import random
12	from typing import Any, TypedDict
13	
14	
15	# ---------------------------------------------------------------------------
16	# Shared type definitions (UIE JSON format)
17	# ---------------------------------------------------------------------------
18	
19	class Entity(TypedDict):
20	    text: str
21	    type: str
22	    start: int
23	    end: int
24	
25	
26	class Relation(TypedDict):
27	    head: str
28	    tail: str
29	    type: str
30	    head_start: int
31	    head_end: int
32	    tail_start: int
33	    tail_end: int
34	
35	
36	class EventArgument(TypedDict):
37	    text: str
38	    role: str
39	    start: int
40	    end: int
41	
42	
43	class Trigger(TypedDict):
44	    text: str
45	    type: str
46	    start: int
47	    end: int
48	
49	
50	class Event(TypedDict):
51	    trigger: Trigger
52	    arguments: list[EventArgument]
53	
54	
55	class Extraction(TypedDict, total=False):
56	    entities: list[Entity]
57	    relations: list[Relation]
58	    events: list[Event]
59	
60	
61	class Instance(TypedDict, total=False):
62	    id: str
63	    text: str
64	    entities: list[Entity]
65	    relations: list[Relation]
66	    events: list[Event]
67	
68	
69	# ---------------------------------------------------------------------------
70	# SciERC
71	# ---------------------------------------------------------------------------
72	
73	def _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:
74	    """Compute (char_start, char_end) for each token when joined by single spaces."""
75	    offsets = []
76	    pos = 0
77	    for tok in tokens:
78	        offsets.append((pos, pos + len(tok)))
79	        pos += len(tok) + 1  # +1 for the space

…[truncated 2803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-20T18:25:10.643597+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*fewnerd*\" -type f | grep -v \".log\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*fewnerd*\" -type f | grep -v \".log\" | head -20"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-20T18:25:10.643720+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_031_fewnerd_t12_PREPARING_20260518T200412.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_llama_fewnerd_lora_RUNNING_20260519T010811.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_qwen25_32b_fewnerd_RUNNING_20260519T093547.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_b1_scd_fewnerd_curriculum_q_ALLOCATED_20260520T115455.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_qwen25_7b_fewnerd_ALLOCATED_20260519T075923.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_qwen25_14b_fewnerd_RUNNING_20260519T075736.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_028_fewnerd_5epoch_RUNNING_20260517T091210.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_llama_fewnerd_inference_RUNNING_20260519T031451.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_b1_scd_fewnerd_standard_QUEUED_20260520T115436.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_14b_inference_fewnerd_ALLOCATED_20260520T153640.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_031_fewnerd_t12_PENDING_20260519T002959.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_14b_inference_fewnerd_PENDING_20260520T174933.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_14b_inference_fewnerd_QUEUED_20260520T174945.json
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_b1_sc
…[truncated 916 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-20T18:25:10.643862+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fewnerd|FewNERD|coarse|fine.*type",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py",
  "output_mode": "content",
  "head_limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fewnerd|FewNERD|coarse|fine.*type",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py",
    "output_mode": "content",
    "head_limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-20T18:25:10.643978+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-20T18:25:10.644095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py",
  "offset": "150",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py",
    "offset": "150",
    "limit": "200"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-20T18:25:10.644257+00:00_

150	        text=text,
151	        entities=entities,
152	        relations=relations,
153	        events=[],
154	    )
155	
156	
157	def load_scierc(data_dir: str) -> dict[str, list[Instance]]:
158	    """Load SciERC dataset and convert to UIE JSON format.
159	
160	    Args:
161	        data_dir: Path to the SciERC directory containing {train,dev,test}.json.
162	
163	    Returns:
164	        Dict with keys "train", "dev", "test", each mapping to a list of Instance dicts.
165	    """
166	    splits: dict[str, list[Instance]] = {}
167	    for split in ("train", "dev", "test"):
168	        filepath = os.path.join(data_dir, f"{split}.json")
169	        instances: list[Instance] = []
170	        with open(filepath, "r", encoding="utf-8") as f:
171	            for line in f:
172	                line = line.strip()
173	                if not line:
174	                    continue
175	                doc = json.loads(line)
176	                doc_key = doc["doc_key"]
177	                sentences = doc["sentences"]
178	                ner_all = doc.get("ner", [[] for _ in sentences])
179	                rel_all = doc.get("relations", [[] for _ in sentences])
180	
181	                global_offset = 0
182	                for sent_idx, tokens in enumerate(sentences):
183	                    ner_spans = ner_all[sent_idx] if sent_idx < len(ner_all) else []
184	                    rel_spans = rel_all[sent_idx] if sent_idx < len(rel_all) else []
185	                    inst = _parse_scierc_sentence(
186	                        doc_key, sent_idx, tokens, ner_spans, rel_spans, global_offset,
187	                    )
188	                    instances.append(inst)
189	                    global_offset += len(tokens)
190	
191	        splits[split] = instances
192	    return splits
193	
194	
195	# ---------------------------------------------------------------------------
196	# ACE05 (interface only)
197	# ---------------------------------------------------------------------------
19
…[truncated 3364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-20T18:25:10.644408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/IDEA_BRIEF.md",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/IDEA_BRIEF.md",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-20T18:25:10.644595+00:00_

1	# Idea Brief: When Does Test-Time Scaling Help Structured Prediction? Adaptive Structural Self-Consistency with Learned Aggregation
2	
3	
4	- **Idea ID**: `idea_010`
5	- **Created**: 2026-05-14
6	- **Approved**: 2026-05-14
7	- **Source**: foreign:be-idea-gen-0509-6
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 via ARR May 2026 (submission: May 25, 2026; commitment: Aug 2, 2026; notification: Aug 20, 2026; conference: Oct 24-29, Budapest), Backup: ARR August 2026 (submission: Aug 3, 2026) → EACL 2027 or NAACL 2027
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Information Extraction.
14	
15	Direction: Structured information extraction — named entity recognition, relation extraction, event extraction, document-level IE, end-to-end extraction pipelines. Both LLM-based and non-LLM approaches welcome. In-scope: schema-guided extraction, zero-shot/few-shot IE, cross-document extraction, multimodal IE (text + layout + images), temporal/causal relation extraction.
16	
17	Contribution type: METHOD ONLY. New extraction architectures, training strategies, or inference algorithms. Not a new dataset or annotation guideline.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. IE work is typically lightweight — most experiments are fine-tuning or in-context learning.
21	2. Time: ≤16 days. Use existing IE frameworks (GoLLIE, UniNER, USM) or build on open LLMs with structured output.
22	3. Eval: ACE05, SciERC, TACRED/TACREV, DocRED, MAVEN, Few-NERD, WikiEvents, RAMS.
23	
24	Look for: schema-guided extraction that generalizes across domains, efficient document-level IE beyond sliding windows, extraction with faithful provenance/citation, structured extraction from semi-structured sources (tables, forms, code). Avoid: basic NER fine-tuning, prompt-only extraction without architectural insight.
25	
26	Tag: direction=information_extraction, contribution_type=method. target_venues=["EMNLP
…[truncated 22430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-20T18:25:10.644753+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ | head -30"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-20T18:25:10.644906+00:00_

total 1040
drwxr-xr-x  13 ubuntu ubuntu   4096 May 20 18:15 .
drwxrwxr-x   4 ubuntu ubuntu   4096 May 14 04:20 ..
drwxr-xr-x   3 ubuntu ubuntu   4096 May 14 04:20 .claude
drwxr-xr-x   6 ubuntu ubuntu   4096 May 15 02:23 .venv
-rw-r--r--   1 ubuntu ubuntu  14175 May 20 18:17 AGENTS.md
-rw-r--r--   1 ubuntu ubuntu      0 May 14 04:23 ROADMAP.lock
-rw-------   1 ubuntu ubuntu   3935 May 20 18:14 ROADMAP.md
-rw-r--r--   1 ubuntu ubuntu     90 May 20 14:32 _last_visual_review.json
-rw-r--r--   1 ubuntu ubuntu   7234 May 18 13:38 analysis_r21_q1_alignment.py
drwxr-xr-x 135 ubuntu ubuntu  20480 May 20 17:59 artifacts
-rw-r--r--   1 ubuntu ubuntu  22309 May 20 10:07 b2_entity_verifier.py
drwxr-xr-x   2 ubuntu ubuntu 110592 May 20 18:15 checkpoints
drwxr-xr-x   2 ubuntu ubuntu   4096 May 20 12:02 code
-rw-r--r--   1 ubuntu ubuntu      0 May 16 03:03 constraints.lock
-rw-------   1 ubuntu ubuntu    457 May 16 03:03 constraints.yaml
-rw-r--r--   1 ubuntu ubuntu      0 May 14 04:23 decisions.lock
-rw-------   1 ubuntu ubuntu 195128 May 20 18:14 decisions.yaml
drwxr-xr-x   4 ubuntu ubuntu   4096 May 15 05:25 docs
-rwxr-xr-x   1 ubuntu ubuntu      0 May 14 09:33 dream_registry.lock
-rw-------   1 ubuntu ubuntu   8728 May 16 22:54 dream_registry.yaml
-rw-r--r--   1 ubuntu ubuntu   8656 May 16 22:54 dream_registry.yaml.bak
-rw-r--r--   1 ubuntu ubuntu  14268 May 20 09:47 e1_signal_routing.py
-rw-r--r--   1 ubuntu ubuntu      0 May 14 11:49 experiment_plan.lock
-rw-------   1 ubuntu ubuntu  16334 May 19 22:51 experiment_plan.yaml
drwxr-xr-x   3 ubuntu ubuntu   4096 May 14 13:35 figures
-rw-r--r--   1 ubuntu ubuntu      0 May 14 15:47 literature_map.lock
-rw-------   1 ubuntu ubuntu  43680 May 14 19:51 literature_map.yaml
drwxr-xr-x   4 ubuntu ubuntu   4096 May 14 04:25 logs
-rw-r--r--   1 ubuntu ubuntu   5708 May 20 17:33 memory.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-20T18:25:10.645169+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_mvp_pilot.py",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_mvp_pilot.py",
    "limit": "120"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-20T18:25:10.645365+00:00_

1	"""MVP pilot experiment script for structured self-consistency IE.
2	
3	Integrates data loading, vLLM sampling, consistency scoring, and evaluation
4	into a single CLI-driven pipeline. Outputs a verdict (PASS/MARGINAL/FAIL)
5	based on the correlation between structural consistency and per-instance F1.
6	"""
7	
8	from __future__ import annotations
9	
10	import argparse
11	import json
12	import os
13	import random
14	import sys
15	
16	import numpy as np
17	
18	from data_utils import load_scierc, load_ace05
19	from sampling import (
20	    VLLMSampler,
21	    run_sampling_pipeline,
22	    save_sampled_results,
23	    load_sampled_results,
24	    realign_spans,
25	    SCIERC_SCHEMA_HINT,
26	)
27	from consistency import compute_all_consistency_scores
28	from evaluation import (
29	    per_instance_f1,
30	    compute_ner_f1,
31	    compute_re_f1,
32	    compute_eae_f1,
33	    spearman_correlation,
34	    kendall_correlation,
35	    compute_auroc,
36	    compute_sample_f1_distribution,
37	)
38	
39	
40	def parse_args() -> argparse.Namespace:
41	    """Parse command-line arguments."""
42	    p = argparse.ArgumentParser(description="MVP pilot for structured self-consistency IE")
43	    p.add_argument("--model_path", type=str, required=True, help="Path to the fine-tuned model")
44	    p.add_argument("--data_dir", type=str, required=True, help="Dataset directory (SciERC or ACE05)")
45	    p.add_argument("--dataset", type=str, default="scierc", choices=["scierc", "ace05"],
46	                   help="Dataset name (default: scierc)")
47	    p.add_argument("--subtask", type=str, default="ner", choices=["ner", "re", "eae", "joint"],
48	                   help="Subtask (default: ner)")
49	    p.add_argument("--schema_hint", type=str, default="",
50	                   help="Schema hint string (entity/relation types). Auto-set for scierc if empty")
51	    p.add_argument("--use_train_format", type=lambda x: x.lower() != "false", default=True,
52	                   help="Use train-ali
…[truncated 4435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-20T18:25:10.645534+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"requirements*.txt\" -o -name \"setup.py\" -o -name \"pyproject.toml\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"requirements*.txt\" -o -name \"setup.py\" -o -name \"pyproject.toml\""
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-20T18:25:10.645657+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/numpy/_core/tests/examples/limited_api/setup.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/numpy/_core/tests/examples/cython/setup.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-20T18:25:10.645783+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts -name \"*.py\" -type f -path \"*/exp*/data/*\" | head -15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts -name \"*.py\" -type f -path \"*/exp*/data/*\" | head -15"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-20T18:25:10.645899+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_lsc_latent_sc/data/run_lsc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_016_v2/data/exp_016_v2_ensemble.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_e1v2_signal_routing/data/e1v2_signal_routing.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_009_capability_stratification/data/exp009_stratification_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_asb_adaptive_budget/data/run_asb.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-20T18:25:10.646025+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "entity.*type|coarse.*type|fine.*type|ENTITY_TYPES|SCHEMA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
  "output_mode": "content",
  "head_limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "tool_args": {
    "pattern": "entity.*type|coarse.*type|fine.*type|ENTITY_TYPES|SCHEMA",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
    "output_mode": "content",
    "head_limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-20T18:25:10.646155+00:00_

18:UIE_JSON_SCHEMA: dict[str, Any] = {
169:        guided_params = StructuredOutputsParams(json=UIE_JSON_SCHEMA) if use_grammar else None
231:    "Extract all relations (head entity, relation type, tail entity) from the following text. "
262:SCIERC_SCHEMA_HINT = (
274:        schema_hint: Optional schema description (e.g. entity type list).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-20T18:25:10.646286+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
  "offset": "200",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
    "offset": "200",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-20T18:25:10.646432+00:00_

200	        if collect_logprobs:
201	            return results, logprobs_data
202	        return results
203	
204	
205	# ---------------------------------------------------------------------------
206	# Prompt construction
207	# ---------------------------------------------------------------------------
208	
209	_NER_TEMPLATE = (
210	    "Extract named entities from the following text. "
211	    "Output a JSON object with the fields: entities, relations, events.\n\n"
212	    "Text: {text}\n"
213	    "{schema_line}"
214	    "\nOutput format: "
215	    '{{"entities": [{{"text": "...", "type": "...", "start": &lt;int>, "end": &lt;int>}}], '
216	    '"relations": [], "events": []}}'
217	)
218	
219	_EAE_TEMPLATE = (
220	    "Extract events (triggers and arguments) from the following text. "
221	    "Output a JSON object with the fields: entities, relations, events.\n\n"
222	    "Text: {text}\n"
223	    "{schema_line}"
224	    "\nOutput format: "
225	    '{{"entities": [], "relations": [], '
226	    '"events": [{{"trigger": {{"text": "...", "type": "...", "start": &lt;int>, "end": &lt;int>}}, '
227	    '"arguments": [{{"text": "...", "role": "...", "start": &lt;int>, "end": &lt;int>}}]}}]}}'
228	)
229	
230	_RE_TEMPLATE = (
231	    "Extract all relations (head entity, relation type, tail entity) from the following text. "
232	    "Output a JSON object with the fields: entities, relations, events.\n\n"
233	    "Text: {text}\n"
234	    "{schema_line}"
235	    "\nOutput format: "
236	    '{{"entities": [], '
237	    '"relations": [{{"head": "...", "tail": "...", "type": "...", '
238	    '"head_start": &lt;int>, "head_end": &lt;int>, "tail_start": &lt;int>, "tail_end": &lt;int>}}], '
239	    '"events": []}}'
240	)
241	
242	_FULL_TEMPLATE = (
243	    "Extract all structured information (entities, relations, events) from the following text. "
244	    "Output a JSON object with the fields: entities, relations, events.\n\n"
245	    "Text: {text}\n"
246	    "{schema_line}"
247	    "\nOutput:"
248	)
249	
250	_T
…[truncated 3872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-20T18:25:10.646594+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"SCIERC_SCHEMA_HINT\\|person\\|organization\\|location\\|building\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"SCIERC_SCHEMA_HINT\\|person\\|organization\\|location\\|building\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py | head -30"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-20T18:25:10.646723+00:00_

262:SCIERC_SCHEMA_HINT = (

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-20T18:25:10.646840+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/ 2>/dev/null || echo \"data dir not found\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/ 2>/dev/null || echo \"data dir not found\""
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-20T18:25:10.646948+00:00_

total 60
drwxr-xr-x   2 ubuntu ubuntu  4096 May 14 21:47 .
drwxr-xr-x 135 ubuntu ubuntu 20480 May 20 17:59 ..
-rw-r--r--   1 ubuntu ubuntu 17964 May 14 21:47 bootstrap_ci_summary.json
-rw-r--r--   1 ubuntu ubuntu  9001 May 14 21:16 qwen_scierc_3seed_em_voting.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-20T18:25:10.647065+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.jsonl\" -type f | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.jsonl\" -type f | head -10"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-20T18:25:10.647199+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/ralph_loop_timeline.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_exp_e_theta_v1_logreg_20260520T154053.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_code_exp_028_multigpu_switch_20260517T122517.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_dm_oc_4206a99c0a8b5482c9bbd8f23ccc03f0_briefer.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_code_dgs_persistence_fix_20260518T164426.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_exp_010_selection_curves_20260514T144948.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/cron_hook_exp_029b.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_analysis_4b_selection_pipeline_20260515T200110.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_exp_conll_s123_cuda2_20260518T094904.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_code_llama_conll_inference_20260518T181743.jsonl

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-20T18:25:10.647354+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "head -20 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/qwen_scierc_3seed_em_voting.json 2>/dev/null | jq . | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "head -20 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data/qwen_scierc_3seed_em_voting.json 2>/dev/null | jq . | head -80"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-20T18:25:10.647465+00:00_

jq: parse error: Unfinished JSON term at EOF at line 21, column 0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-20T18:25:10.647580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-20T18:25:10.647711+00:00_

1	# Memory
2	
3	## exp_qwen25_72b_fewshot 完整结果（2026-05-20）
4	
5	实验于 2026-05-20 08:47 完成。模型：Qwen2.5-72B-Instruct-AWQ, 3-shot, N=8 samples, seed=42。
6	
7	### ZS vs FS 完整对比表
8	
9	| Dataset  | Regime | N inst | Degen% | LP ρ   | SJ ρ  | FK ρ  | VC ρ  | EM ρ  | Greedy F1 | Oracle F1 | LP-wt F1 | LP Δ (pp) | p-value |
10	|----------|--------|--------|--------|--------|-------|-------|-------|-------|-----------|-----------|----------|-----------|---------|
11	| SciERC   | ZS     | 529    | 21.0%  | 0.081  | 0.217 | 0.227 | 0.277 | 0.181 | 0.399     | 0.549     | 0.415    | +1.53     | 0.008** |
12	| SciERC   | FS     | 529    | 16.6%  | 0.060  | 0.293 | 0.301 | 0.258 | 0.205 | 0.461     | 0.604     | 0.461    | -0.08     | 0.544   |
13	| CoNLL    | ZS     | 2756   | 67.7%  | -0.002 | 0.304 | 0.302 | 0.297 | 0.281 | 0.712     | 0.765     | 0.708    | -0.37     | n/a     |
14	| CoNLL    | FS     | 2756   | 70.0%  | 0.106  | 0.442 | 0.451 | 0.426 | 0.403 | 0.745     | 0.796     | 0.745    | +0.03     | 0.417   |
15	| FewNERD  | ZS     | 32565  | 46.2%  | 0.119  | 0.345 | 0.321 | 0.416 | 0.303 | 0.628     | 0.707     | 0.626    | -0.20     | n/a     |
16	| FewNERD  | FS     | 32565  | 45.2%  | 0.161  | 0.345 | 0.327 | 0.410 | 0.302 | 0.619     | 0.702     | 0.619    | +0.02     | 0.401   |
17	
18	### Dual-gating hypothesis 评估
19	
20	Dual-gating 在 FT+ZS regime 内成立（6/6 条件一致）。FS regime 引入独立失效因素（LP 退化），不构成对 dual-gating 的挑战。
21	
22	### Error Correlation 分析
23	"Demonstration-induced error correlation" 假说缺乏实证支持（FS Jaccard ≈ ZS，CoNLL FS entropy 反而更高）。替代解释：LP signal 在 FS 下区分力退化是 construction 失效的直接原因。
24	
25	## F1 Scaling Law 写作约束（Director 2026-05-20）
26	
27	1. 不报 c 均值 — 分数据集：SciERC c≈0.35, FewNERD c≈0.61
28	2. CoNLL 只报 a 和 b，不报 c（c_se 太大）
29	3. 这是 oracle ceiling scaling，不是 achievable
30	4. LLaMA/FewNERD 仅 4 点拟合 → appendix 注明过拟合风险
31	5. N=1 低于 greedy 需解释（T=1 采样噪声 vs T=0 确定性）
32	
33	## CPU 分析实验汇总（2026-05-20）
34	
35	### E2 Mixture-of-Signals Ensemble
36	- Selection: 5-signal ensemble +0.
…[truncated 2880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-20T18:25:10.647867+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 1 -name \"*.py\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 1 -name \"*.py\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-20T18:25:10.647982+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/e1_signal_routing.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/analysis_r21_q1_alignment.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/b2_entity_verifier.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-20T18:25:10.648101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
  "offset": "150",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
    "offset": "150",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-20T18:25:10.648262+00:00_

150	        return 0.0
151	
152	    # Group by entity type
153	    types: set[str] = set()
154	    groups_a: dict[str, list[Entity]] = {}
155	    groups_b: dict[str, list[Entity]] = {}
156	
157	    for e in entities_a:
158	        t = e["type"]
159	        types.add(t)
160	        groups_a.setdefault(t, []).append(e)
161	    for e in entities_b:
162	        t = e["type"]
163	        types.add(t)
164	        groups_b.setdefault(t, []).append(e)
165	
166	    total_score = 0.0
167	    total_weight = 0
168	
169	    for t in types:
170	        ga = groups_a.get(t, [])
171	        gb = groups_b.get(t, [])
172	        denom = max(len(ga), len(gb))
173	        if denom == 0:
174	            continue
175	
176	        total_weight += denom
177	
178	        if not ga or not gb:
179	            # One side empty — all unmatched, contributes 0
180	            continue
181	
182	        # Cost matrix for Hungarian (we maximize similarity, so negate for min-cost)
183	        cost = np.zeros((len(ga), len(gb)), dtype=np.float64)
184	        for i, ea in enumerate(ga):
185	            for j, eb in enumerate(gb):
186	                cost[i, j] = _span_soft_jaccard(ea["start"], ea["end"],
187	                                                 eb["start"], eb["end"])
188	
189	        row_ind, col_ind = linear_sum_assignment(-cost)  # negate to maximize
190	        matched_sim = cost[row_ind, col_ind].sum()
191	        # Normalize by the larger set size to penalize unmatched spans
192	        total_score += matched_sim
193	
194	    if total_weight == 0:
195	        return 1.0
196	    return total_score / total_weight
197	
198	
199	def _re_soft_jaccard_pair(relations_a: list[dict], relations_b: list[dict]) -> float:
200	    """Soft Jaccard for relation extraction via Hungarian matching.
201	
202	    Relation similarity = head_span_sj * tail_span_sj * type_match.
203	    """
204	    if not relations_a and not relations_b:
205	        return 1.0
206	    if not relations_a or not relations_b:
2
…[truncated 1848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-20T18:25:10.648533+00:00_

Excellent! Now I have all the information I need. Let me create the comprehensive report.

## Project Exploration Summary

I've conducted a thorough exploration of the NER experiment project at `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/`. Here are the findings:

### 1. PROJECT STRUCTURE

**Core Directories:**
- `/artifacts/` — Main experimental code and analysis scripts
- `/code/` — Utility and analysis code
- `/checkpoints/` — Experiment tracking files (JSON checkpoint records)
- `/docs/` — Project documentation (IDEA_BRIEF.md, paper sections)
- `/figures/` — Visualization scripts and data
- `/logs/` — Worker logs and chat histories

**Key Base Modules:**
- `/artifacts/sampling.py` — Multi-sample inference with vLLM + XGrammar constrained decoding
- `/artifacts/data_utils.py` — Dataset loading and unified UIE JSON format conversion
- `/artifacts/consistency.py` — Consistency metrics (Fleiss' Kappa, soft Jaccard, oracle best-of-N)
- `/artifacts/entity_construction.py` — Entity-level majority vote aggregation
- `/artifacts/evaluation.py` — Strict-match NER/RE evaluation and correlation analysis
- `/code/zeroshot_prompts.py` — Zero-shot NER prompt templates for multiple datasets

### 2. NER ENTITY TYPES & SCHEMA DEFINITIONS

**FewNERD (Coarse-Grained Types)** — 8 types:
```python
DATASET_ENTITY_TYPES["fewnerd"] = {
    "types": ["person", "organization", "location", "building", "art", "product", "event", "other"],
    "descriptions": {
        "person": "Person names",
        "organization": "Organizations, companies, teams",
        "location": "Geographic locations, countries, cities",
        "building": "Buildings, facilities, landmarks",
        "art": "Artworks, songs, films, books",
        "product": "Commercial products, software, vehicles",
        "event": "Events, competitions, wars, festivals",
        "other": "Other named entities not fitting the above categories",
    }
}
```

**CoNLL2003:** ["PER", "ORG", "LOC",
…[truncated 10669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Agent",
  "elapsed_ms": 11
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-20T18:25:10.648734+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/zeroshot_prompts.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/zeroshot_prompts.py"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-20T18:25:10.648930+00:00_

1	"""Zero-shot NER prompt templates for Qwen2.5-72B baseline evaluation.
2	
3	Output format is compatible with the existing pipeline (sampling.py):
4	  {"entities": [{"text": "...", "type": "...", "start": &lt;int>, "end": &lt;int>}],
5	   "relations": [], "events": []}
6	"""
7	
8	# ---------------------------------------------------------------------------
9	# Entity type definitions per dataset
10	# ---------------------------------------------------------------------------
11	
12	DATASET_ENTITY_TYPES = {
13	    "conll2003": {
14	        "types": ["PER", "ORG", "LOC", "MISC"],
15	        "descriptions": {
16	            "PER": "Person names (e.g., John Smith, Obama)",
17	            "ORG": "Organizations (e.g., Google, United Nations)",
18	            "LOC": "Locations (e.g., France, Mount Everest)",
19	            "MISC": "Miscellaneous named entities not fitting PER/ORG/LOC (e.g., English, World Cup)",
20	        },
21	    },
22	    "fewnerd": {
23	        "types": ["person", "organization", "location", "building", "art", "product", "event", "other"],
24	        "descriptions": {
25	            "person": "Person names",
26	            "organization": "Organizations, companies, teams",
27	            "location": "Geographic locations, countries, cities",
28	            "building": "Buildings, facilities, landmarks",
29	            "art": "Artworks, songs, films, books",
30	            "product": "Commercial products, software, vehicles",
31	            "event": "Events, competitions, wars, festivals",
32	            "other": "Other named entities not fitting the above categories",
33	        },
34	    },
35	    "scierc": {
36	        "types": ["Generic", "Material", "Method", "Metric", "OtherScientificTerm", "Task"],
37	        "descriptions": {
38	            "Generic": "Generic references to scientific concepts (coreference)",
39	            "Material": "Data, datasets, corpora, resources",
40	            "Method": "Algorithms, models, systems, tools",
41	           
…[truncated 5191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-20T18:25:10.649096+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-20T18:25:10.649312+00:00_

1	"""Data processing utilities for structured self-consistency IE experiments.
2	
3	Handles loading, converting, and splitting datasets into the unified UIE JSON format.
4	Supported datasets: SciERC (fully implemented), ACE05 (interface only).
5	"""
6	
7	from __future__ import annotations
8	
9	import json
10	import os
11	import random
12	from typing import Any, TypedDict
13	
14	
15	# ---------------------------------------------------------------------------
16	# Shared type definitions (UIE JSON format)
17	# ---------------------------------------------------------------------------
18	
19	class Entity(TypedDict):
20	    text: str
21	    type: str
22	    start: int
23	    end: int
24	
25	
26	class Relation(TypedDict):
27	    head: str
28	    tail: str
29	    type: str
30	    head_start: int
31	    head_end: int
32	    tail_start: int
33	    tail_end: int
34	
35	
36	class EventArgument(TypedDict):
37	    text: str
38	    role: str
39	    start: int
40	    end: int
41	
42	
43	class Trigger(TypedDict):
44	    text: str
45	    type: str
46	    start: int
47	    end: int
48	
49	
50	class Event(TypedDict):
51	    trigger: Trigger
52	    arguments: list[EventArgument]
53	
54	
55	class Extraction(TypedDict, total=False):
56	    entities: list[Entity]
57	    relations: list[Relation]
58	    events: list[Event]
59	
60	
61	class Instance(TypedDict, total=False):
62	    id: str
63	    text: str
64	    entities: list[Entity]
65	    relations: list[Relation]
66	    events: list[Event]
67	
68	
69	# ---------------------------------------------------------------------------
70	# SciERC
71	# ---------------------------------------------------------------------------
72	
73	def _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:
74	    """Compute (char_start, char_end) for each token when joined by single spaces."""
75	    offsets = []
76	    pos = 0
77	    for tok in tokens:
78	        offsets.append((pos, pos + len(tok)))
79	        pos += len(tok) + 1  # +1 for the space

…[truncated 8145 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-20T18:25:10.649459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/entity_construction.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/entity_construction.py"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-20T18:25:10.649801+00:00_

1	"""Entity-Level Majority Vote Construction for NER and RE.
2	
3	Core hypothesis: the correct analogy for self-consistency on structured output
4	is entity-level majority vote construction, not instance-level best-of-N selection.
5	"""
6	
7	import json
8	import math
9	import os
10	import sys
11	import numpy as np
12	from collections import defaultdict
13	
14	# ---------------------------------------------------------------------------
15	# Metrics (mirroring unified_metrics.py)
16	# ---------------------------------------------------------------------------
17	
18	def compute_prf(pred_set, gold_set):
19	    if not gold_set and not pred_set:
20	        return 1.0, 1.0, 1.0
21	    if not pred_set:
22	        return 0.0, 0.0, 0.0
23	    if not gold_set:
24	        return 0.0, 0.0, 0.0
25	    tp = len(pred_set & gold_set)
26	    if tp == 0:
27	        return 0.0, 0.0, 0.0
28	    p = tp / len(pred_set)
29	    r = tp / len(gold_set)
30	    f = 2 * p * r / (p + r)
31	    return p, r, f
32	
33	
34	def entity_set(entities):
35	    return {(e["start"], e["end"], e["type"]) for e in entities}
36	
37	
38	def relation_set(relations):
39	    return {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
40	            for r in relations}
41	
42	
43	# ---------------------------------------------------------------------------
44	# Construction
45	# ---------------------------------------------------------------------------
46	
47	def entity_majority_vote(samples, threshold, weights=None):
48	    """Collect entities across N samples, keep those above threshold."""
49	    entity_counts = defaultdict(float)
50	    N = len(samples)
51	    for i, sample in enumerate(samples):
52	        w = weights[i] if weights is not None else 1.0
53	        for e in sample.get("entities", []):
54	            key = (e["start"], e["end"], e["type"])
55	            entity_counts[key] += w
56	
57	    total_weight = sum(weights) if weights is not None else N
58	    constructed = set
…[truncated 18967 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-20T18:25:10.649970+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/evaluation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/evaluation.py"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-20T18:25:10.650233+00:00_

1	"""Evaluation module for structured self-consistency IE experiments.
2	
3	Provides strict-match NER/EAE evaluation, per-instance F1 computation,
4	correlation analysis, and summary report generation.
5	"""
6	
7	from __future__ import annotations
8	
9	import statistics
10	from typing import Any
11	
12	from scipy.stats import kendalltau, spearmanr
13	
14	
15	# ---------------------------------------------------------------------------
16	# NER evaluation (strict match)
17	# ---------------------------------------------------------------------------
18	
19	def entity_strict_match(
20	    pred_entities: list[dict],
21	    gold_entities: list[dict],
22	) -> tuple[int, int, int]:
23	    """Compute strict entity match counts.
24	
25	    Strict match requires exact span (start, end) AND exact type.
26	
27	    Args:
28	        pred_entities: Predicted entity dicts with keys text, type, start, end.
29	        gold_entities: Gold entity dicts with the same schema.
30	
31	    Returns:
32	        (tp, fp, fn) counts.
33	    """
34	    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
35	    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
36	    tp = len(pred_set & gold_set)
37	    fp = len(pred_set - gold_set)
38	    fn = len(gold_set - pred_set)
39	    return tp, fp, fn
40	
41	
42	def compute_ner_f1(
43	    predictions: list[dict],
44	    golds: list[dict],
45	) -> dict[str, float]:
46	    """Compute micro-averaged NER precision, recall, and F1.
47	
48	    Args:
49	        predictions: List of Extraction dicts (one per instance).
50	        golds: List of Extraction dicts (one per instance), aligned with predictions.
51	
52	    Returns:
53	        Dict with keys "precision", "recall", "f1".
54	    """
55	    total_tp = total_fp = total_fn = 0
56	    for pred, gold in zip(predictions, golds):
57	        tp, fp, fn = entity_strict_match(
58	            pred.get("entities", []),
59	            gold.get("entities", []),
60	        )
61	  
…[truncated 14026 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-20T18:25:10.650433+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/fewnerd/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/fewnerd/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-20T18:25:10.650562+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-20T18:25:10.650678+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenRouter GPT-5.5 pricing per million tokens 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenRouter GPT-5.5 pricing per million tokens 2026"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-20T18:25:10.650814+00:00_

Web search results for query: "OpenRouter GPT-5.5 pricing per million tokens 2026"

Links: [{"title":"GPT-5.5 - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/openai/gpt-5.5"},{"title":"GPT-5.5 Price Increase: What It Actually Costs | OpenRouter","url":"https://openrouter.ai/announcements/gpt55-cost-analysis"},{"title":"GPT-5.5 Pro - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/openai/gpt-5.5-pro"},{"title":"GPT-5.2 - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/openai/gpt-5.2"},{"title":"GPT-5.5 may burn fewer tokens, but it always burns more cash","url":"https://www.theregister.com/ai-and-ml/2026/05/08/gpt-55-may-burn-fewer-tokens-but-it-always-burns-more-cash/5237498"},{"title":"Pricing | OpenRouter","url":"https://openrouter.ai/pricing"},{"title":"GPT-5 - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/openai/gpt-5"},{"title":"GPT-5 Mini - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/openai/gpt-5-mini"},{"title":"GPT-5.4 - API Pricing & Benchmarks | OpenRouter","url":"https://openrouter.ai/openai/gpt-5.4"},{"title":"GPT-5.5 - API Pricing & Providers | OpenRouter","url":"https://openrouter.ai/openai/gpt-5.5-20260423"}]

Based on the search results, here's the OpenRouter GPT-5.5 pricing for 2026:

**GPT-5.5 Standard:**
Input price is $5 per 1M tokens and output price is $30 per 1M tokens.

**GPT-5.5 Pro:**
Input price is $30 per 1M tokens and output price is $180 per 1M tokens.

For context, GPT-5.5 was released on April 24, 2026, and it launched with a 2x price increase over GPT-5.4, with input tokens increasing from $2.50/M to $5.00/M and output tokens from $15/M to $30/M.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-20T18:25:10.650988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
    "limit": "120"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-20T18:25:10.651178+00:00_

1	"""Multi-sample inference module for structured IE with vLLM + XGrammar constrained decoding.
2	
3	Provides VLLMSampler for batch sampling, prompt construction for UIE tasks,
4	and a full pipeline that produces SampledInstance dicts.
5	"""
6	
7	from __future__ import annotations
8	
9	import json
10	import os
11	from typing import Any
12	
13	
14	# ---------------------------------------------------------------------------
15	# UIE JSON schema for XGrammar constrained decoding
16	# ---------------------------------------------------------------------------
17	
18	UIE_JSON_SCHEMA: dict[str, Any] = {
19	    "type": "object",
20	    "properties": {
21	        "entities": {
22	            "type": "array",
23	            "items": {
24	                "type": "object",
25	                "properties": {
26	                    "text": {"type": "string"},
27	                    "type": {"type": "string"},
28	                    "start": {"type": "integer"},
29	                    "end": {"type": "integer"},
30	                },
31	                "required": ["text", "type", "start", "end"],
32	            },
33	        },
34	        "relations": {
35	            "type": "array",
36	            "items": {
37	                "type": "object",
38	                "properties": {
39	                    "head": {"type": "string"},
40	                    "tail": {"type": "string"},
41	                    "type": {"type": "string"},
42	                    "head_start": {"type": "integer"},
43	                    "head_end": {"type": "integer"},
44	                    "tail_start": {"type": "integer"},
45	                    "tail_end": {"type": "integer"},
46	                },
47	                "required": ["head", "tail", "type", "head_start", "head_end",
48	                             "tail_start", "tail_end"],
49	            },
50	        },
51	        "events": {
52	            "type": "array",
53	            "items": {
54	                "type": "object",
55	             
…[truncated 2628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-20T18:25:10.651343+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/ 2>/dev/null || echo \"NO_DIR\"",
  "description": "Check experiments directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/ 2>/dev/null || echo \"NO_DIR\"",
    "description": "Check experiments directory"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-20T18:25:10.651469+00:00_

asb
distill_verifier
e_theta
esj
het_temp
humaneval_sc
lsc
mrsc

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-20T18:25:10.651586+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
  "offset": "280",
  "limit": "130"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py",
    "offset": "280",
    "limit": "130"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-20T18:25:10.651748+00:00_

280	    if use_train_format:
281	        schema_line = f"{schema_hint}\n" if schema_hint else ""
282	        return _TRAIN_ALIGNED_TEMPLATE.format(text=text, schema_line=schema_line)
283	
284	    schema_line = f"Schema: {schema_hint}\n" if schema_hint else ""
285	
286	    if subtask == "ner":
287	        template = _NER_TEMPLATE
288	    elif subtask == "re":
289	        template = _RE_TEMPLATE
290	    elif subtask == "eae":
291	        template = _EAE_TEMPLATE
292	    elif subtask == "full":
293	        template = _FULL_TEMPLATE
294	    else:
295	        raise ValueError(f"subtask must be 'ner', 're', 'eae', or 'full', got '{subtask}'")
296	
297	    return template.format(text=text, schema_line=schema_line)
298	
299	
300	# ---------------------------------------------------------------------------
301	# Output parsing
302	# ---------------------------------------------------------------------------
303	
304	def parse_extraction_output(raw_output: str) -> dict[str, Any]:
305	    """Parse a model output string into an Extraction dict.
306	
307	    Handles JSON parsing (XGrammar guarantees valid JSON, but we still guard),
308	    field validation, and type coercion for start/end.
309	
310	    Args:
311	        raw_output: Raw model completion text.
312	
313	    Returns:
314	        Extraction dict with keys entities, relations, events.
315	    """
316	    raw = raw_output.strip()
317	    try:
318	        data = json.loads(raw)
319	    except json.JSONDecodeError:
320	        # Attempt to extract the first JSON object from the string
321	        start = raw.find("{")
322	        end = raw.rfind("}")
323	        if start != -1 and end != -1 and end > start:
324	            try:
325	                data = json.loads(raw[start:end + 1])
326	            except json.JSONDecodeError:
327	                return dict(_EMPTY_EXTRACTION)
328	        else:
329	            return dict(_EMPTY_EXTRACTION)
330	
331	    if not isinstance(data, dict):
332	        return dict(_EMPTY_EXTR
…[truncated 2696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-20T18:25:10.652001+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc",
  "description": "Create frontier_sc experiment directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc",
    "description": "Create frontier_sc experiment directory"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-20T18:25:10.652154+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-20T18:25:10.652396+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
  "content": "#!/usr/bin/env python3\n\"\"\"Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).\n\nTests whether the correlation-selection gap in structured self-consistency\npersists with frontier models (GPT-5.5, Claude Opus 4.6), validating it\nas a fundamental limitation rather than a capability issue.\n\nCPU-only — all computation is via API calls through OpenRouter.\n\nUsage:\n    export OPENROUTER_API_KEY=\"[REDACTED]\"\n    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n    python run_frontier_sc.py --from-hf  # load from HuggingFace\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nMODELS = {\n    \"gpt-5.5\": \"openai/gpt-5.5\",\n    \"claude-opus-4.6\": \"anthropic/claude-opus-4.6\",\n}\n\nAPI_BASE_URL = \"http://47.94.22.126/v1\"\n\nENTITY_TYPES = {\n    \"person\": \"Person names\",\n    \"organization\": \"Organizations, companies, teams\",\n    \"location\": \"Geographic locations, countries, cities\",\n    \"building\": \"Buildings, facilities, landmarks\",\n    \"art\": \"Artworks, songs, films, books\",\n    \"product\": \"Commercial products, software, vehicles\",\n    \"event\": \"Events, competitions, wars, festivals\",\n    \"other\": \"Other named entities not fitting the above categories\",\n}\n\nVALID_TYPES = set(ENTITY_TYPES.keys())\n\nMV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data Loading\n# ---------------------------------------------------------------------------\n\ndef _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:\n    offsets = []\n    pos = 0\n    for tok in tokens:\n        offsets.append((pos, pos + len(tok)))\n        pos += len(tok) + 1\n    return offsets\n\n\ndef _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:\n    \"\"\"Convert BIO-tagged tokens to entity spans with char offsets.\"\"\"\n    offsets = _token_offsets(tokens)\n    entities = []\n    current = None\n\n    for i, tag_id in enumerate(tag_ids):\n        tag = tag_names[tag_id]\n\n        if tag.startswith(\"B-\"):\n            if current is not None:\n                entities.append(current)\n            fine_type = tag[2:]\n            coarse = fine_type.split(\"-\")[0].lower()\n            current = {\n                \"text\": tokens[i],\n                \"type\": coarse,\n                \"start\": offsets[i][0],\n                \"end\": offsets[i][1],\n            }\n        elif tag.startswith(\"I-\") and current is not None:\n            fine_type = tag[2:]\n            coarse = fine_type.split(\"-\")[0].lower()\n            if coarse == current[\"type\"]:\n                current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                current[\"end\"] = offsets[i][1]\n            else:\n                entities.append(current)\n                current = None\n        else:\n            if current is not None:\n                entities.append(current)\n                current = None\n\n    if current is not None:\n        entities.append(current)\n\n    return entities\n\n\ndef load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD test set from HuggingFace, convert to UIE format.\"\"\"\n    from datasets import load_dataset\n\n    log.info(\"Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...\")\n    ds = load_dataset(\"DFKI-SLT/few-nerd\", \"supervised\", split=\"test\")\n    tag_names = ds.features[\"ner_tags\"].feature.names\n\n    instances = []\n    for idx, example in enumerate(ds):\n        tokens = example[\"tokens\"]\n        tag_ids = example[\"ner_tags\"]\n        text = \" \".join(tokens)\n        entities = _bio_to_entities(tokens, tag_names, tag_ids)\n\n        instances.append({\n            \"id\": f\"fewnerd_test_{idx:05d}\",\n            \"text\": text,\n            \"entities\": entities,\n            \"relations\": [],\n            \"events\": [],\n        })\n\n    instances_with_ents = [inst for inst in instances if inst[\"entities\"]]\n    log.info(\"  Total test: %d, with entities: %d\", len(instances), len(instances_with_ents))\n\n    rng = random.Random(seed)\n    if len(instances_with_ents) > n_instances:\n        instances_with_ents = rng.sample(instances_with_ents, n_instances)\n\n    log.info(\"  Sampled %d instances (seed=%d)\", len(instances_with_ents), seed)\n    return instances_with_ents\n\n\ndef load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD from local UIE-format JSONL file.\"\"\"\n    instances = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            obj = json.loads(line)\n            if isinstance(obj, dict) and obj.get(\"entities\"):\n                instances.append(obj)\n\n    log.info(\"Loaded %d instances with entities from %s\", len(instances), path)\n\n    rng = random.Random(seed)\n    if len(instances) > n_instances:\n        instances = rng.sample(instances, n_instances)\n\n    log.info(\"Sampled %d instances (seed=%d)\", len(instances), seed)\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Prompt Construction (matches project template in zeroshot_prompts.py)\n# ---------------------------------------------------------------------------\n\nSYSTEM_PROMPT = (\n    \"You are a precise named entity recognition (NER) system. \"\n    \"Extract all named entities from the given text and output them in the specified JSON format. \"\n    \"Be exhaustive: identify every entity that matches the given types. \"\n    \"Be precise: the 'start' and 'end' values must be character offsets in the original text, \"\n    \"where 'start' is the index of the first character and 'end' is the index after the last character, \"\n    \"such that text[start:end] == entity text.\"\n)\n\n\ndef build_ner_prompt(text: str) -> list[dict]:\n    type_desc_lines = \"\\n\".join(f\"  - {t}: {d}\" for t, d in ENTITY_TYPES.items())\n    user_prompt = (\n        \"Extract all named entities from the following text.\\n\\n\"\n        f\"Entity types and their definitions:\\n{type_desc_lines}\\n\\n\"\n        f\"Text: {text}\\n\\n\"\n        \"Output a JSON object in exactly this format:\\n\"\n        '{\"entities\": [{\"text\": \"exact span\", \"type\": \"TYPE\", \"start\": 0, \"end\": 5}], '\n        '\"relations\": [], \"events\": []}\\n\\n'\n        \"Rules:\\n\"\n        \"- Extract ALL entities matching the given types\\n\"\n        \"- 'start' is the character offset of the first character of the entity in the text\\n\"\n        \"- 'end' is the character offset after the last character (Python slice convention)\\n\"\n        \"- 'text' must be the exact substring from the input text\\n\"\n        '- If no entities are found, return: {\"entities\": [], \"relations\": [], \"events\": []}\\n'\n        \"- Output ONLY the JSON object, no explanation\"\n    )\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_prompt},\n    ]\n\n\n# ---------------------------------------------------------------------------\n# API Sampling\n# ---------------------------------------------------------------------------\n\ndef create_client(api_base: str):\n    from openai import OpenAI\n\n    api_key = [REDACTED]\"OPENROUTER_API_KEY\", \"\")\n    if not api_key:\n        [REDACTED]\"OPENROUTER_API_KEY not set\")\n        sys.exit(1)\n    return OpenAI(base_url=api_base, api_key=[REDACTED]\n\n\ndef _api_call(client, model_id: str, messages: list[dict],\n              temperature: float, max_retries: int = 5) -> str:\n    for attempt in range(max_retries):\n        try:\n            resp = client.chat.completions.create(\n                model=model_id,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=1024,\n                response_format={\"type\": \"json_object\"},\n            )\n            return resp.choices[0].message.content or \"{}\"\n        except Exception as e:\n            wait = min(2 ** attempt * 1.0, 60)\n            log.warning(\"  API error (attempt %d/%d): %s\", attempt + 1, max_retries, e)\n            if attempt < max_retries - 1:\n                time.sleep(wait)\n            else:\n                log.error(\"  FAILED after %d attempts, returning empty\", max_retries)\n                return \"{}\"\n\n\ndef sample_instance(client, model_id: str, messages: list[dict],\n                    n_samples: int, temperature: float) -> tuple[str, list[str]]:\n    \"\"\"Return (greedy_response, [n_samples stochastic responses]).\"\"\"\n    greedy = _api_call(client, model_id, messages, temperature=0.0)\n    stochastic = []\n    for _ in range(n_samples):\n        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))\n    return greedy, stochastic\n\n\n# ---------------------------------------------------------------------------\n# Response Parsing\n# ---------------------------------------------------------------------------\n\ndef parse_response(raw: str) -> dict:\n    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    entities = []\n    for e in data.get(\"entities\", []):\n        if not isinstance(e, dict):\n            continue\n        try:\n            etype = str(e[\"type\"]).lower()\n            if etype not in VALID_TYPES:\n                continue\n            entities.append({\n                \"text\": str(e[\"text\"]),\n                \"type\": etype,\n                \"start\": int(e[\"start\"]),\n                \"end\": int(e[\"end\"]),\n            })\n        except (KeyError, ValueError, TypeError):\n            continue\n\n    return {\"entities\": entities, \"relations\": [], \"events\": []}\n\n\n# ---------------------------------------------------------------------------\n# Evaluation Primitives\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities: list[dict]) -> set[tuple]:\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:\n    if not gold_set and not pred_set:\n        return 1.0, 1.0, 1.0\n    if not pred_set:\n        return 0.0, 0.0, 0.0\n    if not gold_set:\n        return 0.0, 0.0, 0.0\n    tp = len(pred_set & gold_set)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred_set)\n    r = tp / len(gold_set)\n    f = 2 * p * r / (p + r)\n    return p, r, f\n\n\ndef entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:\n    counts: dict[tuple, int] = defaultdict(int)\n    N = len(samples)\n    for sample in samples:\n        for e in sample.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Instance-level Metrics\n# ---------------------------------------------------------------------------\n\ndef compute_instance_metrics(\n    greedy_parsed: dict,\n    sc_parsed: list[dict],\n    gold_entities: list[dict],\n) -> dict:\n    gold = entity_set(gold_entities)\n\n    # Greedy F1\n    greedy_ents = entity_set(greedy_parsed)\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)\n\n    # Per-sample F1\n    sample_f1s = []\n    for s in sc_parsed:\n        _, _, f = compute_prf(entity_set(s), gold)\n        sample_f1s.append(f)\n\n    # MV at multiple thresholds\n    mv_results = {}\n    for t in MV_THRESHOLDS:\n        mv_ents = entity_majority_vote(sc_parsed, threshold=t)\n        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)\n        mv_results[f\"t{t:.1f}\"] = {\"p\": mv_p, \"r\": mv_r, \"f1\": mv_f}\n\n    # Entity-level agreement: frequency of each entity across N samples\n    N = len(sc_parsed)\n    ent_counts: dict[tuple, int] = defaultdict(int)\n    for s in sc_parsed:\n        for e in s.get(\"entities\", []):\n            ent_counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n\n    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}\n    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0\n\n    # Degeneracy: all sample entity sets identical\n    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]\n    is_degenerate = len(set(sample_sets)) == 1\n\n    # Oracle best-of-N\n    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0\n\n    return {\n        \"greedy_p\": g_p,\n        \"greedy_r\": g_r,\n        \"greedy_f1\": g_f,\n        \"sample_f1s\": sample_f1s,\n        \"mean_sample_f1\": float(np.mean(sample_f1s)) if sample_f1s else 0.0,\n        \"oracle_f1\": oracle_f1,\n        \"mv\": mv_results,\n        \"mean_agreement\": mean_agreement,\n        \"n_unique_entities\": len(ent_counts),\n        \"n_gold_entities\": len(gold),\n        \"is_degenerate\": is_degenerate,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Aggregate Analysis\n# ---------------------------------------------------------------------------\n\ndef aggregate_model_results(results: list[dict]) -> dict:\n    n = len(results)\n\n    # Macro-averaged metrics\n    greedy_f1s = [r[\"metrics\"][\"greedy_f1\"] for r in results]\n    oracle_f1s = [r[\"metrics\"][\"oracle_f1\"] for r in results]\n    mean_sample_f1s = [r[\"metrics\"][\"mean_sample_f1\"] for r in results]\n    agreements = [r[\"metrics\"][\"mean_agreement\"] for r in results]\n    degeneracy_flags = [r[\"metrics\"][\"is_degenerate\"] for r in results]\n\n    # MV F1 per threshold\n    mv_f1_by_threshold = {}\n    for t in MV_THRESHOLDS:\n        tk = f\"t{t:.1f}\"\n        f1s = [r[\"metrics\"][\"mv\"][tk][\"f1\"] for r in results]\n        mv_f1_by_threshold[tk] = {\n            \"mean_f1\": float(np.mean(f1s)),\n            \"std_f1\": float(np.std(f1s)),\n        }\n\n    # Best threshold\n    best_t = max(mv_f1_by_threshold, key=lambda k: mv_f1_by_threshold[k][\"mean_f1\"])\n    best_mv_f1 = mv_f1_by_threshold[best_t][\"mean_f1\"]\n\n    greedy_mean = float(np.mean(greedy_f1s))\n    selection_gap = best_mv_f1 - greedy_mean\n\n    # Correlation: mean_agreement vs greedy_f1 (Spearman)\n    if n >= 3:\n        rho, pval = spearmanr(agreements, greedy_f1s)\n        corr_agreement_f1 = {\"rho\": float(rho), \"p\": float(pval)}\n    else:\n        corr_agreement_f1 = {\"rho\": 0.0, \"p\": 1.0}\n\n    # Correlation: mean_agreement vs MV F1 at best threshold\n    best_mv_f1s = [r[\"metrics\"][\"mv\"][best_t][\"f1\"] for r in results]\n    if n >= 3:\n        rho2, pval2 = spearmanr(agreements, best_mv_f1s)\n        corr_agreement_mv = {\"rho\": float(rho2), \"p\": float(pval2)}\n    else:\n        corr_agreement_mv = {\"rho\": 0.0, \"p\": 1.0}\n\n    return {\n        \"n_instances\": n,\n        \"greedy_f1\": {\"mean\": greedy_mean, \"std\": float(np.std(greedy_f1s))},\n        \"oracle_f1\": {\"mean\": float(np.mean(oracle_f1s)), \"std\": float(np.std(oracle_f1s))},\n        \"mean_sample_f1\": {\"mean\": float(np.mean(mean_sample_f1s)), \"std\": float(np.std(mean_sample_f1s))},\n        \"mv_f1_by_threshold\": mv_f1_by_threshold,\n        \"best_threshold\": best_t,\n        \"best_mv_f1\": best_mv_f1,\n        \"selection_gap\": selection_gap,\n        \"degeneracy_rate\": sum(degeneracy_flags) / n,\n        \"mean_agreement\": {\"mean\": float(np.mean(agreements)), \"std\": float(np.std(agreements))},\n        \"correlation_agreement_greedy_f1\": corr_agreement_f1,\n        \"correlation_agreement_mv_f1\": corr_agreement_mv,\n    }\n\n\ndef diagnose_failure_modes(results: list[dict]) -> dict:\n    \"\"\"Categorize failure modes across instances.\"\"\"\n    n = len(results)\n    degenerate = [r for r in results if r[\"metrics\"][\"is_degenerate\"]]\n    best_t_key = f\"t0.5\"\n\n    mv_better = []\n    mv_worse = []\n    mv_same = []\n\n    for r in results:\n        g = r[\"metrics\"][\"greedy_f1\"]\n        m = r[\"metrics\"][\"mv\"][best_t_key][\"f1\"]\n        diff = m - g\n        if diff > 0.01:\n            mv_better.append(r)\n        elif diff < -0.01:\n            mv_worse.append(r)\n        else:\n            mv_same.append(r)\n\n    # High agreement but wrong\n    high_agree_wrong = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] > 0.8 and r[\"metrics\"][\"greedy_f1\"] < 0.5\n    ]\n\n    # Low agreement but correct\n    low_agree_correct = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] < 0.3 and r[\"metrics\"][\"greedy_f1\"] > 0.8\n    ]\n\n    return {\n        \"degeneracy_count\": len(degenerate),\n        \"degeneracy_rate\": len(degenerate) / n,\n        \"mv_better_count\": len(mv_better),\n        \"mv_worse_count\": len(mv_worse),\n        \"mv_same_count\": len(mv_same),\n        \"high_agreement_wrong_count\": len(high_agree_wrong),\n        \"low_agreement_correct_count\": len(low_agree_correct),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpointing\n# ---------------------------------------------------------------------------\n\ndef save_checkpoint(data: list[dict], path: str):\n    with open(path, \"w\", encoding=\"utf-8\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n\n\ndef load_checkpoint(path: str) -> list[dict]:\n    if not os.path.exists(path):\n        return []\n    data = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                data.append(json.loads(line))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Main Experiment Loop\n# ---------------------------------------------------------------------------\n\ndef run_model(\n    client,\n    model_name: str,\n    model_id: str,\n    instances: list[dict],\n    n_samples: int,\n    temperature: float,\n    output_dir: Path,\n    resume: bool = True,\n) -> list[dict]:\n    ckpt_path = output_dir / f\"checkpoint_{model_name}.jsonl\"\n    results = load_checkpoint(str(ckpt_path)) if resume else []\n    done_ids = {r[\"id\"] for r in results}\n\n    remaining = [inst for inst in instances if inst[\"id\"] not in done_ids]\n    log.info(\"Model %s: %d done, %d remaining\", model_name, len(done_ids), len(remaining))\n\n    for i, inst in enumerate(remaining):\n        log.info(\n            \"  [%d/%d] id=%s len=%d entities=%d\",\n            len(done_ids) + i + 1,\n            len(instances),\n            inst[\"id\"],\n            len(inst[\"text\"]),\n            len(inst[\"entities\"]),\n        )\n\n        messages = build_ner_prompt(inst[\"text\"])\n        greedy_raw, sc_raws = sample_instance(\n            client, model_id, messages, n_samples, temperature\n        )\n\n        greedy_parsed = parse_response(greedy_raw)\n        sc_parsed = [parse_response(r) for r in sc_raws]\n\n        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst[\"entities\"])\n\n        result = {\n            \"id\": inst[\"id\"],\n            \"text\": inst[\"text\"],\n            \"gold_entities\": inst[\"entities\"],\n            \"greedy_raw\": greedy_raw,\n            \"greedy_parsed\": greedy_parsed,\n            \"sc_raws\": sc_raws,\n            \"sc_parsed\": sc_parsed,\n            \"metrics\": metrics,\n        }\n        results.append(result)\n\n        # Checkpoint every 10 instances\n        if (len(done_ids) + i + 1) % 10 == 0:\n            save_checkpoint(results, str(ckpt_path))\n            running = aggregate_model_results(results)\n            log.info(\n                \"    Checkpoint: greedy=%.4f, MV@0.5=%.4f, gap=%.4f, degen=%.1f%%\",\n                running[\"greedy_f1\"][\"mean\"],\n                running[\"mv_f1_by_threshold\"][\"t0.5\"][\"mean_f1\"],\n                running[\"selection_gap\"],\n                running[\"degeneracy_rate\"] * 100,\n            )\n\n    save_checkpoint(results, str(ckpt_path))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Frontier SC on FewNERD\")\n    parser.add_argument(\"--data-path\", type=str, default=None,\n                        help=\"Path to local FewNERD UIE JSONL file\")\n    parser.add_argument(\"--from-hf\", action=\"store_true\",\n                        help=\"Load FewNERD from HuggingFace\")\n    parser.add_argument(\"--n-instances\", type=int, default=200)\n    parser.add_argument(\"--n-samples\", type=int, default=8)\n    parser.add_argument(\"--temperature\", type=float, default=1.0)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--api-base\", type=str, default=API_BASE_URL)\n    parser.add_argument(\"--models\", type=str, nargs=\"+\", default=list(MODELS.keys()),\n                        choices=list(MODELS.keys()),\n                        help=\"Which models to run\")\n    parser.add_argument(\"--output-dir\", type=str,\n                        default=str(Path(__file__).parent / \"output\"))\n    parser.add_argument(\"--no-resume\", action=\"store_true\",\n                        help=\"Start fresh, ignore checkpoints\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # Load data\n    if args.data_path and os.path.exists(args.data_path):\n        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)\n    elif args.from_hf:\n        instances = load_fewnerd_hf(args.n_instances, args.seed)\n    else:\n        parser.error(\"Specify --data-path or --from-hf\")\n\n    # Save selected instance IDs for reproducibility\n    id_list = [inst[\"id\"] for inst in instances]\n    with open(output_dir / \"instance_ids.json\", \"w\") as f:\n        json.dump({\"seed\": args.seed, \"n\": len(id_list), \"ids\": id_list}, f, indent=2)\n\n    client = create_client(args.api_base)\n\n    all_summaries = {}\n\n    for model_name in args.models:\n        model_id = MODELS[model_name]\n        log.info(\"=\" * 60)\n        log.info(\"Running model: %s (%s)\", model_name, model_id)\n        log.info(\"=\" * 60)\n\n        results = run_model(\n            client, model_name, model_id, instances,\n            args.n_samples, args.temperature, output_dir,\n            resume=not args.no_resume,\n        )\n\n        # Aggregate\n        summary = aggregate_model_results(results)\n        diagnosis = diagnose_failure_modes(results)\n        summary[\"diagnosis\"] = diagnosis\n        all_summaries[model_name] = summary\n\n        # Print summary\n        log.info(\"\\n--- %s Summary ---\", model_name)\n        log.info(\"  Greedy F1:       %.4f (±%.4f)\", summary[\"greedy_f1\"][\"mean\"], summary[\"greedy_f1\"][\"std\"])\n        log.info(\"  Oracle F1:       %.4f\", summary[\"oracle_f1\"][\"mean\"])\n        log.info(\"  Best MV F1:      %.4f (threshold=%s)\", summary[\"best_mv_f1\"], summary[\"best_threshold\"])\n        log.info(\"  Selection gap:   %+.4f\", summary[\"selection_gap\"])\n        log.info(\"  Degeneracy rate: %.1f%%\", summary[\"degeneracy_rate\"] * 100)\n        log.info(\"  Corr(agree,F1):  rho=%.4f (p=%.4f)\",\n                 summary[\"correlation_agreement_greedy_f1\"][\"rho\"],\n                 summary[\"correlation_agreement_greedy_f1\"][\"p\"])\n        log.info(\"  MV threshold sweep:\")\n        for t in MV_THRESHOLDS:\n            tk = f\"t{t:.1f}\"\n            mv = summary[\"mv_f1_by_threshold\"][tk]\n            delta = mv[\"mean_f1\"] - summary[\"greedy_f1\"][\"mean\"]\n            marker = \" <-- BEST\" if tk == summary[\"best_threshold\"] else \"\"\n            log.info(\"    θ=%.1f  F1=%.4f  Δ=%+.4f%s\", t, mv[\"mean_f1\"], delta, marker)\n\n    # Cross-model comparison\n    if len(all_summaries) > 1:\n        log.info(\"\\n\" + \"=\" * 60)\n        log.info(\"CROSS-MODEL COMPARISON\")\n        log.info(\"=\" * 60)\n        log.info(\"%-20s %8s %8s %8s %10s %8s\", \"Model\", \"Greedy\", \"MV@best\", \"Oracle\", \"Gap\", \"Degen%\")\n        for name, s in all_summaries.items():\n            log.info(\n                \"%-20s %8.4f %8.4f %8.4f %+10.4f %7.1f%%\",\n                name,\n                s[\"greedy_f1\"][\"mean\"],\n                s[\"best_mv_f1\"],\n                s[\"oracle_f1\"][\"mean\"],\n                s[\"selection_gap\"],\n                s[\"degeneracy_rate\"] * 100,\n            )\n\n    # Save final results\n    final_output = {\n        \"config\": {\n            \"n_instances\": args.n_instances,\n            \"n_samples\": args.n_samples,\n            \"temperature\": args.temperature,\n            \"seed\": args.seed,\n            \"api_base\": args.api_base,\n            \"models\": {m: MODELS[m] for m in args.models},\n        },\n        \"summaries\": all_summaries,\n    }\n\n    with open(output_dir / \"results_summary.json\", \"w\") as f:\n        json.dump(final_output, f, indent=2, default=str)\n\n    log.info(\"\\nResults saved to %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
    "content": "#!/usr/bin/env python3\n\"\"\"Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).\n\nTests whether the correlation-selection gap in structured self-consistency\npersists with frontier models (GPT-5.5, Claude Opus 4.6), validating it\nas a fundamental limitation rather than a capability issue.\n\nCPU-only — all computation is via API calls through OpenRouter.\n\nUsage:\n    export OPENROUTER_API_KEY=\"[REDACTED]\"\n    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl\n    python run_frontier_sc.py --from-hf  # load from HuggingFace\n\"\"\"\n\nfrom __future__ import annotations\n\nimport argparse\nimport json\nimport logging\nimport os\nimport random\nimport sys\nimport time\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nfrom scipy.stats import spearmanr\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\nMODELS = {\n    \"gpt-5.5\": \"openai/gpt-5.5\",\n    \"claude-opus-4.6\": \"anthropic/claude-opus-4.6\",\n}\n\nAPI_BASE_URL = \"http://47.94.22.126/v1\"\n\nENTITY_TYPES = {\n    \"person\": \"Person names\",\n    \"organization\": \"Organizations, companies, teams\",\n    \"location\": \"Geographic locations, countries, cities\",\n    \"building\": \"Buildings, facilities, landmarks\",\n    \"art\": \"Artworks, songs, films, books\",\n    \"product\": \"Commercial products, software, vehicles\",\n    \"event\": \"Events, competitions, wars, festivals\",\n    \"other\": \"Other named entities not fitting the above categories\",\n}\n\nVALID_TYPES = set(ENTITY_TYPES.keys())\n\nMV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n    datefmt=\"%Y-%m-%d %H:%M:%S\",\n)\nlog = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Data Loading\n# ---------------------------------------------------------------------------\n\ndef _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:\n    offsets = []\n    pos = 0\n    for tok in tokens:\n        offsets.append((pos, pos + len(tok)))\n        pos += len(tok) + 1\n    return offsets\n\n\ndef _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:\n    \"\"\"Convert BIO-tagged tokens to entity spans with char offsets.\"\"\"\n    offsets = _token_offsets(tokens)\n    entities = []\n    current = None\n\n    for i, tag_id in enumerate(tag_ids):\n        tag = tag_names[tag_id]\n\n        if tag.startswith(\"B-\"):\n            if current is not None:\n                entities.append(current)\n            fine_type = tag[2:]\n            coarse = fine_type.split(\"-\")[0].lower()\n            current = {\n                \"text\": tokens[i],\n                \"type\": coarse,\n                \"start\": offsets[i][0],\n                \"end\": offsets[i][1],\n            }\n        elif tag.startswith(\"I-\") and current is not None:\n            fine_type = tag[2:]\n            coarse = fine_type.split(\"-\")[0].lower()\n            if coarse == current[\"type\"]:\n                current[\"text\"] = current[\"text\"] + \" \" + tokens[i]\n                current[\"end\"] = offsets[i][1]\n            else:\n                entities.append(current)\n                current = None\n        else:\n            if current is not None:\n                entities.append(current)\n                current = None\n\n    if current is not None:\n        entities.append(current)\n\n    return entities\n\n\ndef load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD test set from HuggingFace, convert to UIE format.\"\"\"\n    from datasets import load_dataset\n\n    log.info(\"Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...\")\n    ds = load_dataset(\"DFKI-SLT/few-nerd\", \"supervised\", split=\"test\")\n    tag_names = ds.features[\"ner_tags\"].feature.names\n\n    instances = []\n    for idx, example in enumerate(ds):\n        tokens = example[\"tokens\"]\n        tag_ids = example[\"ner_tags\"]\n        text = \" \".join(tokens)\n        entities = _bio_to_entities(tokens, tag_names, tag_ids)\n\n        instances.append({\n            \"id\": f\"fewnerd_test_{idx:05d}\",\n            \"text\": text,\n            \"entities\": entities,\n            \"relations\": [],\n            \"events\": [],\n        })\n\n    instances_with_ents = [inst for inst in instances if inst[\"entities\"]]\n    log.info(\"  Total test: %d, with entities: %d\", len(instances), len(instances_with_ents))\n\n    rng = random.Random(seed)\n    if len(instances_with_ents) > n_instances:\n        instances_with_ents = rng.sample(instances_with_ents, n_instances)\n\n    log.info(\"  Sampled %d instances (seed=%d)\", len(instances_with_ents), seed)\n    return instances_with_ents\n\n\ndef load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:\n    \"\"\"Load FewNERD from local UIE-format JSONL file.\"\"\"\n    instances = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            obj = json.loads(line)\n            if isinstance(obj, dict) and obj.get(\"entities\"):\n                instances.append(obj)\n\n    log.info(\"Loaded %d instances with entities from %s\", len(instances), path)\n\n    rng = random.Random(seed)\n    if len(instances) > n_instances:\n        instances = rng.sample(instances, n_instances)\n\n    log.info(\"Sampled %d instances (seed=%d)\", len(instances), seed)\n    return instances\n\n\n# ---------------------------------------------------------------------------\n# Prompt Construction (matches project template in zeroshot_prompts.py)\n# ---------------------------------------------------------------------------\n\nSYSTEM_PROMPT = (\n    \"You are a precise named entity recognition (NER) system. \"\n    \"Extract all named entities from the given text and output them in the specified JSON format. \"\n    \"Be exhaustive: identify every entity that matches the given types. \"\n    \"Be precise: the 'start' and 'end' values must be character offsets in the original text, \"\n    \"where 'start' is the index of the first character and 'end' is the index after the last character, \"\n    \"such that text[start:end] == entity text.\"\n)\n\n\ndef build_ner_prompt(text: str) -> list[dict]:\n    type_desc_lines = \"\\n\".join(f\"  - {t}: {d}\" for t, d in ENTITY_TYPES.items())\n    user_prompt = (\n        \"Extract all named entities from the following text.\\n\\n\"\n        f\"Entity types and their definitions:\\n{type_desc_lines}\\n\\n\"\n        f\"Text: {text}\\n\\n\"\n        \"Output a JSON object in exactly this format:\\n\"\n        '{\"entities\": [{\"text\": \"exact span\", \"type\": \"TYPE\", \"start\": 0, \"end\": 5}], '\n        '\"relations\": [], \"events\": []}\\n\\n'\n        \"Rules:\\n\"\n        \"- Extract ALL entities matching the given types\\n\"\n        \"- 'start' is the character offset of the first character of the entity in the text\\n\"\n        \"- 'end' is the character offset after the last character (Python slice convention)\\n\"\n        \"- 'text' must be the exact substring from the input text\\n\"\n        '- If no entities are found, return: {\"entities\": [], \"relations\": [], \"events\": []}\\n'\n        \"- Output ONLY the JSON object, no explanation\"\n    )\n    return [\n        {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n        {\"role\": \"user\", \"content\": user_prompt},\n    ]\n\n\n# ---------------------------------------------------------------------------\n# API Sampling\n# ---------------------------------------------------------------------------\n\ndef create_client(api_base: str):\n    from openai import OpenAI\n\n    api_key = [REDACTED]\"OPENROUTER_API_KEY\", \"\")\n    if not api_key:\n        [REDACTED]\"OPENROUTER_API_KEY not set\")\n        sys.exit(1)\n    return OpenAI(base_url=api_base, api_key=[REDACTED]\n\n\ndef _api_call(client, model_id: str, messages: list[dict],\n              temperature: float, max_retries: int = 5) -> str:\n    for attempt in range(max_retries):\n        try:\n            resp = client.chat.completions.create(\n                model=model_id,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=1024,\n                response_format={\"type\": \"json_object\"},\n            )\n            return resp.choices[0].message.content or \"{}\"\n        except Exception as e:\n            wait = min(2 ** attempt * 1.0, 60)\n            log.warning(\"  API error (attempt %d/%d): %s\", attempt + 1, max_retries, e)\n            if attempt < max_retries - 1:\n                time.sleep(wait)\n            else:\n                log.error(\"  FAILED after %d attempts, returning empty\", max_retries)\n                return \"{}\"\n\n\ndef sample_instance(client, model_id: str, messages: list[dict],\n                    n_samples: int, temperature: float) -> tuple[str, list[str]]:\n    \"\"\"Return (greedy_response, [n_samples stochastic responses]).\"\"\"\n    greedy = _api_call(client, model_id, messages, temperature=0.0)\n    stochastic = []\n    for _ in range(n_samples):\n        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))\n    return greedy, stochastic\n\n\n# ---------------------------------------------------------------------------\n# Response Parsing\n# ---------------------------------------------------------------------------\n\ndef parse_response(raw: str) -> dict:\n    raw = raw.strip()\n    try:\n        data = json.loads(raw)\n    except json.JSONDecodeError:\n        start = raw.find(\"{\")\n        end = raw.rfind(\"}\")\n        if start != -1 and end != -1 and end > start:\n            try:\n                data = json.loads(raw[start : end + 1])\n            except json.JSONDecodeError:\n                return {\"entities\": [], \"relations\": [], \"events\": []}\n        else:\n            return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    if not isinstance(data, dict):\n        return {\"entities\": [], \"relations\": [], \"events\": []}\n\n    entities = []\n    for e in data.get(\"entities\", []):\n        if not isinstance(e, dict):\n            continue\n        try:\n            etype = str(e[\"type\"]).lower()\n            if etype not in VALID_TYPES:\n                continue\n            entities.append({\n                \"text\": str(e[\"text\"]),\n                \"type\": etype,\n                \"start\": int(e[\"start\"]),\n                \"end\": int(e[\"end\"]),\n            })\n        except (KeyError, ValueError, TypeError):\n            continue\n\n    return {\"entities\": entities, \"relations\": [], \"events\": []}\n\n\n# ---------------------------------------------------------------------------\n# Evaluation Primitives\n# ---------------------------------------------------------------------------\n\ndef entity_set(entities: list[dict]) -> set[tuple]:\n    return {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in entities}\n\n\ndef compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:\n    if not gold_set and not pred_set:\n        return 1.0, 1.0, 1.0\n    if not pred_set:\n        return 0.0, 0.0, 0.0\n    if not gold_set:\n        return 0.0, 0.0, 0.0\n    tp = len(pred_set & gold_set)\n    if tp == 0:\n        return 0.0, 0.0, 0.0\n    p = tp / len(pred_set)\n    r = tp / len(gold_set)\n    f = 2 * p * r / (p + r)\n    return p, r, f\n\n\ndef entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:\n    counts: dict[tuple, int] = defaultdict(int)\n    N = len(samples)\n    for sample in samples:\n        for e in sample.get(\"entities\", []):\n            counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n    return {k for k, c in counts.items() if c / N >= threshold}\n\n\n# ---------------------------------------------------------------------------\n# Instance-level Metrics\n# ---------------------------------------------------------------------------\n\ndef compute_instance_metrics(\n    greedy_parsed: dict,\n    sc_parsed: list[dict],\n    gold_entities: list[dict],\n) -> dict:\n    gold = entity_set(gold_entities)\n\n    # Greedy F1\n    greedy_ents = entity_set(greedy_parsed)\n    g_p, g_r, g_f = compute_prf(greedy_ents, gold)\n\n    # Per-sample F1\n    sample_f1s = []\n    for s in sc_parsed:\n        _, _, f = compute_prf(entity_set(s), gold)\n        sample_f1s.append(f)\n\n    # MV at multiple thresholds\n    mv_results = {}\n    for t in MV_THRESHOLDS:\n        mv_ents = entity_majority_vote(sc_parsed, threshold=t)\n        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)\n        mv_results[f\"t{t:.1f}\"] = {\"p\": mv_p, \"r\": mv_r, \"f1\": mv_f}\n\n    # Entity-level agreement: frequency of each entity across N samples\n    N = len(sc_parsed)\n    ent_counts: dict[tuple, int] = defaultdict(int)\n    for s in sc_parsed:\n        for e in s.get(\"entities\", []):\n            ent_counts[(e[\"start\"], e[\"end\"], e[\"type\"])] += 1\n\n    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}\n    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0\n\n    # Degeneracy: all sample entity sets identical\n    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]\n    is_degenerate = len(set(sample_sets)) == 1\n\n    # Oracle best-of-N\n    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0\n\n    return {\n        \"greedy_p\": g_p,\n        \"greedy_r\": g_r,\n        \"greedy_f1\": g_f,\n        \"sample_f1s\": sample_f1s,\n        \"mean_sample_f1\": float(np.mean(sample_f1s)) if sample_f1s else 0.0,\n        \"oracle_f1\": oracle_f1,\n        \"mv\": mv_results,\n        \"mean_agreement\": mean_agreement,\n        \"n_unique_entities\": len(ent_counts),\n        \"n_gold_entities\": len(gold),\n        \"is_degenerate\": is_degenerate,\n    }\n\n\n# ---------------------------------------------------------------------------\n# Aggregate Analysis\n# ---------------------------------------------------------------------------\n\ndef aggregate_model_results(results: list[dict]) -> dict:\n    n = len(results)\n\n    # Macro-averaged metrics\n    greedy_f1s = [r[\"metrics\"][\"greedy_f1\"] for r in results]\n    oracle_f1s = [r[\"metrics\"][\"oracle_f1\"] for r in results]\n    mean_sample_f1s = [r[\"metrics\"][\"mean_sample_f1\"] for r in results]\n    agreements = [r[\"metrics\"][\"mean_agreement\"] for r in results]\n    degeneracy_flags = [r[\"metrics\"][\"is_degenerate\"] for r in results]\n\n    # MV F1 per threshold\n    mv_f1_by_threshold = {}\n    for t in MV_THRESHOLDS:\n        tk = f\"t{t:.1f}\"\n        f1s = [r[\"metrics\"][\"mv\"][tk][\"f1\"] for r in results]\n        mv_f1_by_threshold[tk] = {\n            \"mean_f1\": float(np.mean(f1s)),\n            \"std_f1\": float(np.std(f1s)),\n        }\n\n    # Best threshold\n    best_t = max(mv_f1_by_threshold, key=lambda k: mv_f1_by_threshold[k][\"mean_f1\"])\n    best_mv_f1 = mv_f1_by_threshold[best_t][\"mean_f1\"]\n\n    greedy_mean = float(np.mean(greedy_f1s))\n    selection_gap = best_mv_f1 - greedy_mean\n\n    # Correlation: mean_agreement vs greedy_f1 (Spearman)\n    if n >= 3:\n        rho, pval = spearmanr(agreements, greedy_f1s)\n        corr_agreement_f1 = {\"rho\": float(rho), \"p\": float(pval)}\n    else:\n        corr_agreement_f1 = {\"rho\": 0.0, \"p\": 1.0}\n\n    # Correlation: mean_agreement vs MV F1 at best threshold\n    best_mv_f1s = [r[\"metrics\"][\"mv\"][best_t][\"f1\"] for r in results]\n    if n >= 3:\n        rho2, pval2 = spearmanr(agreements, best_mv_f1s)\n        corr_agreement_mv = {\"rho\": float(rho2), \"p\": float(pval2)}\n    else:\n        corr_agreement_mv = {\"rho\": 0.0, \"p\": 1.0}\n\n    return {\n        \"n_instances\": n,\n        \"greedy_f1\": {\"mean\": greedy_mean, \"std\": float(np.std(greedy_f1s))},\n        \"oracle_f1\": {\"mean\": float(np.mean(oracle_f1s)), \"std\": float(np.std(oracle_f1s))},\n        \"mean_sample_f1\": {\"mean\": float(np.mean(mean_sample_f1s)), \"std\": float(np.std(mean_sample_f1s))},\n        \"mv_f1_by_threshold\": mv_f1_by_threshold,\n        \"best_threshold\": best_t,\n        \"best_mv_f1\": best_mv_f1,\n        \"selection_gap\": selection_gap,\n        \"degeneracy_rate\": sum(degeneracy_flags) / n,\n        \"mean_agreement\": {\"mean\": float(np.mean(agreements)), \"std\": float(np.std(agreements))},\n        \"correlation_agreement_greedy_f1\": corr_agreement_f1,\n        \"correlation_agreement_mv_f1\": corr_agreement_mv,\n    }\n\n\ndef diagnose_failure_modes(results: list[dict]) -> dict:\n    \"\"\"Categorize failure modes across instances.\"\"\"\n    n = len(results)\n    degenerate = [r for r in results if r[\"metrics\"][\"is_degenerate\"]]\n    best_t_key = f\"t0.5\"\n\n    mv_better = []\n    mv_worse = []\n    mv_same = []\n\n    for r in results:\n        g = r[\"metrics\"][\"greedy_f1\"]\n        m = r[\"metrics\"][\"mv\"][best_t_key][\"f1\"]\n        diff = m - g\n        if diff > 0.01:\n            mv_better.append(r)\n        elif diff < -0.01:\n            mv_worse.append(r)\n        else:\n            mv_same.append(r)\n\n    # High agreement but wrong\n    high_agree_wrong = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] > 0.8 and r[\"metrics\"][\"greedy_f1\"] < 0.5\n    ]\n\n    # Low agreement but correct\n    low_agree_correct = [\n        r for r in results\n        if r[\"metrics\"][\"mean_agreement\"] < 0.3 and r[\"metrics\"][\"greedy_f1\"] > 0.8\n    ]\n\n    return {\n        \"degeneracy_count\": len(degenerate),\n        \"degeneracy_rate\": len(degenerate) / n,\n        \"mv_better_count\": len(mv_better),\n        \"mv_worse_count\": len(mv_worse),\n        \"mv_same_count\": len(mv_same),\n        \"high_agreement_wrong_count\": len(high_agree_wrong),\n        \"low_agreement_correct_count\": len(low_agree_correct),\n    }\n\n\n# ---------------------------------------------------------------------------\n# Checkpointing\n# ---------------------------------------------------------------------------\n\ndef save_checkpoint(data: list[dict], path: str):\n    with open(path, \"w\", encoding=\"utf-8\") as f:\n        for item in data:\n            f.write(json.dumps(item, ensure_ascii=False) + \"\\n\")\n\n\ndef load_checkpoint(path: str) -> list[dict]:\n    if not os.path.exists(path):\n        return []\n    data = []\n    with open(path, encoding=\"utf-8\") as f:\n        for line in f:\n            line = line.strip()\n            if line:\n                data.append(json.loads(line))\n    return data\n\n\n# ---------------------------------------------------------------------------\n# Main Experiment Loop\n# ---------------------------------------------------------------------------\n\ndef run_model(\n    client,\n    model_name: str,\n    model_id: str,\n    instances: list[dict],\n    n_samples: int,\n    temperature: float,\n    output_dir: Path,\n    resume: bool = True,\n) -> list[dict]:\n    ckpt_path = output_dir / f\"checkpoint_{model_name}.jsonl\"\n    results = load_checkpoint(str(ckpt_path)) if resume else []\n    done_ids = {r[\"id\"] for r in results}\n\n    remaining = [inst for inst in instances if inst[\"id\"] not in done_ids]\n    log.info(\"Model %s: %d done, %d remaining\", model_name, len(done_ids), len(remaining))\n\n    for i, inst in enumerate(remaining):\n        log.info(\n            \"  [%d/%d] id=%s len=%d entities=%d\",\n            len(done_ids) + i + 1,\n            len(instances),\n            inst[\"id\"],\n            len(inst[\"text\"]),\n            len(inst[\"entities\"]),\n        )\n\n        messages = build_ner_prompt(inst[\"text\"])\n        greedy_raw, sc_raws = sample_instance(\n            client, model_id, messages, n_samples, temperature\n        )\n\n        greedy_parsed = parse_response(greedy_raw)\n        sc_parsed = [parse_response(r) for r in sc_raws]\n\n        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst[\"entities\"])\n\n        result = {\n            \"id\": inst[\"id\"],\n            \"text\": inst[\"text\"],\n            \"gold_entities\": inst[\"entities\"],\n            \"greedy_raw\": greedy_raw,\n            \"greedy_parsed\": greedy_parsed,\n            \"sc_raws\": sc_raws,\n            \"sc_parsed\": sc_parsed,\n            \"metrics\": metrics,\n        }\n        results.append(result)\n\n        # Checkpoint every 10 instances\n        if (len(done_ids) + i + 1) % 10 == 0:\n            save_checkpoint(results, str(ckpt_path))\n            running = aggregate_model_results(results)\n            log.info(\n                \"    Checkpoint: greedy=%.4f, MV@0.5=%.4f, gap=%.4f, degen=%.1f%%\",\n                running[\"greedy_f1\"][\"mean\"],\n                running[\"mv_f1_by_threshold\"][\"t0.5\"][\"mean_f1\"],\n                running[\"selection_gap\"],\n                running[\"degeneracy_rate\"] * 100,\n            )\n\n    save_checkpoint(results, str(ckpt_path))\n    return results\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Frontier SC on FewNERD\")\n    parser.add_argument(\"--data-path\", type=str, default=None,\n                        help=\"Path to local FewNERD UIE JSONL file\")\n    parser.add_argument(\"--from-hf\", action=\"store_true\",\n                        help=\"Load FewNERD from HuggingFace\")\n    parser.add_argument(\"--n-instances\", type=int, default=200)\n    parser.add_argument(\"--n-samples\", type=int, default=8)\n    parser.add_argument(\"--temperature\", type=float, default=1.0)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--api-base\", type=str, default=API_BASE_URL)\n    parser.add_argument(\"--models\", type=str, nargs=\"+\", default=list(MODELS.keys()),\n                        choices=list(MODELS.keys()),\n                        help=\"Which models to run\")\n    parser.add_argument(\"--output-dir\", type=str,\n                        default=str(Path(__file__).parent / \"output\"))\n    parser.add_argument(\"--no-resume\", action=\"store_true\",\n                        help=\"Start fresh, ignore checkpoints\")\n    args = parser.parse_args()\n\n    output_dir = Path(args.output_dir)\n    output_dir.mkdir(parents=True, exist_ok=True)\n\n    # Load data\n    if args.data_path and os.path.exists(args.data_path):\n        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)\n    elif args.from_hf:\n        instances = load_fewnerd_hf(args.n_instances, args.seed)\n    else:\n        parser.error(\"Specify --data-path or --from-hf\")\n\n    # Save selected instance IDs for reproducibility\n    id_list = [inst[\"id\"] for inst in instances]\n    with open(output_dir / \"instance_ids.json\", \"w\") as f:\n        json.dump({\"seed\": args.seed, \"n\": len(id_list), \"ids\": id_list}, f, indent=2)\n\n    client = create_client(args.api_base)\n\n    all_summaries = {}\n\n    for model_name in args.models:\n        model_id = MODELS[model_name]\n        log.info(\"=\" * 60)\n        log.info(\"Running model: %s (%s)\", model_name, model_id)\n        log.info(\"=\" * 60)\n\n        results = run_model(\n            client, model_name, model_id, instances,\n            args.n_samples, args.temperature, output_dir,\n            resume=not args.no_resume,\n        )\n\n        # Aggregate\n        summary = aggregate_model_results(results)\n        diagnosis = diagnose_failure_modes(results)\n        summary[\"diagnosis\"] = diagnosis\n        all_summaries[model_name] = summary\n\n        # Print summary\n        log.info(\"\\n--- %s Summary ---\", model_name)\n        log.info(\"  Greedy F1:       %.4f (±%.4f)\", summary[\"greedy_f1\"][\"mean\"], summary[\"greedy_f1\"][\"std\"])\n        log.info(\"  Oracle F1:       %.4f\", summary[\"oracle_f1\"][\"mean\"])\n        log.info(\"  Best MV F1:      %.4f (threshold=%s)\", summary[\"best_mv_f1\"], summary[\"best_threshold\"])\n        log.info(\"  Selection gap:   %+.4f\", summary[\"selection_gap\"])\n        log.info(\"  Degeneracy rate: %.1f%%\", summary[\"degeneracy_rate\"] * 100)\n        log.info(\"  Corr(agree,F1):  rho=%.4f (p=%.4f)\",\n                 summary[\"correlation_agreement_greedy_f1\"][\"rho\"],\n                 summary[\"correlation_agreement_greedy_f1\"][\"p\"])\n        log.info(\"  MV threshold sweep:\")\n        for t in MV_THRESHOLDS:\n            tk = f\"t{t:.1f}\"\n            mv = summary[\"mv_f1_by_threshold\"][tk]\n            delta = mv[\"mean_f1\"] - summary[\"greedy_f1\"][\"mean\"]\n            marker = \" <-- BEST\" if tk == summary[\"best_threshold\"] else \"\"\n            log.info(\"    θ=%.1f  F1=%.4f  Δ=%+.4f%s\", t, mv[\"mean_f1\"], delta, marker)\n\n    # Cross-model comparison\n    if len(all_summaries) > 1:\n        log.info(\"\\n\" + \"=\" * 60)\n        log.info(\"CROSS-MODEL COMPARISON\")\n        log.info(\"=\" * 60)\n        log.info(\"%-20s %8s %8s %8s %10s %8s\", \"Model\", \"Greedy\", \"MV@best\", \"Oracle\", \"Gap\", \"Degen%\")\n        for name, s in all_summaries.items():\n            log.info(\n                \"%-20s %8.4f %8.4f %8.4f %+10.4f %7.1f%%\",\n                name,\n                s[\"greedy_f1\"][\"mean\"],\n                s[\"best_mv_f1\"],\n                s[\"oracle_f1\"][\"mean\"],\n                s[\"selection_gap\"],\n                s[\"degeneracy_rate\"] * 100,\n            )\n\n    # Save final results\n    final_output = {\n        \"config\": {\n            \"n_instances\": args.n_instances,\n            \"n_samples\": args.n_samples,\n            \"temperature\": args.temperature,\n            \"seed\": args.seed,\n            \"api_base\": args.api_base,\n            \"models\": {m: MODELS[m] for m in args.models},\n        },\n        \"summaries\": all_summaries,\n    }\n\n    with open(output_dir / \"results_summary.json\", \"w\") as f:\n        json.dump(final_output, f, indent=2, default=str)\n\n    log.info(\"\\nResults saved to %s\", output_dir)\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-20T18:25:10.652905+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-20T18:25:10.653077+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-20T18:25:10.653227+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-20T18:25:10.653348+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-20T18:25:10.653464+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-20T18:25:10.653583+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "run_frontier_sc.py",
  "type": "intermediate",
  "description": "Frontier model SC experiment script on FewNERD — GPT-5.5 + Claude Opus 4.6 via OpenRouter API, frequency-based agreement, MV construction, correlation-selection gap analysis",
  "project": "struct_self_consist_ie",
  "exp_id": "exp_b_frontier_sc_fewnerd",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
  "tags": "['frontier', 'self-consistency', 'fewnerd', 'api', 'cpu-only']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "run_frontier_sc.py",
    "type": "intermediate",
    "description": "Frontier model SC experiment script on FewNERD — GPT-5.5 + Claude Opus 4.6 via OpenRouter API, frequency-based agreement, MV construction, correlation-selection gap analysis",
    "project": "struct_self_consist_ie",
    "exp_id": "exp_b_frontier_sc_fewnerd",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py",
    "tags": "['frontier', 'self-consistency', 'fewnerd', 'api', 'cpu-only']"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-20T18:25:10.653733+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_8c8392\", \"name\": \"run_frontier_sc.py\", \"type\": \"intermediate\", \"description\": \"Frontier model SC experiment script on FewNERD — GPT-5.5 + Claude Opus 4.6 via OpenRouter API, frequency-based agreement, MV construction, correlation-selection gap analysis\", \"path\": \"projects/struct_self_consist_ie/artifacts/exp_b_frontier_sc_fewnerd/intermediate/run_frontier_sc.py\", \"url\": null, \"project\": \"struct_self_consist_ie\", \"exp_id\": \"exp_b_frontier_sc_fewnerd\", \"skill\": \"\", \"created_at\": \"2026-05-20T18:24:39.706381+00:00\", \"tags\": [\"frontier\", \"self-consistency\", \"fewnerd\", \"api\", \"cpu-only\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-20T18:25:10.653864+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_b_frontier_sc_fewnerd",
  "field": "hypothesis",
  "value": "The correlation-selection gap in structured self-consistency persists with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental limitation of frequency-based SC for structured prediction rather than a capability issue of smaller models.",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_b_frontier_sc_fewnerd",
    "field": "hypothesis",
    "value": "The correlation-selection gap in structured self-consistency persists with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental limitation of frequency-based SC for structured prediction rather than a capability issue of smaller models.",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-20T18:25:10.653996+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_b_frontier_sc_fewnerd\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:19.266Z\", \"updated_at\": \"2026-05-20T18:24:42.198Z\", \"hypothesis\": \"The correlation-selection gap in structured self-consistency persists with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental limitation of frequency-based SC for structured prediction rather than a capability issue of smaller models.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9189}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-20T18:25:10.654139+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_b_frontier_sc_fewnerd",
  "field": "status",
  "value": "PREPARING",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python run_frontier_sc.py --from-hf --n-instances 200 --n-samples 8 --temperature 1.0 --seed 42', 'server': 'local (CPU-only, API calls)', 'data_path': 'HuggingFace: DFKI-SLT/few-nerd (supervised, test split)', 'data_count': 200, 'model_name': 'GPT-5.5 + Claude Opus 4.6', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_b_frontier_sc_fewnerd",
    "field": "status",
    "value": "PREPARING",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python run_frontier_sc.py --from-hf --n-instances 200 --n-samples 8 --temperature 1.0 --seed 42', 'server': 'local (CPU-only, API calls)', 'data_path': 'HuggingFace: DFKI-SLT/few-nerd (supervised, test split)', 'data_count': 200, 'model_name': 'GPT-5.5 + Claude Opus 4.6', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-20T18:25:10.654291+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_b_frontier_sc_fewnerd\", \"experiment\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:19.266Z\", \"updated_at\": \"2026-05-20T18:24:49.540Z\", \"hypothesis\": \"The correlation-selection gap in structured self-consistency persists with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental limitation of frequency-based SC for structured prediction rather than a capability issue of smaller models.\", \"spec\": {\"command\": \"python run_frontier_sc.py --from-hf --n-instances 200 --n-samples 8 --temperature 1.0 --seed 42\", \"server\": \"local (CPU-only, API calls)\", \"data_path\": \"HuggingFace: DFKI-SLT/few-nerd (supervised, test split)\", \"data_count\": 200, \"model_name\": \"GPT-5.5 + Claude Opus 4.6\", \"seed\": 42}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.4066}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 119 · 2026-05-20T18:25:10.654461+00:00_

代码和 registry 已就绪。产出报告：

---

## 产出报告：exp_b_frontier_sc_fewnerd

### 代码路径
`artifacts/experiments/frontier_sc/run_frontier_sc.py`

### OpenRouter Model IDs
| Model | OpenRouter ID |
|---|---|
| GPT-5.5 | `openai/gpt-5.5` |
| Claude Opus 4.6 | `anthropic/claude-opus-4.6` |

### Cost 估算

| 项目 | 数值 |
|---|---|
| API calls | 200 inst × (1 greedy + 8 SC) × 2 models = **3,600 calls** |
| 每 call tokens | ~800 input + ~300 output |
| 总 input | ~2.88M tokens |
| 总 output | ~1.08M tokens |
| **GPT-5.5** | 1.44M × $5/M + 0.54M × $30/M = **$23.4** |
| **Claude Opus 4.6** | 1.44M × $5/M + 0.54M × $25/M = **$20.7** |
| **总计** | **~$44** |

### 依赖
```
openai          # OpenAI SDK (兼容 OpenRouter)
numpy
scipy
datasets        # 仅 --from-hf 模式需要
```

### 运行方式
```bash
export OPENROUTER_API_KEY="[REDACTED]"

# 从 HuggingFace 加载数据
python run_frontier_sc.py --from-hf

# 或从本地 UIE JSONL 加载（可从服务器 scp）
python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl

# 只跑单个模型
python run_frontier_sc.py --from-hf --models gpt-5.5
```

### 关键设计
- **Greedy 独立调用**（T=0）与 **8 个 SC 样本**（T=1.0）分开
- **9 阈值 MV 扫描**（0.1-0.9），自动找最优阈值
- **每 10 个 instance checkpoint**，支持断点续跑（`--no-resume` 强制重新开始）
- **Failure mode 诊断**：degeneracy rate、high-agreement-wrong、low-agreement-correct
- **Spearman correlation**：agreement ↔ greedy F1、agreement ↔ MV F1
- Prompt 模板与项目 `zeroshot_prompts.py` 完全一致（带 type descriptions）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_exp_b_frontier_sc_20260520T181716"
}
```

</details>

---
