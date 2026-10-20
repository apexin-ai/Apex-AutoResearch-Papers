# analysis cohens kappa pairwise

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 0
- **Tool calls:** 37
- **Original source:** `logs/chats/worker_analysis_cohens_kappa_pairwise_20260522T133438.jsonl`
- **Structured JSON:** [`42ff0cf0adf20c02cef6.json`](../../sessions/42/42ff0cf0adf20c02cef6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

75 recorded events

### Tool call

_source line 1 · 2026-05-22T13:40:09.744019+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-22T13:40:09.744317+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T13:40:09.744524+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/autodl-tmp/nlp_variance_gtheory/results/exp002/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/autodl-tmp/nlp_variance_gtheory/results/exp002/"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T13:40:09.744673+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/nlp_variance_gtheory/results/exp002/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T13:40:09.744798+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root/autodl-tmp/nlp_variance_gtheory/results/ -maxdepth 2 -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root/autodl-tmp/nlp_variance_gtheory/results/ -maxdepth 2 -type d"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T13:40:09.744920+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/autodl-tmp/nlp_variance_gtheory/results/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T13:40:09.745036+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root -maxdepth 3 -name \"*.jsonl\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root -maxdepth 3 -name \"*.jsonl\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T13:40:09.745156+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/results/all_results.jsonl\\n/root/nlp_variance_gtheory/results/float32_results.jsonl\\n/root/nlp_variance_gtheory/results/bf16_eager_results.jsonl\\n/root/nlp_variance_gtheory/results/dryrun_exp001.jsonl\\n/root/nlp_variance_gtheory/results/exp003_scale_7b_mmlu.jsonl\\n/root/nlp_variance_gtheory/results/exp003_scale_3b_mmlu.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T13:40:09.745306+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "find /root -maxdepth 4 -name \"*exp002*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "find /root -maxdepth 4 -name \"*exp002*\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T13:40:09.745444+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/nlp_variance_gtheory/results/"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T13:40:09.745572+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/nlp_variance_gtheory/data/gsm8k_items_exp002.json\\n/root/nlp_variance_gtheory/data/arc_items_exp002.json\\n/root/nlp_variance_gtheory/data/hellaswag_items_exp002.json\\n/root/nlp_variance_gtheory/data/math_items_exp002.json\\n/root/nlp_variance_gtheory/results/analysis/exp002_prep_report.md\\n/root/nlp_variance_gtheory/results/analysis/exp002_per_benchmark_gstudy.json\\n/root/nlp_variance_gtheory/results/exp002/design_matrix_exp002_full.csv\\n/root/nlp_variance_gtheory/scripts/dry_run_exp002.py\\n/root/nlp_variance_gtheory/scripts/prepare_few_shot_exp002.py\\n/root/nlp_variance_gtheory/scripts/run_exp002_pilot.sh\\n/root/nlp_variance_gtheory/scripts/run_exp002_full.sh\\n/root/nlp_variance_gtheory/scripts/post_exp002_master.sh\\n/root/nlp_variance_gtheory/design_matrix_exp002.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T13:40:09.745712+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"all_results.jsonl\\nanalysis\\nbf16_eager_results.jsonl\\nd_study_results.json\\nd_study_results_text.json\\ndesign_matrix_exp001_full.csv\\ndryrun_exp001.jsonl\\nexp001_analysis\\nexp001_bf16_2temp_comparison.json\\nexp001_gemma\\nexp001_gemma_fp32\\nexp001_llama\\nexp001_mistral\\nexp001_pilot\\nexp001_qwen\\nexp001b\\nexp002\\nexp002_pilot\\nexp003_scale_3b_mmlu.jsonl\\nexp003_scale_7b_mmlu.jsonl\\nexp003_scale_crossed_gstudy_test.json\\nexp003_scale_gstudy.json\\nexp004_8model_analysis\\nfigures\\nfloat32_results.jsonl\\nhenderson_i_unified_numbers.json\\nsanity_check.json\\nvariance_components.json\\nvariance_components_text.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T13:40:09.745832+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/results/exp002/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/nlp_variance_gtheory/results/exp002/"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T13:40:09.745975+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"chain_deepseek.log\\nchain_internlm.log\\ndeepseek_arc.jsonl\\ndeepseek_gsm8k.jsonl\\ndeepseek_hellaswag.jsonl\\ndeepseek_math.jsonl\\ndeepseek_math_gpu2.jsonl\\ndeepseek_mmlu.jsonl\\ndesign_matrix_exp002_full.csv\\ndesign_matrix_new_models.csv\\nfull_run.log\\ngemma_arc.jsonl\\ngemma_gsm8k.jsonl\\ngemma_hellaswag.jsonl\\ngemma_math.jsonl\\ngemma_mmlu.jsonl\\ngpu0_internlm_math.log\\ngpu0_qwen.log\\ngpu1_internlm_arc.log\\ngpu1_internlm_gsm8k.log\\ngpu1_internlm_hellaswag.log\\ngpu1_internlm_mmlu.log\\ngpu1_llama.log\\ngpu2_deepseek_math.log\\ngpu2_gemma.log\\ngpu3_deepseek_arc.log\\ngpu3_deepseek_gsm8k.log\\ngpu3_deepseek_hellaswag.log\\ngpu3_deepseek_mmlu.log\\ngpu3_mistral.log\\ninternlm_arc.jsonl\\ninternlm_gsm8k.jsonl\\ninternlm_hellaswag.jsonl\\ninternlm_math.jsonl\\ninternlm_mmlu.jsonl\\nllama_arc.jsonl\\nllama_gsm8k.jsonl\\nllama_hellaswag.jsonl\\nllama_math.jsonl\\nllama_mmlu.jsonl\\nmath_then_new_models.log\\nmistral_arc.jsonl\\nmistral_gsm8k.jsonl\\nmistral_hellaswag.jsonl\\nmistral_math.jsonl\\nmistral_mmlu.jsonl\\nolmo_arc.jsonl\\nolmo_gsm8k.jsonl\\nolmo_math.jsonl\\nolmo_mmlu.jsonl\\nqwen_arc.jsonl\\nqwen_gsm8k.jsonl\\nqwen_hellaswag.jsonl\\nqwen_math.jsonl\\nqwen_mmlu.jsonl\\nshard_0_qwen.csv\\nshard_1_llama.csv\\nshard_2_gemma.csv\\nshard_3_mistral.csv\\nshard_deepseek_arc.csv\\nshard_deepseek_gsm8k.csv\\nshard_deepseek_hellaswag.csv\\nshard_deepseek_math.csv\\nshard_deepseek_mmlu.csv\\nshard_gemma_arc.csv\\nshard_gemma_gsm8k.csv\\nshard_gemma_hellaswag.csv\\nshard_gemma_math.csv\\nshard_gemma_mmlu.csv\\nshard_internlm_arc.csv\\nshard_internlm_gsm8k.csv\\nshard_internlm_hellaswag.csv\\nshard_internlm_math.csv\\nshard_internlm_mmlu.csv\\nshard_llama_arc.csv\\nshard_llama_gsm8k.csv\\nshard_llama_hellaswag.csv\\nshard_llama_math.csv\\nshard_llama_mmlu.csv\\nshard_mistral_arc.csv\\nshard_mistral_gsm8k.csv\\nshard_mistral_hellaswag.csv\\nshard_mistral_math.csv\\nshard_mistral_mmlu.csv\\nshard_qwen_ar
…[truncated 270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T13:40:09.746113+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "ls /root/nlp_variance_gtheory/results/exp004_8model_analysis/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "ls /root/nlp_variance_gtheory/results/exp004_8model_analysis/"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T13:40:09.746246+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"binary_sim_ranking_consistency.json\\nbootstrap_ci_arc.json\\nbootstrap_ci_gsm8k.json\\nbootstrap_ci_hellaswag.json\\nbootstrap_ci_math.json\\nbootstrap_ci_mmlu.json\\nclean_permutation_test.json\\ncross_benchmark_difficulty_heterogeneity.json\\ncross_model_gstudy_8model.json\\ndeepseek_lomo_cross_benchmark.json\\ndefensive_analyses.json\\ndifficulty_vs_item_variance.pdf\\ndifficulty_vs_item_variance.png\\ndstudy_8model.json\\ndstudy_arc.json\\ndstudy_bootstrap_ci.json\\ndstudy_gsm8k.json\\ndstudy_hellaswag.json\\ndstudy_math.json\\nfig1_variance_decomposition.pdf\\nfig1_variance_decomposition.png\\ngitem_consistency_check.json\\nitem_heterogeneity_scatter.png\\nitem_heterogeneity_verification.json\\nlobo_stability.json\\nlomo_8model_mmlu.json\\nmath_8model_verified.json\\nmmlu_subject_gradient_8model.json\\nper_benchmark_gstudy_arc.json\\nper_benchmark_gstudy_ff.json\\nper_benchmark_gstudy_hellaswag.json\\nper_benchmark_gstudy_hellaswag_2temp.json\\nper_benchmark_gstudy_mc.json\\nper_benchmark_gstudy_mmlu.json\\npermutation_test_5bm.json\\nsingle_condition_dstudy.json\\nstratified_bootstrap_comparison.json\\nthree_in_one_8model.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T13:40:09.746406+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -3 /root/nlp_variance_gtheory/results/exp002/llama_mmlu.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -3 /root/nlp_variance_gtheory/results/exp002/llama_mmlu.jsonl"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-22T13:40:09.746530+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -3 /root/nlp_variance_gtheory/results/exp002/llama_gsm8k.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -3 /root/nlp_variance_gtheory/results/exp002/llama_gsm8k.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T13:40:09.746692+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"condition_id\\\": 1153, \\\"item_id\\\": \\\"abstract_algebra_81\\\", \\\"benchmark\\\": \\\"mmlu\\\", \\\"subject\\\": \\\"abstract_algebra\\\", \\\"model\\\": \\\"meta-llama/Llama-3.1-8B-Instruct\\\", \\\"precision\\\": \\\"bfloat16\\\", \\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1, \\\"generated_text\\\": \\\"A\\\\n\\\\nStatement 1 | If G is a finite group and H is a\\\", \\\"predicted_answer\\\": \\\"A\\\", \\\"gold_answer\\\": \\\"D\\\", \\\"correct\\\": 0, \\\"text_exact_match\\\": 0, \\\"latency_ms\\\": 24.23, \\\"answer_logprob\\\": -0.8737277984619141, \\\"top_logprobs\\\": {\\\" A\\\": -0.8737277984619141, \\\" C\\\": -1.373727798461914, \\\" B\\\": -1.498727798461914, \\\" D\\\": -2.248727798461914, \\\" \\\": -9.373727798461914}}\\n{\\\"condition_id\\\": 1153, \\\"item_id\\\": \\\"abstract_algebra_14\\\", \\\"benchmark\\\": \\\"mmlu\\\", \\\"subject\\\": \\\"abstract_algebra\\\", \\\"model\\\": \\\"meta-llama/Llama-3.1-8B-Instruct\\\", \\\"precision\\\": \\\"bfloat16\\\", \\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1, \\\"generated_text\\\": \\\"D\\\\n\\\\nStatement 1 | If a and b are elements of a group G\\\", \\\"predicted_answer\\\": \\\"D\\\", \\\"gold_answer\\\": \\\"C\\\", \\\"correct\\\": 0, \\\"text_exact_match\\\": 0, \\\"latency_ms\\\": 24.23, \\\"answer_logprob\\\": -0.7932339310646057, \\\"top_logprobs\\\": {\\\" D\\\": -0.7932339310646057, \\\" C\\\": -1.168233871459961, \\\" B\\\": -1.918233871459961, \\\" A\\\": -2.418233871459961, \\\" \\\": -8.168233871459961}}\\n{\\\"condition_id\\\": 1153, \\\"item_id\\\": \\\"abstract_algebra_3\\\", \\\"benchmark\\\": \\\"mmlu\\\", \\\"subject\\\": \\\"abstract_algebra\\\", \\\"model\\\": \\\"meta-llama/Llama-3.1-8B-Instruct\\\", \\\"precision\\\": \\\"bfloat16\\\", \\\"temperature\\\": 0.0, \\\"top_p\\\": nu
…[truncated 649 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T13:40:09.746892+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"condition_id\\\": 1441, \\\"item_id\\\": \\\"gsm8k_91\\\", \\\"benchmark\\\": \\\"gsm8k\\\", \\\"subject\\\": null, \\\"model\\\": \\\"meta-llama/Llama-3.1-8B-Instruct\\\", \\\"precision\\\": \\\"bfloat16\\\", \\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1, \\\"generated_text\\\": \\\"Cindy has 4 pets.\\\\nMarcia has 4 + 2 = 6 pets.\\\\nJan has 6 * 3 = 18 pets.\\\\nThe total number of pets is 4 + 6 + 18 = 28.\\\\nThe answer is 28.\\\", \\\"predicted_answer\\\": \\\"28\\\", \\\"gold_answer\\\": \\\"28\\\", \\\"correct\\\": 1, \\\"text_exact_match\\\": 0, \\\"latency_ms\\\": 112.62, \\\"answer_logprob\\\": -1.226076602935791, \\\"top_logprobs\\\": {\\\"C\\\": -1.226076602935791, \\\"Marc\\\": -1.226076602935791, \\\"First\\\": -2.476076602935791, \\\"Step\\\": -2.976076602935791, \\\"We\\\": -3.226076602935791}}\\n{\\\"condition_id\\\": 1441, \\\"item_id\\\": \\\"gsm8k_1239\\\", \\\"benchmark\\\": \\\"gsm8k\\\", \\\"subject\\\": null, \\\"model\\\": \\\"meta-llama/Llama-3.1-8B-Instruct\\\", \\\"precision\\\": \\\"bfloat16\\\", \\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1, \\\"generated_text\\\": \\\"First, we need to find out how many minutes they have to clean the classrooms in total. They have 5 days, and each day is 8 hours long. So, they have 5 * 8 = 40 hours. Since there are 60 minutes in an hour, they have 40 * 60 = 2400 minutes to clean the classrooms.\\\\nNext, we need to find out how many minutes it takes to clean all the classrooms. There are 80 classrooms, and it takes 15 minutes to clean each one. So, it takes 80 * 15 = 1200 minutes to clean all the classrooms.\\\\nNow, we need to find out what percentage of their day is spent cleaning classrooms. To do this, we need to divide the number of minutes spent cleaning classrooms (1200) by the total number of minutes the
…[truncated 1735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T13:40:09.747177+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "python3 -c \"\nimport json\nf = open('/root/nlp_variance_gtheory/results/exp002/llama_mmlu.jsonl')\nconds = set()\nfor line in f:\n    r = json.loads(line)\n    conds.add((r['temperature'], r['prompt_template'], r['seed'], r['ordering']))\nf.close()\nfor c in sorted(conds):\n    print(c)\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "python3 -c \"\nimport json\nf = open('/root/nlp_variance_gtheory/results/exp002/llama_mmlu.jsonl')\nconds = set()\nfor line in f:\n    r = json.loads(line)\n    conds.add((r['temperature'], r['prompt_template'], r['seed'], r['ordering']))\nf.close()\nfor c in sorted(conds):\n    print(c)\n\""
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T13:40:09.747354+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T13:40:09.747521+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "python3 -c \"\nimport json, os\nd = '/root/nlp_variance_gtheory/results/exp002/'\nfor f in sorted(os.listdir(d)):\n    if f.endswith('.jsonl'):\n        count = sum(1 for _ in open(d+f))\n        print(f'{f}: {count} rows')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "python3 -c \"\nimport json, os\nd = '/root/nlp_variance_gtheory/results/exp002/'\nfor f in sorted(os.listdir(d)):\n    if f.endswith('.jsonl'):\n        count = sum(1 for _ in open(d+f))\n        print(f'{f}: {count} rows')\n\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T13:40:09.747647+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T13:40:09.747761+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "wc -l /root/nlp_variance_gtheory/results/exp002/*.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "wc -l /root/nlp_variance_gtheory/results/exp002/*.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T13:40:09.747899+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"     57600 /root/nlp_variance_gtheory/results/exp002/deepseek_arc.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/deepseek_gsm8k.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/deepseek_hellaswag.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/deepseek_math.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/deepseek_math_gpu2.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/deepseek_mmlu.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/gemma_arc.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/gemma_gsm8k.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/gemma_hellaswag.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/gemma_math.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/gemma_mmlu.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/internlm_arc.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/internlm_gsm8k.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/internlm_hellaswag.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/internlm_math.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/internlm_mmlu.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/llama_arc.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/llama_gsm8k.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/llama_hellaswag.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/llama_math.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/llama_mmlu.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/mistral_arc.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/mistral_gsm8k.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/mistral_hellaswag.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/mistral_math.jsonl\\n     57600 /root/nlp_variance_gtheory/results/exp002/mistral_mmlu.jsonl\\
…[truncated 1043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T13:40:09.748038+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_mmlu.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_mmlu.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T13:40:09.748160+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"200\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T13:40:09.748308+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_arc.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_arc.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T13:40:09.748447+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"200\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-22T13:40:09.748564+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_gsm8k.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_gsm8k.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T13:40:09.748679+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"200\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-22T13:40:09.748794+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_hellaswag.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_hellaswag.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T13:40:09.748908+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"200\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-22T13:40:09.749017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_math.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "grep -c \"\\\"temperature\\\": 0.0, \\\"top_p\\\": null, \\\"prompt_template\\\": 1, \\\"seed\\\": 42, \\\"ordering\\\": 1\" /root/nlp_variance_gtheory/results/exp002/llama_math.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-22T13:40:09.749127+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"200\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-22T13:40:09.749278+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T13:40:09.749419+00:00_

data
figures

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-22T13:40:09.749587+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/scripts/exp004_cohens_kappa.py",
  "content": "\"\"\"\nCohen's kappa pairwise agreement + Fleiss' kappa for 8 models × 5 benchmarks.\nBaseline condition: temperature=0.0, prompt_template=1, seed=42, ordering=1.\n\"\"\"\nimport json\nimport os\nimport sys\nfrom itertools import combinations\nfrom collections import defaultdict\n\nDATA_DIR = \"/root/nlp_variance_gtheory/results/exp002\"\nOUTPUT_PATH = \"/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json\"\n\nMODEL_SHORTS = [\"llama\", \"gemma\", \"mistral\", \"qwen\", \"olmo\", \"yi\", \"internlm\", \"deepseek\"]\nBENCHMARKS = [\"mmlu\", \"arc\", \"gsm8k\", \"hellaswag\", \"math\"]\n\nBASELINE = {\"temperature\": 0.0, \"prompt_template\": 1, \"seed\": 42, \"ordering\": 1}\n\n\ndef load_baseline(model_short, benchmark):\n    \"\"\"Load item_id -> correct for baseline condition.\"\"\"\n    path = os.path.join(DATA_DIR, f\"{model_short}_{benchmark}.jsonl\")\n    if not os.path.exists(path):\n        return None\n    items = {}\n    with open(path) as f:\n        for line in f:\n            r = json.loads(line)\n            if (r[\"temperature\"] == BASELINE[\"temperature\"]\n                    and r[\"prompt_template\"] == BASELINE[\"prompt_template\"]\n                    and r[\"seed\"] == BASELINE[\"seed\"]\n                    and r[\"ordering\"] == BASELINE[\"ordering\"]):\n                items[r[\"item_id\"]] = r[\"correct\"]\n    return items\n\n\ndef cohens_kappa(labels_a, labels_b):\n    \"\"\"Compute Cohen's kappa for two binary label vectors (same length).\"\"\"\n    n = len(labels_a)\n    assert n == len(labels_b) and n > 0\n    agree = sum(a == b for a, b in zip(labels_a, labels_b))\n    po = agree / n\n    p1_a = sum(labels_a) / n\n    p1_b = sum(labels_b) / n\n    p0_a = 1 - p1_a\n    p0_b = 1 - p1_b\n    pe = p1_a * p1_b + p0_a * p0_b\n    if pe == 1.0:\n        return 1.0, po, pe\n    kappa = (po - pe) / (1 - pe)\n    return kappa, po, pe\n\n\ndef fleiss_kappa(ratings_matrix):\n    \"\"\"\n    Fleiss' kappa for binary ratings.\n    ratings_matrix: list of [n_raters_correct, n_raters_total] per item.\n    Equivalently: list of lists where each sublist is binary votes per rater.\n\n    Input: list of dicts {item_id: correct} for each rater,\n    but we'll compute from a matrix of (n_items x n_raters).\n    \"\"\"\n    # ratings_matrix: n_items x n_raters, values 0/1\n    n_items = len(ratings_matrix)\n    n_raters = len(ratings_matrix[0])\n\n    if n_items == 0 or n_raters < 2:\n        return None\n\n    # For each item, count category assignments\n    # Categories: 0 and 1\n    P_bar = 0.0\n    p_cat = [0.0, 0.0]  # proportion assigned to each category\n\n    for row in ratings_matrix:\n        n1 = sum(row)\n        n0 = n_raters - n1\n        P_bar += (n0 * (n0 - 1) + n1 * (n1 - 1)) / (n_raters * (n_raters - 1))\n        p_cat[0] += n0\n        p_cat[1] += n1\n\n    P_bar /= n_items\n    total_ratings = n_items * n_raters\n    p_cat[0] /= total_ratings\n    p_cat[1] /= total_ratings\n\n    Pe = p_cat[0] ** 2 + p_cat[1] ** 2\n\n    if Pe == 1.0:\n        return 1.0\n\n    return (P_bar - Pe) / (1 - Pe)\n\n\ndef get_model_display_name(short):\n    names = {\n        \"llama\": \"Llama-3.1-8B\",\n        \"gemma\": \"Gemma-2-9B\",\n        \"mistral\": \"Mistral-7B\",\n        \"qwen\": \"Qwen3-8B\",\n        \"olmo\": \"OLMo-2-7B\",\n        \"yi\": \"Yi-1.5-9B\",\n        \"internlm\": \"InternLM2.5-7B\",\n        \"deepseek\": \"DeepSeek-7B\",\n    }\n    return names.get(short, short)\n\n\ndef main():\n    results = {\n        \"method\": \"Cohen's kappa\",\n        \"condition\": \"baseline (T=0, P=1, S=42, O=1)\",\n        \"benchmarks\": {}\n    }\n\n    summary_rows = []\n\n    for bm in BENCHMARKS:\n        # Load all models for this benchmark\n        model_data = {}\n        for ms in MODEL_SHORTS:\n            data = load_baseline(ms, bm)\n            if data and len(data) > 0:\n                model_data[ms] = data\n\n        available_models = sorted(model_data.keys())\n        n_models = len(available_models)\n        print(f\"\\n{'='*60}\")\n        print(f\"Benchmark: {bm.upper()} — {n_models} models: {', '.join(get_model_display_name(m) for m in available_models)}\")\n\n        # Find common items across all models\n        common_items = set(model_data[available_models[0]].keys())\n        for ms in available_models[1:]:\n            common_items &= set(model_data[ms].keys())\n        common_items = sorted(common_items)\n        print(f\"Common items: {len(common_items)}\")\n\n        # Pairwise Cohen's kappa\n        pairs = []\n        for ma, mb in combinations(available_models, 2):\n            labels_a = [model_data[ma][item] for item in common_items]\n            labels_b = [model_data[mb][item] for item in common_items]\n            kappa, po, pe = cohens_kappa(labels_a, labels_b)\n            pairs.append({\n                \"model_a\": get_model_display_name(ma),\n                \"model_b\": get_model_display_name(mb),\n                \"kappa\": round(kappa, 4),\n                \"po\": round(po, 4),\n                \"pe\": round(pe, 4),\n            })\n\n        kappas = [p[\"kappa\"] for p in pairs]\n        mean_k = sum(kappas) / len(kappas)\n        min_k = min(kappas)\n        max_k = max(kappas)\n\n        # Fleiss' kappa\n        ratings_matrix = []\n        for item in common_items:\n            row = [model_data[ms][item] for ms in available_models]\n            ratings_matrix.append(row)\n        fk = fleiss_kappa(ratings_matrix)\n\n        results[\"benchmarks\"][bm] = {\n            \"n_models\": n_models,\n            \"n_pairs\": len(pairs),\n            \"n_items\": len(common_items),\n            \"mean_kappa\": round(mean_k, 4),\n            \"min_kappa\": round(min_k, 4),\n            \"max_kappa\": round(max_k, 4),\n            \"fleiss_kappa\": round(fk, 4) if fk is not None else None,\n            \"pairs\": sorted(pairs, key=lambda x: x[\"kappa\"]),\n        }\n\n        summary_rows.append((bm, n_models, len(common_items), len(pairs),\n                             mean_k, min_k, max_k, fk))\n\n        # Print top-3 and bottom-3\n        sorted_pairs = sorted(pairs, key=lambda x: x[\"kappa\"])\n        print(f\"  Mean κ={mean_k:.4f}, Min κ={min_k:.4f}, Max κ={max_k:.4f}, Fleiss κ={fk:.4f}\")\n        print(f\"  Lowest 3:\")\n        for p in sorted_pairs[:3]:\n            print(f\"    {p['model_a']:>16s} × {p['model_b']:<16s}  κ={p['kappa']:.4f}  po={p['po']:.4f}\")\n        print(f\"  Highest 3:\")\n        for p in sorted_pairs[-3:]:\n            print(f\"    {p['model_a']:>16s} × {p['model_b']:<16s}  κ={p['kappa']:.4f}  po={p['po']:.4f}\")\n\n    # Summary table\n    print(f\"\\n{'='*60}\")\n    print(f\"{'Benchmark':>12s} {'Models':>6s} {'Items':>6s} {'Pairs':>6s} {'Mean_κ':>8s} {'Min_κ':>8s} {'Max_κ':>8s} {'Fleiss_κ':>9s}\")\n    print(\"-\" * 70)\n    for row in summary_rows:\n        bm, nm, ni, np_, mk, mink, maxk, fk = row\n        print(f\"{bm:>12s} {nm:>6d} {ni:>6d} {np_:>6d} {mk:>8.4f} {mink:>8.4f} {maxk:>8.4f} {fk:>9.4f}\")\n\n    # Save\n    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)\n    with open(OUTPUT_PATH, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved to {OUTPUT_PATH}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/scripts/exp004_cohens_kappa.py",
    "content": "\"\"\"\nCohen's kappa pairwise agreement + Fleiss' kappa for 8 models × 5 benchmarks.\nBaseline condition: temperature=0.0, prompt_template=1, seed=42, ordering=1.\n\"\"\"\nimport json\nimport os\nimport sys\nfrom itertools import combinations\nfrom collections import defaultdict\n\nDATA_DIR = \"/root/nlp_variance_gtheory/results/exp002\"\nOUTPUT_PATH = \"/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json\"\n\nMODEL_SHORTS = [\"llama\", \"gemma\", \"mistral\", \"qwen\", \"olmo\", \"yi\", \"internlm\", \"deepseek\"]\nBENCHMARKS = [\"mmlu\", \"arc\", \"gsm8k\", \"hellaswag\", \"math\"]\n\nBASELINE = {\"temperature\": 0.0, \"prompt_template\": 1, \"seed\": 42, \"ordering\": 1}\n\n\ndef load_baseline(model_short, benchmark):\n    \"\"\"Load item_id -> correct for baseline condition.\"\"\"\n    path = os.path.join(DATA_DIR, f\"{model_short}_{benchmark}.jsonl\")\n    if not os.path.exists(path):\n        return None\n    items = {}\n    with open(path) as f:\n        for line in f:\n            r = json.loads(line)\n            if (r[\"temperature\"] == BASELINE[\"temperature\"]\n                    and r[\"prompt_template\"] == BASELINE[\"prompt_template\"]\n                    and r[\"seed\"] == BASELINE[\"seed\"]\n                    and r[\"ordering\"] == BASELINE[\"ordering\"]):\n                items[r[\"item_id\"]] = r[\"correct\"]\n    return items\n\n\ndef cohens_kappa(labels_a, labels_b):\n    \"\"\"Compute Cohen's kappa for two binary label vectors (same length).\"\"\"\n    n = len(labels_a)\n    assert n == len(labels_b) and n > 0\n    agree = sum(a == b for a, b in zip(labels_a, labels_b))\n    po = agree / n\n    p1_a = sum(labels_a) / n\n    p1_b = sum(labels_b) / n\n    p0_a = 1 - p1_a\n    p0_b = 1 - p1_b\n    pe = p1_a * p1_b + p0_a * p0_b\n    if pe == 1.0:\n        return 1.0, po, pe\n    kappa = (po - pe) / (1 - pe)\n    return kappa, po, pe\n\n\ndef fleiss_kappa(ratings_matrix):\n    \"\"\"\n    Fleiss' kappa for binary ratings.\n    ratings_matrix: list of [n_raters_correct, n_raters_total] per item.\n    Equivalently: list of lists where each sublist is binary votes per rater.\n\n    Input: list of dicts {item_id: correct} for each rater,\n    but we'll compute from a matrix of (n_items x n_raters).\n    \"\"\"\n    # ratings_matrix: n_items x n_raters, values 0/1\n    n_items = len(ratings_matrix)\n    n_raters = len(ratings_matrix[0])\n\n    if n_items == 0 or n_raters < 2:\n        return None\n\n    # For each item, count category assignments\n    # Categories: 0 and 1\n    P_bar = 0.0\n    p_cat = [0.0, 0.0]  # proportion assigned to each category\n\n    for row in ratings_matrix:\n        n1 = sum(row)\n        n0 = n_raters - n1\n        P_bar += (n0 * (n0 - 1) + n1 * (n1 - 1)) / (n_raters * (n_raters - 1))\n        p_cat[0] += n0\n        p_cat[1] += n1\n\n    P_bar /= n_items\n    total_ratings = n_items * n_raters\n    p_cat[0] /= total_ratings\n    p_cat[1] /= total_ratings\n\n    Pe = p_cat[0] ** 2 + p_cat[1] ** 2\n\n    if Pe == 1.0:\n        return 1.0\n\n    return (P_bar - Pe) / (1 - Pe)\n\n\ndef get_model_display_name(short):\n    names = {\n        \"llama\": \"Llama-3.1-8B\",\n        \"gemma\": \"Gemma-2-9B\",\n        \"mistral\": \"Mistral-7B\",\n        \"qwen\": \"Qwen3-8B\",\n        \"olmo\": \"OLMo-2-7B\",\n        \"yi\": \"Yi-1.5-9B\",\n        \"internlm\": \"InternLM2.5-7B\",\n        \"deepseek\": \"DeepSeek-7B\",\n    }\n    return names.get(short, short)\n\n\ndef main():\n    results = {\n        \"method\": \"Cohen's kappa\",\n        \"condition\": \"baseline (T=0, P=1, S=42, O=1)\",\n        \"benchmarks\": {}\n    }\n\n    summary_rows = []\n\n    for bm in BENCHMARKS:\n        # Load all models for this benchmark\n        model_data = {}\n        for ms in MODEL_SHORTS:\n            data = load_baseline(ms, bm)\n            if data and len(data) > 0:\n                model_data[ms] = data\n\n        available_models = sorted(model_data.keys())\n        n_models = len(available_models)\n        print(f\"\\n{'='*60}\")\n        print(f\"Benchmark: {bm.upper()} — {n_models} models: {', '.join(get_model_display_name(m) for m in available_models)}\")\n\n        # Find common items across all models\n        common_items = set(model_data[available_models[0]].keys())\n        for ms in available_models[1:]:\n            common_items &= set(model_data[ms].keys())\n        common_items = sorted(common_items)\n        print(f\"Common items: {len(common_items)}\")\n\n        # Pairwise Cohen's kappa\n        pairs = []\n        for ma, mb in combinations(available_models, 2):\n            labels_a = [model_data[ma][item] for item in common_items]\n            labels_b = [model_data[mb][item] for item in common_items]\n            kappa, po, pe = cohens_kappa(labels_a, labels_b)\n            pairs.append({\n                \"model_a\": get_model_display_name(ma),\n                \"model_b\": get_model_display_name(mb),\n                \"kappa\": round(kappa, 4),\n                \"po\": round(po, 4),\n                \"pe\": round(pe, 4),\n            })\n\n        kappas = [p[\"kappa\"] for p in pairs]\n        mean_k = sum(kappas) / len(kappas)\n        min_k = min(kappas)\n        max_k = max(kappas)\n\n        # Fleiss' kappa\n        ratings_matrix = []\n        for item in common_items:\n            row = [model_data[ms][item] for ms in available_models]\n            ratings_matrix.append(row)\n        fk = fleiss_kappa(ratings_matrix)\n\n        results[\"benchmarks\"][bm] = {\n            \"n_models\": n_models,\n            \"n_pairs\": len(pairs),\n            \"n_items\": len(common_items),\n            \"mean_kappa\": round(mean_k, 4),\n            \"min_kappa\": round(min_k, 4),\n            \"max_kappa\": round(max_k, 4),\n            \"fleiss_kappa\": round(fk, 4) if fk is not None else None,\n            \"pairs\": sorted(pairs, key=lambda x: x[\"kappa\"]),\n        }\n\n        summary_rows.append((bm, n_models, len(common_items), len(pairs),\n                             mean_k, min_k, max_k, fk))\n\n        # Print top-3 and bottom-3\n        sorted_pairs = sorted(pairs, key=lambda x: x[\"kappa\"])\n        print(f\"  Mean κ={mean_k:.4f}, Min κ={min_k:.4f}, Max κ={max_k:.4f}, Fleiss κ={fk:.4f}\")\n        print(f\"  Lowest 3:\")\n        for p in sorted_pairs[:3]:\n            print(f\"    {p['model_a']:>16s} × {p['model_b']:<16s}  κ={p['kappa']:.4f}  po={p['po']:.4f}\")\n        print(f\"  Highest 3:\")\n        for p in sorted_pairs[-3:]:\n            print(f\"    {p['model_a']:>16s} × {p['model_b']:<16s}  κ={p['kappa']:.4f}  po={p['po']:.4f}\")\n\n    # Summary table\n    print(f\"\\n{'='*60}\")\n    print(f\"{'Benchmark':>12s} {'Models':>6s} {'Items':>6s} {'Pairs':>6s} {'Mean_κ':>8s} {'Min_κ':>8s} {'Max_κ':>8s} {'Fleiss_κ':>9s}\")\n    print(\"-\" * 70)\n    for row in summary_rows:\n        bm, nm, ni, np_, mk, mink, maxk, fk = row\n        print(f\"{bm:>12s} {nm:>6d} {ni:>6d} {np_:>6d} {mk:>8.4f} {mink:>8.4f} {maxk:>8.4f} {fk:>9.4f}\")\n\n    # Save\n    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)\n    with open(OUTPUT_PATH, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved to {OUTPUT_PATH}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T13:40:09.749822+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/scripts/exp004_cohens_kappa.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-22T13:40:09.749980+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "cat > /root/nlp_variance_gtheory/scripts/exp004_cohens_kappa.py << 'PYEOF'\n\"\"\"\nCohen's kappa pairwise agreement + Fleiss' kappa for 8 models x 5 benchmarks.\nBaseline condition: temperature=0.0, prompt_template=1, seed=42, ordering=1.\n\"\"\"\nimport json\nimport os\nimport sys\nfrom itertools import combinations\nfrom collections import defaultdict\n\nDATA_DIR = \"/root/nlp_variance_gtheory/results/exp002\"\nOUTPUT_PATH = \"/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json\"\n\nMODEL_SHORTS = [\"llama\", \"gemma\", \"mistral\", \"qwen\", \"olmo\", \"yi\", \"internlm\", \"deepseek\"]\nBENCHMARKS = [\"mmlu\", \"arc\", \"gsm8k\", \"hellaswag\", \"math\"]\n\nBASELINE = {\"temperature\": 0.0, \"prompt_template\": 1, \"seed\": 42, \"ordering\": 1}\n\n\ndef load_baseline(model_short, benchmark):\n    path = os.path.join(DATA_DIR, f\"{model_short}_{benchmark}.jsonl\")\n    if not os.path.exists(path):\n        return None\n    items = {}\n    with open(path) as f:\n        for line in f:\n            r = json.loads(line)\n            if (r[\"temperature\"] == BASELINE[\"temperature\"]\n                    and r[\"prompt_template\"] == BASELINE[\"prompt_template\"]\n                    and r[\"seed\"] == BASELINE[\"seed\"]\n                    and r[\"ordering\"] == BASELINE[\"ordering\"]):\n                items[r[\"item_id\"]] = r[\"correct\"]\n    return items\n\n\ndef cohens_kappa(labels_a, labels_b):\n    n = len(labels_a)\n    assert n == len(labels_b) and n > 0\n    agree = sum(a == b for a, b in zip(labels_a, labels_b))\n    po = agree / n\n    p1_a = sum(labels_a) / n\n    p1_b = sum(labels_b) / n\n    p0_a = 1 - p1_a\n    p0_b = 1 - p1_b\n    pe = p1_a * p1_b + p0_a * p0_b\n    if pe == 1.0:\n        return 1.0, po, pe\n    kappa = (po - pe) / (1 - pe)\n    return kappa, po, pe\n\n\ndef fleiss_kappa(ratings_matrix):\n    n_items = len(ratings_matrix)\n    n_raters = len(ratings_matrix[0])\n    if n_items == 0 or n_raters < 2:\n        return None\n    P_bar = 0.0\n    p_cat = [0.0, 0.0]\n    for row in ratings_matrix:\n        n1 = sum(row)\n        n0 = n_raters - n1\n        P_bar += (n0 * (n0 - 1) + n1 * (n1 - 1)) / (n_raters * (n_raters - 1))\n        p_cat[0] += n0\n        p_cat[1] += n1\n    P_bar /= n_items\n    total_ratings = n_items * n_raters\n    p_cat[0] /= total_ratings\n    p_cat[1] /= total_ratings\n    Pe = p_cat[0] ** 2 + p_cat[1] ** 2\n    if Pe == 1.0:\n        return 1.0\n    return (P_bar - Pe) / (1 - Pe)\n\n\ndef get_model_display_name(short):\n    names = {\n        \"llama\": \"Llama-3.1-8B\",\n        \"gemma\": \"Gemma-2-9B\",\n        \"mistral\": \"Mistral-7B\",\n        \"qwen\": \"Qwen3-8B\",\n        \"olmo\": \"OLMo-2-7B\",\n        \"yi\": \"Yi-1.5-9B\",\n        \"internlm\": \"InternLM2.5-7B\",\n        \"deepseek\": \"DeepSeek-7B\",\n    }\n    return names.get(short, short)\n\n\ndef main():\n    results = {\n        \"method\": \"Cohen's kappa\",\n        \"condition\": \"baseline (T=0, P=1, S=42, O=1)\",\n        \"benchmarks\": {}\n    }\n    summary_rows = []\n\n    for bm in BENCHMARKS:\n        model_data = {}\n        for ms in MODEL_SHORTS:\n            data = load_baseline(ms, bm)\n            if data and len(data) > 0:\n                model_data[ms] = data\n\n        available_models = sorted(model_data.keys())\n        n_models = len(available_models)\n        print(f\"\\n{'='*60}\")\n        print(f\"Benchmark: {bm.upper()} -- {n_models} models: {', '.join(get_model_display_name(m) for m in available_models)}\")\n\n        common_items = set(model_data[available_models[0]].keys())\n        for ms in available_models[1:]:\n            common_items &= set(model_data[ms].keys())\n        common_items = sorted(common_items)\n        print(f\"Common items: {len(common_items)}\")\n\n        pairs = []\n        for ma, mb in combinations(available_models, 2):\n            labels_a = [model_data[ma][item] for item in common_items]\n            labels_b = [model_data[mb][item] for item in common_items]\n            kappa, po, pe = cohens_kappa(labels_a, labels_b)\n            pairs.append({\n                \"model_a\": get_model_display_name(ma),\n                \"model_b\": get_model_display_name(mb),\n                \"kappa\": round(kappa, 4),\n                \"po\": round(po, 4),\n                \"pe\": round(pe, 4),\n            })\n\n        kappas = [p[\"kappa\"] for p in pairs]\n        mean_k = sum(kappas) / len(kappas)\n        min_k = min(kappas)\n        max_k = max(kappas)\n\n        ratings_matrix = []\n        for item in common_items:\n            row = [model_data[ms][item] for ms in available_models]\n            ratings_matrix.append(row)\n        fk = fleiss_kappa(ratings_matrix)\n\n        results[\"benchmarks\"][bm] = {\n            \"n_models\": n_models,\n            \"n_pairs\": len(pairs),\n            \"n_items\": len(common_items),\n            \"mean_kappa\": round(mean_k, 4),\n            \"min_kappa\": round(min_k, 4),\n            \"max_kappa\": round(max_k, 4),\n            \"fleiss_kappa\": round(fk, 4) if fk is not None else None,\n            \"pairs\": sorted(pairs, key=lambda x: x[\"kappa\"]),\n        }\n        summary_rows.append((bm, n_models, len(common_items), len(pairs),\n                             mean_k, min_k, max_k, fk))\n\n        sorted_pairs = sorted(pairs, key=lambda x: x[\"kappa\"])\n        print(f\"  Mean k={mean_k:.4f}, Min k={min_k:.4f}, Max k={max_k:.4f}, Fleiss k={fk:.4f}\")\n        print(f\"  Lowest 3:\")\n        for p in sorted_pairs[:3]:\n            print(f\"    {p['model_a']:>16s} x {p['model_b']:<16s}  k={p['kappa']:.4f}  po={p['po']:.4f}\")\n        print(f\"  Highest 3:\")\n        for p in sorted_pairs[-3:]:\n            print(f\"    {p['model_a']:>16s} x {p['model_b']:<16s}  k={p['kappa']:.4f}  po={p['po']:.4f}\")\n\n    print(f\"\\n{'='*60}\")\n    print(f\"{'Benchmark':>12s} {'Models':>6s} {'Items':>6s} {'Pairs':>6s} {'Mean_k':>8s} {'Min_k':>8s} {'Max_k':>8s} {'Fleiss_k':>9s}\")\n    print(\"-\" * 70)\n    for row in summary_rows:\n        bm, nm, ni, np_, mk, mink, maxk, fk = row\n        print(f\"{bm:>12s} {nm:>6d} {ni:>6d} {np_:>6d} {mk:>8.4f} {mink:>8.4f} {maxk:>8.4f} {fk:>9.4f}\")\n\n    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)\n    with open(OUTPUT_PATH, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved to {OUTPUT_PATH}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat > /root/nlp_variance_gtheory/scripts/exp004_cohens_kappa.py << 'PYEOF'\n\"\"\"\nCohen's kappa pairwise agreement + Fleiss' kappa for 8 models x 5 benchmarks.\nBaseline condition: temperature=0.0, prompt_template=1, seed=42, ordering=1.\n\"\"\"\nimport json\nimport os\nimport sys\nfrom itertools import combinations\nfrom collections import defaultdict\n\nDATA_DIR = \"/root/nlp_variance_gtheory/results/exp002\"\nOUTPUT_PATH = \"/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json\"\n\nMODEL_SHORTS = [\"llama\", \"gemma\", \"mistral\", \"qwen\", \"olmo\", \"yi\", \"internlm\", \"deepseek\"]\nBENCHMARKS = [\"mmlu\", \"arc\", \"gsm8k\", \"hellaswag\", \"math\"]\n\nBASELINE = {\"temperature\": 0.0, \"prompt_template\": 1, \"seed\": 42, \"ordering\": 1}\n\n\ndef load_baseline(model_short, benchmark):\n    path = os.path.join(DATA_DIR, f\"{model_short}_{benchmark}.jsonl\")\n    if not os.path.exists(path):\n        return None\n    items = {}\n    with open(path) as f:\n        for line in f:\n            r = json.loads(line)\n            if (r[\"temperature\"] == BASELINE[\"temperature\"]\n                    and r[\"prompt_template\"] == BASELINE[\"prompt_template\"]\n                    and r[\"seed\"] == BASELINE[\"seed\"]\n                    and r[\"ordering\"] == BASELINE[\"ordering\"]):\n                items[r[\"item_id\"]] = r[\"correct\"]\n    return items\n\n\ndef cohens_kappa(labels_a, labels_b):\n    n = len(labels_a)\n    assert n == len(labels_b) and n > 0\n    agree = sum(a == b for a, b in zip(labels_a, labels_b))\n    po = agree / n\n    p1_a = sum(labels_a) / n\n    p1_b = sum(labels_b) / n\n    p0_a = 1 - p1_a\n    p0_b = 1 - p1_b\n    pe = p1_a * p1_b + p0_a * p0_b\n    if pe == 1.0:\n        return 1.0, po, pe\n    kappa = (po - pe) / (1 - pe)\n    return kappa, po, pe\n\n\ndef fleiss_kappa(ratings_matrix):\n    n_items = len(ratings_matrix)\n    n_raters = len(ratings_matrix[0])\n    if n_items == 0 or n_raters < 2:\n        return None\n    P_bar = 0.0\n    p_cat = [0.0, 0.0]\n    for row in ratings_matrix:\n        n1 = sum(row)\n        n0 = n_raters - n1\n        P_bar += (n0 * (n0 - 1) + n1 * (n1 - 1)) / (n_raters * (n_raters - 1))\n        p_cat[0] += n0\n        p_cat[1] += n1\n    P_bar /= n_items\n    total_ratings = n_items * n_raters\n    p_cat[0] /= total_ratings\n    p_cat[1] /= total_ratings\n    Pe = p_cat[0] ** 2 + p_cat[1] ** 2\n    if Pe == 1.0:\n        return 1.0\n    return (P_bar - Pe) / (1 - Pe)\n\n\ndef get_model_display_name(short):\n    names = {\n        \"llama\": \"Llama-3.1-8B\",\n        \"gemma\": \"Gemma-2-9B\",\n        \"mistral\": \"Mistral-7B\",\n        \"qwen\": \"Qwen3-8B\",\n        \"olmo\": \"OLMo-2-7B\",\n        \"yi\": \"Yi-1.5-9B\",\n        \"internlm\": \"InternLM2.5-7B\",\n        \"deepseek\": \"DeepSeek-7B\",\n    }\n    return names.get(short, short)\n\n\ndef main():\n    results = {\n        \"method\": \"Cohen's kappa\",\n        \"condition\": \"baseline (T=0, P=1, S=42, O=1)\",\n        \"benchmarks\": {}\n    }\n    summary_rows = []\n\n    for bm in BENCHMARKS:\n        model_data = {}\n        for ms in MODEL_SHORTS:\n            data = load_baseline(ms, bm)\n            if data and len(data) > 0:\n                model_data[ms] = data\n\n        available_models = sorted(model_data.keys())\n        n_models = len(available_models)\n        print(f\"\\n{'='*60}\")\n        print(f\"Benchmark: {bm.upper()} -- {n_models} models: {', '.join(get_model_display_name(m) for m in available_models)}\")\n\n        common_items = set(model_data[available_models[0]].keys())\n        for ms in available_models[1:]:\n            common_items &= set(model_data[ms].keys())\n        common_items = sorted(common_items)\n        print(f\"Common items: {len(common_items)}\")\n\n        pairs = []\n        for ma, mb in combinations(available_models, 2):\n            labels_a = [model_data[ma][item] for item in common_items]\n            labels_b = [model_data[mb][item] for item in common_items]\n            kappa, po, pe = cohens_kappa(labels_a, labels_b)\n            pairs.append({\n                \"model_a\": get_model_display_name(ma),\n                \"model_b\": get_model_display_name(mb),\n                \"kappa\": round(kappa, 4),\n                \"po\": round(po, 4),\n                \"pe\": round(pe, 4),\n            })\n\n        kappas = [p[\"kappa\"] for p in pairs]\n        mean_k = sum(kappas) / len(kappas)\n        min_k = min(kappas)\n        max_k = max(kappas)\n\n        ratings_matrix = []\n        for item in common_items:\n            row = [model_data[ms][item] for ms in available_models]\n            ratings_matrix.append(row)\n        fk = fleiss_kappa(ratings_matrix)\n\n        results[\"benchmarks\"][bm] = {\n            \"n_models\": n_models,\n            \"n_pairs\": len(pairs),\n            \"n_items\": len(common_items),\n            \"mean_kappa\": round(mean_k, 4),\n            \"min_kappa\": round(min_k, 4),\n            \"max_kappa\": round(max_k, 4),\n            \"fleiss_kappa\": round(fk, 4) if fk is not None else None,\n            \"pairs\": sorted(pairs, key=lambda x: x[\"kappa\"]),\n        }\n        summary_rows.append((bm, n_models, len(common_items), len(pairs),\n                             mean_k, min_k, max_k, fk))\n\n        sorted_pairs = sorted(pairs, key=lambda x: x[\"kappa\"])\n        print(f\"  Mean k={mean_k:.4f}, Min k={min_k:.4f}, Max k={max_k:.4f}, Fleiss k={fk:.4f}\")\n        print(f\"  Lowest 3:\")\n        for p in sorted_pairs[:3]:\n            print(f\"    {p['model_a']:>16s} x {p['model_b']:<16s}  k={p['kappa']:.4f}  po={p['po']:.4f}\")\n        print(f\"  Highest 3:\")\n        for p in sorted_pairs[-3:]:\n            print(f\"    {p['model_a']:>16s} x {p['model_b']:<16s}  k={p['kappa']:.4f}  po={p['po']:.4f}\")\n\n    print(f\"\\n{'='*60}\")\n    print(f\"{'Benchmark':>12s} {'Models':>6s} {'Items':>6s} {'Pairs':>6s} {'Mean_k':>8s} {'Min_k':>8s} {'Max_k':>8s} {'Fleiss_k':>9s}\")\n    print(\"-\" * 70)\n    for row in summary_rows:\n        bm, nm, ni, np_, mk, mink, maxk, fk = row\n        print(f\"{bm:>12s} {nm:>6d} {ni:>6d} {np_:>6d} {mk:>8.4f} {mink:>8.4f} {maxk:>8.4f} {fk:>9.4f}\")\n\n    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)\n    with open(OUTPUT_PATH, \"w\") as f:\n        json.dump(results, f, indent=2)\n    print(f\"\\nSaved to {OUTPUT_PATH}\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF\necho \"Script written OK\""
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T13:40:09.750160+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Script written OK\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-22T13:40:09.750281+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/nlp_variance_gtheory && python scripts/exp004_cohens_kappa.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/nlp_variance_gtheory && python scripts/exp004_cohens_kappa.py"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-22T13:40:09.750448+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n============================================================\\nBenchmark: MMLU -- 8 models: DeepSeek-7B, Gemma-2-9B, InternLM2.5-7B, Llama-3.1-8B, Mistral-7B, OLMo-2-7B, Qwen3-8B, Yi-1.5-9B\\nCommon items: 200\\n  Mean k=0.4606, Min k=0.2409, Max k=0.6115, Fleiss k=0.4558\\n  Lowest 3:\\n         DeepSeek-7B x InternLM2.5-7B    k=0.2409  po=0.6300\\n         DeepSeek-7B x Qwen3-8B          k=0.3402  po=0.6800\\n         DeepSeek-7B x Gemma-2-9B        k=0.3410  po=0.6800\\n  Highest 3:\\n      InternLM2.5-7B x Yi-1.5-9B         k=0.5575  po=0.8150\\n        Llama-3.1-8B x Yi-1.5-9B         k=0.5814  po=0.8250\\n      InternLM2.5-7B x Llama-3.1-8B      k=0.6115  po=0.8400\\n\\n============================================================\\nBenchmark: ARC -- 8 models: DeepSeek-7B, Gemma-2-9B, InternLM2.5-7B, Llama-3.1-8B, Mistral-7B, OLMo-2-7B, Qwen3-8B, Yi-1.5-9B\\nCommon items: 200\\n  Mean k=0.3764, Min k=0.0416, Max k=0.7408, Fleiss k=0.3312\\n  Lowest 3:\\n         DeepSeek-7B x Yi-1.5-9B         k=0.0416  po=0.5300\\n          Mistral-7B x Yi-1.5-9B         k=0.0768  po=0.5550\\n          Gemma-2-9B x Yi-1.5-9B         k=0.1185  po=0.5850\\n  Highest 3:\\n      InternLM2.5-7B x Llama-3.1-8B      k=0.6020  po=0.8900\\n        Llama-3.1-8B x OLMo-2-7B         k=0.6211  po=0.8750\\n          Gemma-2-9B x Llama-3.1-8B      k=0.7408  po=0.9300\\n\\n============================================================\\nBenchmark: GSM8K -- 8 models: DeepSeek-7B, Gemma-2-9B, InternLM2.5-7B, Llama-3.1-8B, Mistral-7B, OLMo-2-7B, Qwen3-8B, Yi-1.5-9B\\nCommon items: 200\\n  Mean k=0.3346, Min k=0.1165, Max k=0.5897, Fleiss k=0.3092\\n  Lowest 3:\\n         DeepSeek-7B x Qwen3-8B          k=0.1165  po=0.5450\\n          Mistral-7B x Qwen3-8B          k=0.1675  po=0.5650\\n         DeepSeek-7B x InternLM2.5-7B    k=0.1872  po=0.5850\\n  Highest 3:\\n      InternLM2.5-7B x Llama-3.1-8B      k=0.4983  po=0.8050\\n          Gemma
…[truncated 2361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-22T13:40:09.750611+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-22T13:40:09.750954+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"Cohen's kappa\\\",\\n  \\\"condition\\\": \\\"baseline (T=0, P=1, S=42, O=1)\\\",\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"n_models\\\": 8,\\n      \\\"n_pairs\\\": 28,\\n      \\\"n_items\\\": 200,\\n      \\\"mean_kappa\\\": 0.4606,\\n      \\\"min_kappa\\\": 0.2409,\\n      \\\"max_kappa\\\": 0.6115,\\n      \\\"fleiss_kappa\\\": 0.4558,\\n      \\\"pairs\\\": [\\n        {\\n          \\\"model_a\\\": \\\"DeepSeek-7B\\\",\\n          \\\"model_b\\\": \\\"InternLM2.5-7B\\\",\\n          \\\"kappa\\\": 0.2409,\\n          \\\"po\\\": 0.63,\\n          \\\"pe\\\": 0.5126\\n        },\\n        {\\n          \\\"model_a\\\": \\\"DeepSeek-7B\\\",\\n          \\\"model_b\\\": \\\"Qwen3-8B\\\",\\n          \\\"kappa\\\": 0.3402,\\n          \\\"po\\\": 0.68,\\n          \\\"pe\\\": 0.515\\n        },\\n        {\\n          \\\"model_a\\\": \\\"DeepSeek-7B\\\",\\n          \\\"model_b\\\": \\\"Gemma-2-9B\\\",\\n          \\\"kappa\\\": 0.341,\\n          \\\"po\\\": 0.68,\\n          \\\"pe\\\": 0.5144\\n        },\\n        {\\n          \\\"model_a\\\": \\\"InternLM2.5-7B\\\",\\n          \\\"model_b\\\": \\\"Mistral-7B\\\",\\n          \\\"kappa\\\": 0.3447,\\n          \\\"po\\\": 0.715,\\n          \\\"pe\\\": 0.5651\\n        },\\n        {\\n          \\\"model_a\\\": \\\"OLMo-2-7B\\\",\\n          \\\"model_b\\\": \\\"Qwen3-8B\\\",\\n          \\\"kappa\\\": 0.3714,\\n          \\\"po\\\": 0.725,\\n          \\\"pe\\\": 0.5625\\n        },\\n        {\\n          \\\"model_a\\\": \\\"Mistral-7B\\\",\\n          \\\"model_b\\\": \\\"Qwen3-8B\\\",\\n          \\\"kappa\\\": 0.3964,\\n          \\\"po\\\": 0.745,\\n          \\\"pe\\\": 0.5775\\n        },\\n        {\\n          \\\"model_a\\\": \\\"InternLM2.5-7B\\\",\\n          \\\"model_b\\\": \\\"OLMo-2-7B\\\",\\n          \\\"kappa\\\": 0.4078,\\n          \\\"po\\\": 0.735,\\n          \\\"pe\\\": 0.5525\\n
…[truncated 8949 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-22T13:40:09.751121+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "scp connect.westd.seetacloud.com:/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data/cohens_kappa_pairwise.json",
  "description": "Download kappa results JSON from server",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "Bash",
  "tool_args": {
    "command": "scp connect.westd.seetacloud.com:/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data/cohens_kappa_pairwise.json",
    "description": "Download kappa results JSON from server",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T13:40:09.751243+00:00_

Exit code 255
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
Permission denied, please try again.
ssh_askpass: exec(/usr/bin/ssh-askpass): No such file or directory
ubuntu@connect.westd.seetacloud.com: Permission denied ().
scp: Connection closed

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-22T13:40:09.751403+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T13:40:09.751529+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-22T13:40:09.751654+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "wc -c /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "wc -c /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T13:40:09.751772+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"22035 /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-22T13:40:09.751894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "head -200 /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "head -200 /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T13:40:09.752106+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"method\\\": \\\"Cohen's kappa\\\",\\n  \\\"condition\\\": \\\"baseline (T=0, P=1, S=42, O=1)\\\",\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"n_models\\\": 8,\\n      \\\"n_pairs\\\": 28,\\n      \\\"n_items\\\": 200,\\n      \\\"mean_kappa\\\": 0.4606,\\n      \\\"min_kappa\\\": 0.2409,\\n      \\\"max_kappa\\\": 0.6115,\\n      \\\"fleiss_kappa\\\": 0.4558,\\n      \\\"pairs\\\": [\\n        {\\n          \\\"model_a\\\": \\\"DeepSeek-7B\\\",\\n          \\\"model_b\\\": \\\"InternLM2.5-7B\\\",\\n          \\\"kappa\\\": 0.2409,\\n          \\\"po\\\": 0.63,\\n          \\\"pe\\\": 0.5126\\n        },\\n        {\\n          \\\"model_a\\\": \\\"DeepSeek-7B\\\",\\n          \\\"model_b\\\": \\\"Qwen3-8B\\\",\\n          \\\"kappa\\\": 0.3402,\\n          \\\"po\\\": 0.68,\\n          \\\"pe\\\": 0.515\\n        },\\n        {\\n          \\\"model_a\\\": \\\"DeepSeek-7B\\\",\\n          \\\"model_b\\\": \\\"Gemma-2-9B\\\",\\n          \\\"kappa\\\": 0.341,\\n          \\\"po\\\": 0.68,\\n          \\\"pe\\\": 0.5144\\n        },\\n        {\\n          \\\"model_a\\\": \\\"InternLM2.5-7B\\\",\\n          \\\"model_b\\\": \\\"Mistral-7B\\\",\\n          \\\"kappa\\\": 0.3447,\\n          \\\"po\\\": 0.715,\\n          \\\"pe\\\": 0.5651\\n        },\\n        {\\n          \\\"model_a\\\": \\\"OLMo-2-7B\\\",\\n          \\\"model_b\\\": \\\"Qwen3-8B\\\",\\n          \\\"kappa\\\": 0.3714,\\n          \\\"po\\\": 0.725,\\n          \\\"pe\\\": 0.5625\\n        },\\n        {\\n          \\\"model_a\\\": \\\"Mistral-7B\\\",\\n          \\\"model_b\\\": \\\"Qwen3-8B\\\",\\n          \\\"kappa\\\": 0.3964,\\n          \\\"po\\\": 0.745,\\n          \\\"pe\\\": 0.5775\\n        },\\n        {\\n          \\\"model_a\\\": \\\"InternLM2.5-7B\\\",\\n          \\\"model_b\\\": \\\"OLMo-2-7B\\\",\\n          \\\"kappa\\\": 0.4078,\\n          \\\"po\\\": 0.735,\\n          \\\"pe\\\": 0.5525\\n
…[truncated 4461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-22T13:40:09.752271+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "wc -l /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "wc -l /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T13:40:09.752410+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"949 /root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-22T13:40:09.752542+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json') as f:\n    data = json.load(f)\n# Write compact version\nwith open('/tmp/kappa_compact.json', 'w') as f:\n    json.dump(data, f, separators=(',', ':'))\nprint('OK')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json') as f:\n    data = json.load(f)\n# Write compact version\nwith open('/tmp/kappa_compact.json', 'w') as f:\n    json.dump(data, f, separators=(',', ':'))\nprint('OK')\n\""
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-22T13:40:09.752662+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"OK\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-22T13:40:09.752776+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /tmp/kappa_compact.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /tmp/kappa_compact.json"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-22T13:40:09.753161+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"method\\\":\\\"Cohen's kappa\\\",\\\"condition\\\":\\\"baseline (T=0, P=1, S=42, O=1)\\\",\\\"benchmarks\\\":{\\\"mmlu\\\":{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.4606,\\\"min_kappa\\\":0.2409,\\\"max_kappa\\\":0.6115,\\\"fleiss_kappa\\\":0.4558,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2409,\\\"po\\\":0.63,\\\"pe\\\":0.5126},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3402,\\\"po\\\":0.68,\\\"pe\\\":0.515},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.341,\\\"po\\\":0.68,\\\"pe\\\":0.5144},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3447,\\\"po\\\":0.715,\\\"pe\\\":0.5651},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3714,\\\"po\\\":0.725,\\\"pe\\\":0.5625},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3964,\\\"po\\\":0.745,\\\"pe\\\":0.5775},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4078,\\\"po\\\":0.735,\\\"pe\\\":0.5525},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4255,\\\"po\\\":0.72,\\\"pe\\\":0.5126},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4312,\\\"po\\\":0.75,\\\"pe\\\":0.5605},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4416,\\\"po\\\":0.725,\\\"pe\\\":0.5075},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4573,\\\"po\\\":0.735,\\\"pe\\\":0.5117},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4658,\\\"po\\\":0.785,\\\"pe\\\":0.5975},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.471,\\\"po\\\":0.
…[truncated 10043 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-22T13:40:09.753365+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-32570",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json') as f:\n    data = json.load(f)\n# Split into per-benchmark files\nfor bm in ['mmlu','arc','gsm8k','hellaswag','math']:\n    with open(f'/tmp/kappa_{bm}.json', 'w') as f:\n        json.dump(data['benchmarks'][bm], f, separators=(',', ':'))\nprint('Split OK')\n\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-32570",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/nlp_variance_gtheory/results/exp004_8model_analysis/cohens_kappa_pairwise.json') as f:\n    data = json.load(f)\n# Split into per-benchmark files\nfor bm in ['mmlu','arc','gsm8k','hellaswag','math']:\n    with open(f'/tmp/kappa_{bm}.json', 'w') as f:\n        json.dump(data['benchmarks'][bm], f, separators=(',', ':'))\nprint('Split OK')\n\""
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-22T13:40:09.753521+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Split OK\\n\", \"stderr\": \"Error while loading conda entry point: conda-libmamba-solver (module 'libmambapy' has no attribute 'QueryFormat')\\n\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.69}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-22T13:40:09.753641+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /tmp/kappa_arc.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /tmp/kappa_arc.json"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-22T13:40:09.753753+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /tmp/kappa_gsm8k.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /tmp/kappa_gsm8k.json"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-22T13:40:09.753946+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3764,\\\"min_kappa\\\":0.0416,\\\"max_kappa\\\":0.7408,\\\"fleiss_kappa\\\":0.3312,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.0416,\\\"po\\\":0.53,\\\"pe\\\":0.5096},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.0768,\\\"po\\\":0.555,\\\"pe\\\":0.518},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1185,\\\"po\\\":0.585,\\\"pe\\\":0.5292},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1221,\\\"po\\\":0.58,\\\"pe\\\":0.5216},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1412,\\\"po\\\":0.595,\\\"pe\\\":0.5284},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.147,\\\"po\\\":0.595,\\\"pe\\\":0.5252},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1497,\\\"po\\\":0.6,\\\"pe\\\":0.5296},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2647,\\\"po\\\":0.68,\\\"pe\\\":0.5648},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2888,\\\"po\\\":0.705,\\\"pe\\\":0.5852},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2947,\\\"po\\\":0.71,\\\"pe\\\":0.5888},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.3089,\\\"po\\\":0.715,\\\"pe\\\":0.5876},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3253,\\\"po\\\":0.775,\\\"pe\\\":0.6665},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.352,\\\"po\\\":0.725,\\\"pe\\\":0.5756},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3828,\\\"po\\\":0
…[truncated 1924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-22T13:40:09.754163+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3346,\\\"min_kappa\\\":0.1165,\\\"max_kappa\\\":0.5897,\\\"fleiss_kappa\\\":0.3092,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.1165,\\\"po\\\":0.545,\\\"pe\\\":0.485},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.1675,\\\"po\\\":0.565,\\\"pe\\\":0.4775},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.1872,\\\"po\\\":0.585,\\\"pe\\\":0.4894},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.2105,\\\"po\\\":0.595,\\\"pe\\\":0.487},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2145,\\\"po\\\":0.6,\\\"pe\\\":0.4908},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.2204,\\\"po\\\":0.595,\\\"pe\\\":0.4805},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2214,\\\"po\\\":0.745,\\\"pe\\\":0.6725},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2296,\\\"po\\\":0.6,\\\"pe\\\":0.4808},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2409,\\\"po\\\":0.61,\\\"pe\\\":0.4862},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2731,\\\"po\\\":0.625,\\\"pe\\\":0.4841},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2914,\\\"po\\\":0.75,\\\"pe\\\":0.6472},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.298,\\\"po\\\":0.64,\\\"pe\\\":0.4872},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3431,\\\"po\\\":0.775,\\\"pe\\\":0.6575},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.352,\\\"po\\\":0.755,
…[truncated 1920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-22T13:40:09.754337+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /tmp/kappa_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /tmp/kappa_mmlu.json"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-22T13:40:09.754480+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /tmp/kappa_hellaswag.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /tmp/kappa_hellaswag.json"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-22T13:40:09.754597+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-32570",
  "command": "cat /tmp/kappa_math.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-32570",
    "command": "cat /tmp/kappa_math.json"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-22T13:40:09.754786+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.4606,\\\"min_kappa\\\":0.2409,\\\"max_kappa\\\":0.6115,\\\"fleiss_kappa\\\":0.4558,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2409,\\\"po\\\":0.63,\\\"pe\\\":0.5126},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3402,\\\"po\\\":0.68,\\\"pe\\\":0.515},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.341,\\\"po\\\":0.68,\\\"pe\\\":0.5144},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3447,\\\"po\\\":0.715,\\\"pe\\\":0.5651},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3714,\\\"po\\\":0.725,\\\"pe\\\":0.5625},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3964,\\\"po\\\":0.745,\\\"pe\\\":0.5775},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4078,\\\"po\\\":0.735,\\\"pe\\\":0.5525},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4255,\\\"po\\\":0.72,\\\"pe\\\":0.5126},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4312,\\\"po\\\":0.75,\\\"pe\\\":0.5605},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4416,\\\"po\\\":0.725,\\\"pe\\\":0.5075},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4573,\\\"po\\\":0.735,\\\"pe\\\":0.5117},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4658,\\\"po\\\":0.785,\\\"pe\\\":0.5975},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.471,\\\"po\\\":0.785,\\\"pe\\\":0.5936},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.4739,\\\"po\\\
…[truncated 1918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-22T13:40:09.754979+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"n_models\\\":6,\\\"n_pairs\\\":15,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3318,\\\"min_kappa\\\":0.0977,\\\"max_kappa\\\":0.4818,\\\"fleiss_kappa\\\":0.3337,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.0977,\\\"po\\\":0.62,\\\"pe\\\":0.5789},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.1079,\\\"po\\\":0.665,\\\"pe\\\":0.6245},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.1341,\\\"po\\\":0.7,\\\"pe\\\":0.6536},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2247,\\\"po\\\":0.77,\\\"pe\\\":0.7034},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2397,\\\"po\\\":0.765,\\\"pe\\\":0.6909},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3384,\\\"po\\\":0.7,\\\"pe\\\":0.5465},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3531,\\\"po\\\":0.695,\\\"pe\\\":0.5285},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.3754,\\\"po\\\":0.715,\\\"pe\\\":0.5437},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.3977,\\\"po\\\":0.72,\\\"pe\\\":0.5352},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4021,\\\"po\\\":0.745,\\\"pe\\\":0.5735},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.42,\\\"po\\\":0.75,\\\"pe\\\":0.569},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4626,\\\"po\\\":0.78,\\\"pe\\\":0.5907},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4707,\\\"po\\\":0.795,\\\"pe\\\":0.6127},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4713
…[truncated 272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-22T13:40:09.755200+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3256,\\\"min_kappa\\\":0.0138,\\\"max_kappa\\\":0.6066,\\\"fleiss_kappa\\\":0.3246,\\\"pairs\\\":[{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.0138,\\\"po\\\":0.66,\\\"pe\\\":0.6552},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.1415,\\\"po\\\":0.53,\\\"pe\\\":0.4526},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1592,\\\"po\\\":0.655,\\\"pe\\\":0.5897},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2091,\\\"po\\\":0.64,\\\"pe\\\":0.5448},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2108,\\\"po\\\":0.57,\\\"pe\\\":0.4552},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.2256,\\\"po\\\":0.74,\\\"pe\\\":0.6642},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2343,\\\"po\\\":0.81,\\\"pe\\\":0.7518},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2393,\\\"po\\\":0.68,\\\"pe\\\":0.5794},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2487,\\\"po\\\":0.66,\\\"pe\\\":0.5474},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.2789,\\\"po\\\":0.7,\\\"pe\\\":0.5839},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.2965,\\\"po\\\":0.715,\\\"pe\\\":0.5949},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.3092,\\\"po\\\":0.695,\\\"pe\\\":0.5585},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3198,\\\"po\\\":0.64,\\\"pe\\\":0.4708},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.3232,\\\"po\\\
…[truncated 1912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-22T13:40:09.755472+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data && python3 -c \"\nimport json\n\nmmlu = json.loads('{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.4606,\\\"min_kappa\\\":0.2409,\\\"max_kappa\\\":0.6115,\\\"fleiss_kappa\\\":0.4558,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2409,\\\"po\\\":0.63,\\\"pe\\\":0.5126},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3402,\\\"po\\\":0.68,\\\"pe\\\":0.515},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.341,\\\"po\\\":0.68,\\\"pe\\\":0.5144},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3447,\\\"po\\\":0.715,\\\"pe\\\":0.5651},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3714,\\\"po\\\":0.725,\\\"pe\\\":0.5625},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3964,\\\"po\\\":0.745,\\\"pe\\\":0.5775},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4078,\\\"po\\\":0.735,\\\"pe\\\":0.5525},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4255,\\\"po\\\":0.72,\\\"pe\\\":0.5126},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4312,\\\"po\\\":0.75,\\\"pe\\\":0.5605},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4416,\\\"po\\\":0.725,\\\"pe\\\":0.5075},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4573,\\\"po\\\":0.735,\\\"pe\\\":0.5117},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4658,\\\"po\\\":0.785,\\\"pe\\\":0.5975},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.471,\\\"po\\\":0.785,\\\"pe\\\":0.5936},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.4739,\\\"po\\\":0.79,\\\"pe\\\":0.6008},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4739,\\\"po\\\":0.79,\\\"pe\\\":0.6008},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4749,\\\"po\\\":0.765,\\\"pe\\\":0.5525},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4886,\\\"po\\\":0.775,\\\"pe\\\":0.56},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4903,\\\"po\\\":0.77,\\\"pe\\\":0.5487},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5,\\\"po\\\":0.81,\\\"pe\\\":0.62},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.5014,\\\"po\\\":0.77,\\\"pe\\\":0.5388},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.5056,\\\"po\\\":0.785,\\\"pe\\\":0.5651},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.5183,\\\"po\\\":0.795,\\\"pe\\\":0.5744},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.519,\\\"po\\\":0.81,\\\"pe\\\":0.605},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.5211,\\\"po\\\":0.765,\\\"pe\\\":0.5093},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5443,\\\"po\\\":0.82,\\\"pe\\\":0.605},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.5575,\\\"po\\\":0.815,\\\"pe\\\":0.5819},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.5814,\\\"po\\\":0.825,\\\"pe\\\":0.5819},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.6115,\\\"po\\\":0.84,\\\"pe\\\":0.5882}]}')\n\narc = json.loads('{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3764,\\\"min_kappa\\\":0.0416,\\\"max_kappa\\\":0.7408,\\\"fleiss_kappa\\\":0.3312,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.0416,\\\"po\\\":0.53,\\\"pe\\\":0.5096},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.0768,\\\"po\\\":0.555,\\\"pe\\\":0.518},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1185,\\\"po\\\":0.585,\\\"pe\\\":0.5292},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1221,\\\"po\\\":0.58,\\\"pe\\\":0.5216},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1412,\\\"po\\\":0.595,\\\"pe\\\":0.5284},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.147,\\\"po\\\":0.595,\\\"pe\\\":0.5252},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1497,\\\"po\\\":0.6,\\\"pe\\\":0.5296},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2647,\\\"po\\\":0.68,\\\"pe\\\":0.5648},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2888,\\\"po\\\":0.705,\\\"pe\\\":0.5852},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2947,\\\"po\\\":0.71,\\\"pe\\\":0.5888},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.3089,\\\"po\\\":0.715,\\\"pe\\\":0.5876},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3253,\\\"po\\\":0.775,\\\"pe\\\":0.6665},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.352,\\\"po\\\":0.725,\\\"pe\\\":0.5756},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3828,\\\"po\\\":0.79,\\\"pe\\\":0.6597},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4283,\\\"po\\\":0.745,\\\"pe\\\":0.554},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.432,\\\"po\\\":0.785,\\\"pe\\\":0.6215},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4341,\\\"po\\\":0.81,\\\"pe\\\":0.6642},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4883,\\\"po\\\":0.845,\\\"pe\\\":0.6971},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4976,\\\"po\\\":0.82,\\\"pe\\\":0.6417},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5003,\\\"po\\\":0.85,\\\"pe\\\":0.6998},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5154,\\\"po\\\":0.885,\\\"pe\\\":0.7627},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5317,\\\"po\\\":0.875,\\\"pe\\\":0.7331},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.5621,\\\"po\\\":0.865,\\\"pe\\\":0.6917},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.5848,\\\"po\\\":0.9,\\\"pe\\\":0.7591},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5868,\\\"po\\\":0.905,\\\"pe\\\":0.7701},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.602,\\\"po\\\":0.89,\\\"pe\\\":0.7236},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.6211,\\\"po\\\":0.875,\\\"pe\\\":0.6701},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.7408,\\\"po\\\":0.93,\\\"pe\\\":0.7299}]}')\n\ngsm8k = json.loads('{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3346,\\\"min_kappa\\\":0.1165,\\\"max_kappa\\\":0.5897,\\\"fleiss_kappa\\\":0.3092,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.1165,\\\"po\\\":0.545,\\\"pe\\\":0.485},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.1675,\\\"po\\\":0.565,\\\"pe\\\":0.4775},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.1872,\\\"po\\\":0.585,\\\"pe\\\":0.4894},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.2105,\\\"po\\\":0.595,\\\"pe\\\":0.487},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2145,\\\"po\\\":0.6,\\\"pe\\\":0.4908},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.2204,\\\"po\\\":0.595,\\\"pe\\\":0.4805},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2214,\\\"po\\\":0.745,\\\"pe\\\":0.6725},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2296,\\\"po\\\":0.6,\\\"pe\\\":0.4808},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2409,\\\"po\\\":0.61,\\\"pe\\\":0.4862},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2731,\\\"po\\\":0.625,\\\"pe\\\":0.4841},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2914,\\\"po\\\":0.75,\\\"pe\\\":0.6472},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.298,\\\"po\\\":0.64,\\\"pe\\\":0.4872},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3431,\\\"po\\\":0.775,\\\"pe\\\":0.6575},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.352,\\\"po\\\":0.755,\\\"pe\\\":0.6219},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3562,\\\"po\\\":0.67,\\\"pe\\\":0.4874},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3693,\\\"po\\\":0.81,\\\"pe\\\":0.6988},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.381,\\\"po\\\":0.775,\\\"pe\\\":0.6365},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.3866,\\\"po\\\":0.785,\\\"pe\\\":0.6495},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.3898,\\\"po\\\":0.8,\\\"pe\\\":0.6722},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.3902,\\\"po\\\":0.69,\\\"pe\\\":0.4916},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4038,\\\"po\\\":0.845,\\\"pe\\\":0.74},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4146,\\\"po\\\":0.85,\\\"pe\\\":0.7437},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4186,\\\"po\\\":0.71,\\\"pe\\\":0.5012},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4298,\\\"po\\\":0.77,\\\"pe\\\":0.5966},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.4703,\\\"po\\\":0.825,\\\"pe\\\":0.6696},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4983,\\\"po\\\":0.805,\\\"pe\\\":0.6113},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.5034,\\\"po\\\":0.855,\\\"pe\\\":0.708},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.5897,\\\"po\\\":0.85,\\\"pe\\\":0.6344}]}')\n\nhellaswag = json.loads('{\\\"n_models\\\":6,\\\"n_pairs\\\":15,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3318,\\\"min_kappa\\\":0.0977,\\\"max_kappa\\\":0.4818,\\\"fleiss_kappa\\\":0.3337,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.0977,\\\"po\\\":0.62,\\\"pe\\\":0.5789},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.1079,\\\"po\\\":0.665,\\\"pe\\\":0.6245},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.1341,\\\"po\\\":0.7,\\\"pe\\\":0.6536},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2247,\\\"po\\\":0.77,\\\"pe\\\":0.7034},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2397,\\\"po\\\":0.765,\\\"pe\\\":0.6909},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3384,\\\"po\\\":0.7,\\\"pe\\\":0.5465},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3531,\\\"po\\\":0.695,\\\"pe\\\":0.5285},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.3754,\\\"po\\\":0.715,\\\"pe\\\":0.5437},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.3977,\\\"po\\\":0.72,\\\"pe\\\":0.5352},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4021,\\\"po\\\":0.745,\\\"pe\\\":0.5735},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.42,\\\"po\\\":0.75,\\\"pe\\\":0.569},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4626,\\\"po\\\":0.78,\\\"pe\\\":0.5907},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4707,\\\"po\\\":0.795,\\\"pe\\\":0.6127},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4713,\\\"po\\\":0.765,\\\"pe\\\":0.5555},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4818,\\\"po\\\":0.785,\\\"pe\\\":0.5851}]}')\n\nmath = json.loads('{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3256,\\\"min_kappa\\\":0.0138,\\\"max_kappa\\\":0.6066,\\\"fleiss_kappa\\\":0.3246,\\\"pairs\\\":[{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.0138,\\\"po\\\":0.66,\\\"pe\\\":0.6552},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.1415,\\\"po\\\":0.53,\\\"pe\\\":0.4526},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1592,\\\"po\\\":0.655,\\\"pe\\\":0.5897},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2091,\\\"po\\\":0.64,\\\"pe\\\":0.5448},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2108,\\\"po\\\":0.57,\\\"pe\\\":0.4552},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.2256,\\\"po\\\":0.74,\\\"pe\\\":0.6642},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2343,\\\"po\\\":0.81,\\\"pe\\\":0.7518},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2393,\\\"po\\\":0.68,\\\"pe\\\":0.5794},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2487,\\\"po\\\":0.66,\\\"pe\\\":0.5474},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.2789,\\\"po\\\":0.7,\\\"pe\\\":0.5839},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.2965,\\\"po\\\":0.715,\\\"pe\\\":0.5949},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.3092,\\\"po\\\":0.695,\\\"pe\\\":0.5585},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3198,\\\"po\\\":0.64,\\\"pe\\\":0.4708},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.3232,\\\"po\\\":0.755,\\\"pe\\\":0.638},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.3304,\\\"po\\\":0.7,\\\"pe\\\":0.552},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3397,\\\"po\\\":0.66,\\\"pe\\\":0.485},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.353,\\\"po\\\":0.71,\\\"pe\\\":0.5517},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.3644,\\\"po\\\":0.775,\\\"pe\\\":0.646},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.384,\\\"po\\\":0.71,\\\"pe\\\":0.5292},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.3943,\\\"po\\\":0.725,\\\"pe\\\":0.546},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4099,\\\"po\\\":0.695,\\\"pe\\\":0.4831},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4101,\\\"po\\\":0.715,\\\"pe\\\":0.5169},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4202,\\\"po\\\":0.695,\\\"pe\\\":0.474},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4268,\\\"po\\\":0.765,\\\"pe\\\":0.59},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.464,\\\"po\\\":0.74,\\\"pe\\\":0.515},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4788,\\\"po\\\":0.755,\\\"pe\\\":0.5299},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.5253,\\\"po\\\":0.775,\\\"pe\\\":0.526},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.6066,\\\"po\\\":0.8,\\\"pe\\\":0.4915}]}')\n\nresult = {\n    'method': \\\"Cohen's kappa\\\",\n    'condition': 'baseline (T=0, P=1, S=42, O=1)',\n    'benchmarks': {\n        'mmlu': mmlu,\n        'arc': arc,\n        'gsm8k': gsm8k,\n        'hellaswag': hellaswag,\n        'math': math,\n    }\n}\n\nwith open('cohens_kappa_pairwise.json', 'w') as f:\n    json.dump(result, f, indent=2)\nprint('Written OK')\n# Verify\nwith open('cohens_kappa_pairwise.json') as f:\n    d = json.load(f)\nfor bm in d['benchmarks']:\n    b = d['benchmarks'][bm]\n    print(f'{bm}: {b[\\\"n_models\\\"]} models, {b[\\\"n_pairs\\\"]} pairs, mean_k={b[\\\"mean_kappa\\\"]}, fleiss_k={b[\\\"fleiss_kappa\\\"]}')\n\"\n",
  "description": "Assemble full kappa JSON locally"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/exp004/data && python3 -c \"\nimport json\n\nmmlu = json.loads('{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.4606,\\\"min_kappa\\\":0.2409,\\\"max_kappa\\\":0.6115,\\\"fleiss_kappa\\\":0.4558,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2409,\\\"po\\\":0.63,\\\"pe\\\":0.5126},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3402,\\\"po\\\":0.68,\\\"pe\\\":0.515},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.341,\\\"po\\\":0.68,\\\"pe\\\":0.5144},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3447,\\\"po\\\":0.715,\\\"pe\\\":0.5651},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3714,\\\"po\\\":0.725,\\\"pe\\\":0.5625},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3964,\\\"po\\\":0.745,\\\"pe\\\":0.5775},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4078,\\\"po\\\":0.735,\\\"pe\\\":0.5525},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4255,\\\"po\\\":0.72,\\\"pe\\\":0.5126},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4312,\\\"po\\\":0.75,\\\"pe\\\":0.5605},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4416,\\\"po\\\":0.725,\\\"pe\\\":0.5075},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4573,\\\"po\\\":0.735,\\\"pe\\\":0.5117},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4658,\\\"po\\\":0.785,\\\"pe\\\":0.5975},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.471,\\\"po\\\":0.785,\\\"pe\\\":0.5936},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.4739,\\\"po\\\":0.79,\\\"pe\\\":0.6008},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4739,\\\"po\\\":0.79,\\\"pe\\\":0.6008},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4749,\\\"po\\\":0.765,\\\"pe\\\":0.5525},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4886,\\\"po\\\":0.775,\\\"pe\\\":0.56},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4903,\\\"po\\\":0.77,\\\"pe\\\":0.5487},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5,\\\"po\\\":0.81,\\\"pe\\\":0.62},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.5014,\\\"po\\\":0.77,\\\"pe\\\":0.5388},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.5056,\\\"po\\\":0.785,\\\"pe\\\":0.5651},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.5183,\\\"po\\\":0.795,\\\"pe\\\":0.5744},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.519,\\\"po\\\":0.81,\\\"pe\\\":0.605},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.5211,\\\"po\\\":0.765,\\\"pe\\\":0.5093},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5443,\\\"po\\\":0.82,\\\"pe\\\":0.605},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.5575,\\\"po\\\":0.815,\\\"pe\\\":0.5819},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.5814,\\\"po\\\":0.825,\\\"pe\\\":0.5819},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.6115,\\\"po\\\":0.84,\\\"pe\\\":0.5882}]}')\n\narc = json.loads('{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3764,\\\"min_kappa\\\":0.0416,\\\"max_kappa\\\":0.7408,\\\"fleiss_kappa\\\":0.3312,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.0416,\\\"po\\\":0.53,\\\"pe\\\":0.5096},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.0768,\\\"po\\\":0.555,\\\"pe\\\":0.518},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1185,\\\"po\\\":0.585,\\\"pe\\\":0.5292},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1221,\\\"po\\\":0.58,\\\"pe\\\":0.5216},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1412,\\\"po\\\":0.595,\\\"pe\\\":0.5284},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.147,\\\"po\\\":0.595,\\\"pe\\\":0.5252},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1497,\\\"po\\\":0.6,\\\"pe\\\":0.5296},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2647,\\\"po\\\":0.68,\\\"pe\\\":0.5648},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2888,\\\"po\\\":0.705,\\\"pe\\\":0.5852},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2947,\\\"po\\\":0.71,\\\"pe\\\":0.5888},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.3089,\\\"po\\\":0.715,\\\"pe\\\":0.5876},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3253,\\\"po\\\":0.775,\\\"pe\\\":0.6665},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.352,\\\"po\\\":0.725,\\\"pe\\\":0.5756},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3828,\\\"po\\\":0.79,\\\"pe\\\":0.6597},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4283,\\\"po\\\":0.745,\\\"pe\\\":0.554},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.432,\\\"po\\\":0.785,\\\"pe\\\":0.6215},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4341,\\\"po\\\":0.81,\\\"pe\\\":0.6642},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4883,\\\"po\\\":0.845,\\\"pe\\\":0.6971},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4976,\\\"po\\\":0.82,\\\"pe\\\":0.6417},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5003,\\\"po\\\":0.85,\\\"pe\\\":0.6998},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5154,\\\"po\\\":0.885,\\\"pe\\\":0.7627},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5317,\\\"po\\\":0.875,\\\"pe\\\":0.7331},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.5621,\\\"po\\\":0.865,\\\"pe\\\":0.6917},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.5848,\\\"po\\\":0.9,\\\"pe\\\":0.7591},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.5868,\\\"po\\\":0.905,\\\"pe\\\":0.7701},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.602,\\\"po\\\":0.89,\\\"pe\\\":0.7236},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.6211,\\\"po\\\":0.875,\\\"pe\\\":0.6701},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.7408,\\\"po\\\":0.93,\\\"pe\\\":0.7299}]}')\n\ngsm8k = json.loads('{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3346,\\\"min_kappa\\\":0.1165,\\\"max_kappa\\\":0.5897,\\\"fleiss_kappa\\\":0.3092,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.1165,\\\"po\\\":0.545,\\\"pe\\\":0.485},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.1675,\\\"po\\\":0.565,\\\"pe\\\":0.4775},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.1872,\\\"po\\\":0.585,\\\"pe\\\":0.4894},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.2105,\\\"po\\\":0.595,\\\"pe\\\":0.487},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2145,\\\"po\\\":0.6,\\\"pe\\\":0.4908},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.2204,\\\"po\\\":0.595,\\\"pe\\\":0.4805},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2214,\\\"po\\\":0.745,\\\"pe\\\":0.6725},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2296,\\\"po\\\":0.6,\\\"pe\\\":0.4808},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2409,\\\"po\\\":0.61,\\\"pe\\\":0.4862},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2731,\\\"po\\\":0.625,\\\"pe\\\":0.4841},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.2914,\\\"po\\\":0.75,\\\"pe\\\":0.6472},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.298,\\\"po\\\":0.64,\\\"pe\\\":0.4872},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3431,\\\"po\\\":0.775,\\\"pe\\\":0.6575},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.352,\\\"po\\\":0.755,\\\"pe\\\":0.6219},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3562,\\\"po\\\":0.67,\\\"pe\\\":0.4874},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3693,\\\"po\\\":0.81,\\\"pe\\\":0.6988},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.381,\\\"po\\\":0.775,\\\"pe\\\":0.6365},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.3866,\\\"po\\\":0.785,\\\"pe\\\":0.6495},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.3898,\\\"po\\\":0.8,\\\"pe\\\":0.6722},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.3902,\\\"po\\\":0.69,\\\"pe\\\":0.4916},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4038,\\\"po\\\":0.845,\\\"pe\\\":0.74},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4146,\\\"po\\\":0.85,\\\"pe\\\":0.7437},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4186,\\\"po\\\":0.71,\\\"pe\\\":0.5012},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4298,\\\"po\\\":0.77,\\\"pe\\\":0.5966},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.4703,\\\"po\\\":0.825,\\\"pe\\\":0.6696},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4983,\\\"po\\\":0.805,\\\"pe\\\":0.6113},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.5034,\\\"po\\\":0.855,\\\"pe\\\":0.708},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.5897,\\\"po\\\":0.85,\\\"pe\\\":0.6344}]}')\n\nhellaswag = json.loads('{\\\"n_models\\\":6,\\\"n_pairs\\\":15,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3318,\\\"min_kappa\\\":0.0977,\\\"max_kappa\\\":0.4818,\\\"fleiss_kappa\\\":0.3337,\\\"pairs\\\":[{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.0977,\\\"po\\\":0.62,\\\"pe\\\":0.5789},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.1079,\\\"po\\\":0.665,\\\"pe\\\":0.6245},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.1341,\\\"po\\\":0.7,\\\"pe\\\":0.6536},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2247,\\\"po\\\":0.77,\\\"pe\\\":0.7034},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2397,\\\"po\\\":0.765,\\\"pe\\\":0.6909},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3384,\\\"po\\\":0.7,\\\"pe\\\":0.5465},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.3531,\\\"po\\\":0.695,\\\"pe\\\":0.5285},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.3754,\\\"po\\\":0.715,\\\"pe\\\":0.5437},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.3977,\\\"po\\\":0.72,\\\"pe\\\":0.5352},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4021,\\\"po\\\":0.745,\\\"pe\\\":0.5735},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.42,\\\"po\\\":0.75,\\\"pe\\\":0.569},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4626,\\\"po\\\":0.78,\\\"pe\\\":0.5907},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4707,\\\"po\\\":0.795,\\\"pe\\\":0.6127},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.4713,\\\"po\\\":0.765,\\\"pe\\\":0.5555},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.4818,\\\"po\\\":0.785,\\\"pe\\\":0.5851}]}')\n\nmath = json.loads('{\\\"n_models\\\":8,\\\"n_pairs\\\":28,\\\"n_items\\\":200,\\\"mean_kappa\\\":0.3256,\\\"min_kappa\\\":0.0138,\\\"max_kappa\\\":0.6066,\\\"fleiss_kappa\\\":0.3246,\\\"pairs\\\":[{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.0138,\\\"po\\\":0.66,\\\"pe\\\":0.6552},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.1415,\\\"po\\\":0.53,\\\"pe\\\":0.4526},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.1592,\\\"po\\\":0.655,\\\"pe\\\":0.5897},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2091,\\\"po\\\":0.64,\\\"pe\\\":0.5448},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.2108,\\\"po\\\":0.57,\\\"pe\\\":0.4552},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.2256,\\\"po\\\":0.74,\\\"pe\\\":0.6642},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2343,\\\"po\\\":0.81,\\\"pe\\\":0.7518},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Mistral-7B\\\",\\\"kappa\\\":0.2393,\\\"po\\\":0.68,\\\"pe\\\":0.5794},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.2487,\\\"po\\\":0.66,\\\"pe\\\":0.5474},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Gemma-2-9B\\\",\\\"kappa\\\":0.2789,\\\"po\\\":0.7,\\\"pe\\\":0.5839},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.2965,\\\"po\\\":0.715,\\\"pe\\\":0.5949},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.3092,\\\"po\\\":0.695,\\\"pe\\\":0.5585},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3198,\\\"po\\\":0.64,\\\"pe\\\":0.4708},{\\\"model_a\\\":\\\"Mistral-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.3232,\\\"po\\\":0.755,\\\"pe\\\":0.638},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.3304,\\\"po\\\":0.7,\\\"pe\\\":0.552},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.3397,\\\"po\\\":0.66,\\\"pe\\\":0.485},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.353,\\\"po\\\":0.71,\\\"pe\\\":0.5517},{\\\"model_a\\\":\\\"DeepSeek-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.3644,\\\"po\\\":0.775,\\\"pe\\\":0.646},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Llama-3.1-8B\\\",\\\"kappa\\\":0.384,\\\"po\\\":0.71,\\\"pe\\\":0.5292},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.3943,\\\"po\\\":0.725,\\\"pe\\\":0.546},{\\\"model_a\\\":\\\"Qwen3-8B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4099,\\\"po\\\":0.695,\\\"pe\\\":0.4831},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4101,\\\"po\\\":0.715,\\\"pe\\\":0.5169},{\\\"model_a\\\":\\\"OLMo-2-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.4202,\\\"po\\\":0.695,\\\"pe\\\":0.474},{\\\"model_a\\\":\\\"Llama-3.1-8B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.4268,\\\"po\\\":0.765,\\\"pe\\\":0.59},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"InternLM2.5-7B\\\",\\\"kappa\\\":0.464,\\\"po\\\":0.74,\\\"pe\\\":0.515},{\\\"model_a\\\":\\\"Gemma-2-9B\\\",\\\"model_b\\\":\\\"Yi-1.5-9B\\\",\\\"kappa\\\":0.4788,\\\"po\\\":0.755,\\\"pe\\\":0.5299},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"OLMo-2-7B\\\",\\\"kappa\\\":0.5253,\\\"po\\\":0.775,\\\"pe\\\":0.526},{\\\"model_a\\\":\\\"InternLM2.5-7B\\\",\\\"model_b\\\":\\\"Qwen3-8B\\\",\\\"kappa\\\":0.6066,\\\"po\\\":0.8,\\\"pe\\\":0.4915}]}')\n\nresult = {\n    'method': \\\"Cohen's kappa\\\",\n    'condition': 'baseline (T=0, P=1, S=42, O=1)',\n    'benchmarks': {\n        'mmlu': mmlu,\n        'arc': arc,\n        'gsm8k': gsm8k,\n        'hellaswag': hellaswag,\n        'math': math,\n    }\n}\n\nwith open('cohens_kappa_pairwise.json', 'w') as f:\n    json.dump(result, f, indent=2)\nprint('Written OK')\n# Verify\nwith open('cohens_kappa_pairwise.json') as f:\n    d = json.load(f)\nfor bm in d['benchmarks']:\n    b = d['benchmarks'][bm]\n    print(f'{bm}: {b[\\\"n_models\\\"]} models, {b[\\\"n_pairs\\\"]} pairs, mean_k={b[\\\"mean_kappa\\\"]}, fleiss_k={b[\\\"fleiss_kappa\\\"]}')\n\"\n",
    "description": "Assemble full kappa JSON locally"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-22T13:40:09.755728+00:00_

Written OK
mmlu: 8 models, 28 pairs, mean_k=0.4606, fleiss_k=0.4558
arc: 8 models, 28 pairs, mean_k=0.3764, fleiss_k=0.3312
gsm8k: 8 models, 28 pairs, mean_k=0.3346, fleiss_k=0.3092
hellaswag: 6 models, 15 pairs, mean_k=0.3318, fleiss_k=0.3337
math: 8 models, 28 pairs, mean_k=0.3256, fleiss_k=0.3246

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 75 · 2026-05-22T13:40:09.755899+00:00_

All done. Summary:

| Benchmark | Models | Pairs | Mean κ | Min κ | Max κ | Fleiss κ |
|-----------|--------|-------|--------|-------|-------|----------|
| MMLU | 8 | 28 | 0.461 | 0.241 | 0.612 | 0.456 |
| ARC | 8 | 28 | 0.376 | 0.042 | 0.741 | 0.331 |
| GSM8K | 8 | 28 | 0.335 | 0.117 | 0.590 | 0.309 |
| HellaSwag | 6 | 15 | 0.332 | 0.098 | 0.482 | 0.334 |
| MATH | 8 | 28 | 0.326 | 0.014 | 0.607 | 0.325 |

Key findings:
- All κ values are positive (models agree more than chance), as expected
- MMLU has highest inter-model agreement (mean κ=0.46, "moderate"), likely because its MC format constrains variance
- MATH has lowest mean κ=0.33 ("fair") and widest range — Llama×Mistral κ=0.014 (near-random) while InternLM×Qwen κ=0.61
- ARC has the widest spread (0.04–0.74); Yi-1.5-9B is a consistent outlier with very low agreement against most models on ARC
- HellaSwag only has 6 models (OLMo/Yi missing)
- Fleiss κ tracks closely with mean pairwise κ across all benchmarks

Script saved at server `/root/nlp_variance_gtheory/scripts/exp004_cohens_kappa.py`, results at local `artifacts/exp004/data/cohens_kappa_pairwise.json`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_cohens_kappa_pairwise_20260522T133438"
}
```

</details>

---
