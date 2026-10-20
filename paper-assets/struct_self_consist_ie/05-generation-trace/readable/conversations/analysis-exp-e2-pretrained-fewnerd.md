# analysis exp e2 pretrained fewnerd

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/chats/worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620.jsonl`
- **Structured JSON:** [`b1157ff79c60e810b08c.json`](../../sessions/b1/b1157ff79c60e810b08c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

27 recorded events

### Tool call

_source line 1 · 2026-05-21T12:38:38.058217+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T12:38:38.058552+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T12:38:38.058738+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "tail -200 ~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "tail -200 ~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T12:38:38.058873+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_fewnerd/ -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_fewnerd/ -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T12:38:38.059000+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "filters": "{'exp_id': 'exp_e2_pretrained_fewnerd'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "filters": "{'exp_id': 'exp_e2_pretrained_fewnerd'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T12:38:38.059255+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 37648 test instances from fewnerd [index 0:None]\\nINFO 05-21 14:59:39 [utils.py:233] non-default args: {'max_model_len': 4096, 'disable_log_stats': True, 'model': '/root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct'}\\nINFO 05-21 14:59:39 [model.py:533] Resolved architecture: Qwen2ForCausalLM\\nINFO 05-21 14:59:39 [model.py:1582] Using max model len 4096\\nINFO 05-21 14:59:39 [scheduler.py:231] Chunked prefill is enabled with max_num_batched_tokens=8192.\\nINFO 05-21 14:59:39 [vllm.py:775] Asynchronous scheduling is enabled.\\n(EngineCore pid=8696) INFO 05-21 14:59:40 [core.py:103] Initializing a V1 LLM engine (v0.18.1) with config: model='/root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct', speculative_config=None, tokenizer='/root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, data_parallel_size=1, decode_context_parallel_size=1, dcp_comm_backend=ag_rs, disable_custom_all_reduce=False, quantization=None, enforce_eager=False, enable_return_routed_experts=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enable_in_reasoning=False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=False, enable_layerwise_nvtx_tracing=False, enable_mfu_metrics=False, enable_mm_processor_stats=False, enable_logging_iteration_details=False), seed=0, served_model_name=/root/autodl-tmp/models/Qwen2.
…[truncated 6337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T12:38:38.059455+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_fewnerd/samples.jsonl\\n/root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_fewnerd/report.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T12:38:38.059605+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7029}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T12:38:38.059771+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_fewnerd/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_fewnerd/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T12:38:38.059948+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"fewnerd\\\",\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 37648,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.5121318400500658,\\n  \\\"oracle_f1\\\": 0.6175413241802907,\\n  \\\"oracle_headroom\\\": 0.10540948413022488,\\n  \\\"fleiss_kappa_mean\\\": 0.450091181971992,\\n  \\\"soft_jaccard_mean\\\": 0.688141982278897,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.38281007752292456,\\n    \\\"p_value\\\": 0.0,\\n    \\\"n\\\": 32565\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.43286768339747067,\\n    \\\"p_value\\\": 0.0,\\n    \\\"n\\\": 32565\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3706175202241505,\\n    \\\"p_value\\\": 0.0,\\n    \\\"n\\\": 26903\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.439728575837821,\\n    \\\"p_value\\\": 0.0,\\n    \\\"n\\\": 26903\\n  },\\n  \\\"n_gold_empty_filtered\\\": 5083,\\n  \\\"n_greedy_f1_zero_filtered\\\": 5662,\\n  \\\"structural_beats_surface\\\": true,\\n  \\\"rho_advantage\\\": 0.05005760587454611,\\n  \\\"sample_f1_mean\\\": 0.5229158533963159,\\n  \\\"sample_f1_std\\\": 0.33150380421904685,\\n  \\\"sample_f1_pct_zero\\\": 18.206663595885153,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.1886088068976437,\\n      \\\"p_rho\\\": 1.774901536998061e-258,\\n      \\\"tau\\\": 0.13320626207043312,\\n      \\\"p_tau\\\": 5.034422017182722e-262,\\n      \\\"auroc\\\": 0.5961370229191391,\\n      \\\"n\\\": 32565\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.17616069812745358,\\n      \\\"p_rho\\\": 1.95941542691711e-186,\\n      \\\"tau\\\": 0.12352484653872901,\\n      \\\"p_tau\\\": 3.646413867205832e-187,\\n      \\\"auroc\\\": 0.5930242257516504,\\n      \\\"n\\\": 26903\\n    }
…[truncated 280 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T12:38:38.060106+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_conll/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_conll/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T12:38:38.060274+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"report.json\\nsamples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T12:38:38.060431+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_conll/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_conll/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T12:38:38.060602+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"conll2003\\\",\\n  \\\"subtask\\\": \\\"ner\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 3453,\\n  \\\"use_train_format\\\": true,\\n  \\\"greedy_f1\\\": 0.5384668556024054,\\n  \\\"oracle_f1\\\": 0.6274537695590328,\\n  \\\"oracle_headroom\\\": 0.08898691395662739,\\n  \\\"fleiss_kappa_mean\\\": 0.5470055233013172,\\n  \\\"soft_jaccard_mean\\\": 0.7763897024987471,\\n  \\\"correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.3772608098335525,\\n    \\\"p_value\\\": 6.15545023298997e-94,\\n    \\\"n\\\": 2756\\n  },\\n  \\\"correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.39184047364940183,\\n    \\\"p_value\\\": 7.993738416258314e-102,\\n    \\\"n\\\": 2756\\n  },\\n  \\\"correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.43462760515996635,\\n    \\\"p_value\\\": 1.2057131327837848e-98,\\n    \\\"n\\\": 2125\\n  },\\n  \\\"correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.4673615404625117,\\n    \\\"p_value\\\": 9.022361617018571e-116,\\n    \\\"n\\\": 2125\\n  },\\n  \\\"n_gold_empty_filtered\\\": 697,\\n  \\\"n_greedy_f1_zero_filtered\\\": 631,\\n  \\\"structural_beats_surface\\\": true,\\n  \\\"rho_advantage\\\": 0.014579663815849353,\\n  \\\"sample_f1_mean\\\": 0.5812628387769071,\\n  \\\"sample_f1_std\\\": 0.3839551463842149,\\n  \\\"sample_f1_pct_zero\\\": 23.353592162554428,\\n  \\\"logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": -0.019659671649330693,\\n      \\\"p_rho\\\": 0.3022045002939299,\\n      \\\"tau\\\": -0.008505948403764986,\\n      \\\"p_tau\\\": 0.5367872253005026,\\n      \\\"auroc\\\": 0.5375926817525277,\\n      \\\"n\\\": 2756\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.20951666090107726,\\n      \\\"p_rho\\\": 1.653711947960216e-22,\\n      \\\"tau\\\": 0.15097844885269116,\\n      \\\"p_tau\\\": 1.4692839197605526e-21,\\n     
…[truncated 351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T12:38:38.060799+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "content": "# Experiment Memory\n\n## exp_e2_pretrained_fewnerd — Analysis (2026-05-21)\n\n### Setup\n- Model: Qwen2.5-7B-Instruct (pretrained, no fine-tuning)\n- Dataset: FewNERD (37,648 instances)\n- SC pipeline: N=8, T=1.0, seed=42\n\n### Key Metrics\n\n| Metric | FewNERD | CoNLL (ref) |\n|--------|---------|-------------|\n| Greedy F1 | 0.5121 | 0.5385 |\n| Oracle F1 | 0.6175 | 0.6275 |\n| Oracle headroom | +0.1054 | +0.0890 |\n| Fleiss κ (mean) | 0.4501 | 0.5470 |\n| Soft Jaccard (mean) | 0.6881 | 0.7764 |\n| Sample F1 (mean±std) | 0.523±0.332 | 0.581±0.384 |\n| Sample F1=0 (%) | 18.2% | 23.4% |\n| Full ρ(κ,F1) | +0.383 | +0.377 |\n| Full ρ(SJ,F1) | +0.433 | +0.392 |\n| Cond ρ(κ,F1) | +0.371 | +0.435 |\n| Cond ρ(SJ,F1) | +0.440 | +0.467 |\n| Structural > Surface | YES (+0.050) | YES (+0.015) |\n| LP full ρ | +0.189 | -0.020 (ns) |\n| LP full AUROC | 0.596 | 0.538 |\n| LP cond ρ | +0.176 | +0.210 |\n| LP cond AUROC | 0.593 | 0.580 |\n| Verdict | PASS | MARGINAL |\n\n### Conclusion: SUCCESS\n\n**Correlation-selection gap confirmed on pretrained model.**\n\n1. **Gap exists**: Oracle F1 (0.618) exceeds Greedy F1 (0.512) by 10.5pp — substantial untapped selection potential in the 8 samples\n2. **Agreement correlates with correctness**: ρ(SJ,F1) = +0.43 (p≈0), but this correlation does NOT close the gap via naive MV → classic correlation-selection gap\n3. **Structural > Surface**: Soft Jaccard beats Fleiss κ as quality signal by +0.050 ρ — consistent across both datasets\n4. **Logprob weak**: LP correlation exists (ρ=0.19) but much weaker than agreement-based signals — LP alone insufficient for selection\n5. **Cross-dataset consistency**: Gap pattern replicates across FewNERD (37.6K instances) and CoNLL (3.5K instances), with FewNERD showing larger headroom and stronger structural advantage\n\n**Implication**: The gap is model-intrinsic (not a fine-tuning artifact). Pretrained Qwen2.5-7B already exhibits the phenomenon where agreement signals predict quality but standard aggregation fails to exploit this — motivating learned selection/weighting approaches.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "memory.md",
    "content": "# Experiment Memory\n\n## exp_e2_pretrained_fewnerd — Analysis (2026-05-21)\n\n### Setup\n- Model: Qwen2.5-7B-Instruct (pretrained, no fine-tuning)\n- Dataset: FewNERD (37,648 instances)\n- SC pipeline: N=8, T=1.0, seed=42\n\n### Key Metrics\n\n| Metric | FewNERD | CoNLL (ref) |\n|--------|---------|-------------|\n| Greedy F1 | 0.5121 | 0.5385 |\n| Oracle F1 | 0.6175 | 0.6275 |\n| Oracle headroom | +0.1054 | +0.0890 |\n| Fleiss κ (mean) | 0.4501 | 0.5470 |\n| Soft Jaccard (mean) | 0.6881 | 0.7764 |\n| Sample F1 (mean±std) | 0.523±0.332 | 0.581±0.384 |\n| Sample F1=0 (%) | 18.2% | 23.4% |\n| Full ρ(κ,F1) | +0.383 | +0.377 |\n| Full ρ(SJ,F1) | +0.433 | +0.392 |\n| Cond ρ(κ,F1) | +0.371 | +0.435 |\n| Cond ρ(SJ,F1) | +0.440 | +0.467 |\n| Structural > Surface | YES (+0.050) | YES (+0.015) |\n| LP full ρ | +0.189 | -0.020 (ns) |\n| LP full AUROC | 0.596 | 0.538 |\n| LP cond ρ | +0.176 | +0.210 |\n| LP cond AUROC | 0.593 | 0.580 |\n| Verdict | PASS | MARGINAL |\n\n### Conclusion: SUCCESS\n\n**Correlation-selection gap confirmed on pretrained model.**\n\n1. **Gap exists**: Oracle F1 (0.618) exceeds Greedy F1 (0.512) by 10.5pp — substantial untapped selection potential in the 8 samples\n2. **Agreement correlates with correctness**: ρ(SJ,F1) = +0.43 (p≈0), but this correlation does NOT close the gap via naive MV → classic correlation-selection gap\n3. **Structural > Surface**: Soft Jaccard beats Fleiss κ as quality signal by +0.050 ρ — consistent across both datasets\n4. **Logprob weak**: LP correlation exists (ρ=0.19) but much weaker than agreement-based signals — LP alone insufficient for selection\n5. **Cross-dataset consistency**: Gap pattern replicates across FewNERD (37.6K instances) and CoNLL (3.5K instances), with FewNERD showing larger headroom and stronger structural advantage\n\n**Implication**: The gap is model-intrinsic (not a fine-tuning artifact). Pretrained Qwen2.5-7B already exhibits the phenomenon where agreement signals predict quality but standard aggregation fails to exploit this — motivating learned selection/weighting approaches.\n"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T12:38:38.060964+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T12:38:38.061100+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_e2_pretrained_fewnerd",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'command': 'python -m ssc_ie.pipeline --dataset fewnerd --n_samples 8 --temperature 1.0 --seed 42 --model Qwen2.5-7B-Instruct --output_dir output/e2_pretrained_fewnerd', 'server': 'autodl-5090', 'data_path': 'fewnerd', 'data_count': 37648, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct', 'log_path': '~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_e2_pretrained_fewnerd",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'command': 'python -m ssc_ie.pipeline --dataset fewnerd --n_samples 8 --temperature 1.0 --seed 42 --model Qwen2.5-7B-Instruct --output_dir output/e2_pretrained_fewnerd', 'server': 'autodl-5090', 'data_path': 'fewnerd', 'data_count': 37648, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct', 'log_path': '~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log'}"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T12:38:38.061260+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.733}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T12:38:38.061413+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_e2_pretrained_fewnerd",
  "field": "hypothesis",
  "value": "The correlation-selection gap (oracle F1 >> MV F1 despite positive agreement-correctness correlation) is model-intrinsic and exists even in pretrained (non-finetuned) Qwen2.5-7B-Instruct, not a fine-tuning artifact",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_e2_pretrained_fewnerd",
    "field": "hypothesis",
    "value": "The correlation-selection gap (oracle F1 >> MV F1 despite positive agreement-correctness correlation) is model-intrinsic and exists even in pretrained (non-finetuned) Qwen2.5-7B-Instruct, not a fine-tuning artifact",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T12:38:38.061569+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_e2_pretrained_fewnerd\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:52:06.559Z\", \"updated_at\": \"2026-05-21T12:38:04.075Z\", \"hypothesis\": \"The correlation-selection gap (oracle F1 >> MV F1 despite positive agreement-correctness correlation) is model-intrinsic and exists even in pretrained (non-finetuned) Qwen2.5-7B-Instruct, not a fine-tuning artifact\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/e2_pretrained_fewnerd/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"8406\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log\", \"submitted_at\": \"2026-05-21T06:59:29.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained_base\", \"eval_data\": \"fewnerd\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:34:32.119Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:34:40.438881+00:00\"}]}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3222}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T12:38:38.061704+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_e2_pretrained_fewnerd",
  "field": "conclusion",
  "value": "success",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_e2_pretrained_fewnerd",
    "field": "conclusion",
    "value": "success",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T12:38:38.061849+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_e2_pretrained_fewnerd\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:52:06.559Z\", \"updated_at\": \"2026-05-21T12:38:08.322Z\", \"hypothesis\": \"The correlation-selection gap (oracle F1 >> MV F1 despite positive agreement-correctness correlation) is model-intrinsic and exists even in pretrained (non-finetuned) Qwen2.5-7B-Instruct, not a fine-tuning artifact\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/e2_pretrained_fewnerd/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"8406\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log\", \"submitted_at\": \"2026-05-21T06:59:29.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained_base\", \"eval_data\": \"fewnerd\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:34:32.119Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:34:40.438881+00:00\"}]}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2329}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T12:38:38.062010+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_e2_pretrained_fewnerd",
  "field": "metrics",
  "value": "{'greedy_f1': 0.5121, 'oracle_f1': 0.6175, 'oracle_headroom': 0.1054, 'fleiss_kappa_mean': 0.4501, 'soft_jaccard_mean': 0.6881, 'sample_f1_mean': 0.5229, 'sample_f1_std': 0.3315, 'sample_f1_pct_zero': 18.2, 'rho_fleiss_f1_full': 0.3828, 'rho_sj_f1_full': 0.4329, 'rho_fleiss_f1_cond': 0.3706, 'rho_sj_f1_cond': 0.4397, 'structural_beats_surface': True, 'rho_advantage': 0.0501, 'lp_full_rho': 0.1886, 'lp_full_auroc': 0.5961, 'lp_cond_rho': 0.1762, 'lp_cond_auroc': 0.593, 'n_instances': 37648, 'n_gold_empty_filtered': 5083, 'n_greedy_f1_zero_filtered': 5662, 'verdict': 'PASS'}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_e2_pretrained_fewnerd",
    "field": "metrics",
    "value": "{'greedy_f1': 0.5121, 'oracle_f1': 0.6175, 'oracle_headroom': 0.1054, 'fleiss_kappa_mean': 0.4501, 'soft_jaccard_mean': 0.6881, 'sample_f1_mean': 0.5229, 'sample_f1_std': 0.3315, 'sample_f1_pct_zero': 18.2, 'rho_fleiss_f1_full': 0.3828, 'rho_sj_f1_full': 0.4329, 'rho_fleiss_f1_cond': 0.3706, 'rho_sj_f1_cond': 0.4397, 'structural_beats_surface': True, 'rho_advantage': 0.0501, 'lp_full_rho': 0.1886, 'lp_full_auroc': 0.5961, 'lp_cond_rho': 0.1762, 'lp_cond_auroc': 0.593, 'n_instances': 37648, 'n_gold_empty_filtered': 5083, 'n_greedy_f1_zero_filtered': 5662, 'verdict': 'PASS'}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T12:38:38.062201+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_e2_pretrained_fewnerd",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie",
  "spec": "{'checkpoint_path': '/root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct', 'log_path': '~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_e2_pretrained_fewnerd",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie",
    "spec": "{'checkpoint_path': '/root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct', 'log_path': '~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log'}"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T12:38:38.062370+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_e2_pretrained_fewnerd\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:52:06.559Z\", \"updated_at\": \"2026-05-21T12:38:17.737Z\", \"hypothesis\": \"The correlation-selection gap (oracle F1 >> MV F1 despite positive agreement-correctness correlation) is model-intrinsic and exists even in pretrained (non-finetuned) Qwen2.5-7B-Instruct, not a fine-tuning artifact\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/e2_pretrained_fewnerd/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"8406\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log\", \"submitted_at\": \"2026-05-21T06:59:29.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained_base\", \"eval_data\": \"fewnerd\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:34:32.119Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:34:40.438881+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.5121, \"oracle_f1\": 0.6175, \"oracle_headroom\": 0.1054, \"fleiss_kappa_mean\": 0.4501, \"soft_jaccard_mean\": 0.6881, \"sample_f1_mean\": 0.5229, \"sample_f1_std\": 0.3315, \"sample_f1_pct_zero\": 18.2, \"rho_fleiss_f1_full\": 0.3828, \"rho_sj_f1_full\": 0.4329, \"rho_fleiss_f1_cond\": 0.3706, \"rho_sj_f1_cond\": 0.4397, \"structural_beats_surface\":
…[truncated 320 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T12:38:38.062595+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_e2_pretrained_fewnerd\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:52:06.559Z\", \"updated_at\": \"2026-05-21T12:38:18.972Z\", \"hypothesis\": \"The correlation-selection gap (oracle F1 >> MV F1 despite positive agreement-correctness correlation) is model-intrinsic and exists even in pretrained (non-finetuned) Qwen2.5-7B-Instruct, not a fine-tuning artifact\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/e2_pretrained_fewnerd/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"8406\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log\", \"submitted_at\": \"2026-05-21T06:59:29.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained_base\", \"eval_data\": \"fewnerd\", \"checkpoint_path\": \"/root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct\", \"wall_clock_seconds\": 20329.2, \"gpu_hours\": 5.65}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:34:32.119Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:34:40.438881+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.5121, \"oracle_f1\": 0.6175, \"oracle_headroom\": 0.1054, \"fleiss_kappa_mean\": 0.4501, \"soft_jaccard_mean\": 0.6881, \"sample_f1_mean\": 0.5229, \"sample_f1_std\": 0.3315, \"sample_f1_pct_zero\": 18.2, \"r
…[truncated 565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T12:38:38.062795+00:00_

Registry 更新完成。以下是结果汇总：

## exp_e2_pretrained_fewnerd — 结果分析

### 核心 Metrics

| Metric | FewNERD (本实验) | CoNLL (对照) |
|--------|:---:|:---:|
| Greedy F1 | 0.512 | 0.539 |
| Oracle F1 | 0.618 | 0.628 |
| **Oracle headroom** | **+0.105** | +0.089 |
| Fleiss κ | 0.450 | 0.547 |
| Soft Jaccard | 0.688 | 0.776 |
| ρ(SJ, F1) full | +0.433 | +0.392 |
| ρ(SJ, F1) cond | +0.440 | +0.467 |
| Structural > Surface | YES (+0.050) | YES (+0.015) |
| LP full ρ | +0.189 | -0.020 (ns) |
| LP full AUROC | 0.596 | 0.538 |
| Verdict | **PASS** | MARGINAL |

### Conclusion: **SUCCESS**

Correlation-selection gap 在未微调的 Qwen2.5-7B-Instruct 上明确存在：
1. **Gap 大**: Oracle F1 超 Greedy F1 达 10.5pp — 8 个样本中蕴含大量未被利用的选择潜力
2. **Agreement 正相关但不够用**: ρ(SJ,F1)=+0.43，agreement 确实预测 correctness，但 naive aggregation 仍无法逼近 oracle — 典型 correlation-selection gap
3. **Structural > Surface**: Soft Jaccard 比 Fleiss κ 多 +0.05 的相关性优势，跨数据集一致
4. **Logprob 弱**: FewNERD LP ρ=0.19（显著但弱），CoNLL full LP 甚至不显著 — 单靠 log-probability 不足以做 selection
5. **跨数据集复现**: FewNERD (37.6K) 比 CoNLL (3.5K) headroom 更大、structural advantage 更强

**核心含义**: Gap 是 model-intrinsic 而非 fine-tuning artifact，motivates learned selection/weighting approaches。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_e2_pretrained_fewnerd_20260521T123620"
}
```

</details>

---
