# check mvp pilot 005 results

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_check_mvp_pilot_005_results_20260514T094607.jsonl`
- **Structured JSON:** [`2116f78648c4868622a0.json`](../../sessions/21/2116f78648c4868622a0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-14T09:47:24.542723+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__update_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T09:47:24.543107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T09:47:24.543358+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/report.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T09:47:24.543499+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'mvp_pilot_005'}",
  "project": "struct_self_consist_ie",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'mvp_pilot_005'}",
    "project": "struct_self_consist_ie",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T09:47:24.543696+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"joint\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 0.7,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"ner_greedy_f1\\\": 0.6618919725455088,\\n  \\\"ner_oracle_f1\\\": 0.7584770969660917,\\n  \\\"ner_oracle_headroom\\\": 0.09658512442058287,\\n  \\\"ner_fleiss_kappa_mean\\\": 0.47220488877283673,\\n  \\\"ner_soft_jaccard_mean\\\": 0.7756751743868986,\\n  \\\"ner_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.3211381156606757,\\n    \\\"p_value\\\": 3.728468048325399e-14,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.38752870683799207,\\n    \\\"p_value\\\": 2.1176283024296294e-20,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3049733249860266,\\n    \\\"p_value\\\": 2.6149161899438738e-12,\\n    \\\"n\\\": 504\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3868290142068471,\\n    \\\"p_value\\\": 1.949035624666113e-19,\\n    \\\"n\\\": 504\\n  },\\n  \\\"ner_n_gold_empty_filtered\\\": 22,\\n  \\\"ner_n_all_samples_f1_zero_filtered\\\": 25,\\n  \\\"ner_structural_beats_surface\\\": true,\\n  \\\"ner_rho_advantage\\\": 0.06639059117731638,\\n  \\\"ner_sample_f1_mean\\\": 0.6242672694417469,\\n  \\\"ner_sample_f1_std\\\": 0.31308028094863866,\\n  \\\"ner_sample_f1_pct_zero\\\": 11.200378071833649,\\n  \\\"re_greedy_f1\\\": 0.42194513715710724,\\n  \\\"re_oracle_f1\\\": 0.5532128514056225,\\n  \\\"re_oracle_headroom\\\": 0.13126771424851524,\\n  \\\"re_fleiss_kappa_mean\\\": 0.3829257472481029,\\n  \\\"re_soft_jaccard_mean\\\": 0.6870479587459823,\\n  \\\"re_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.18347677834972748,\\n    \\\"p_value\\\": 0.00023741188191916336,\\n    \\\"n\\\": 397\\n  },\\n  \\\"re_correlation_softjaccard_vs_f
…[truncated 1183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T09:47:24.543858+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0281}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T09:47:24.544034+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "struct_self_consist_ie",
  "limit": "10",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "limit": "10",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T09:47:24.544427+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"e1_component_wise_re_sj\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:15:17.262Z\", \"updated_at\": \"2026-05-14T09:23:38.818Z\", \"spec\": {\"hypothesis\": \"RE SJ 乘性惩罚是 root cause：分解后 head_sj ρ ≈ NER ρ (~0.38)，tail_sj 和乘性组合拖低整体 ρ\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 397, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Component-wise decomposition: head_sj, tail_sj, type_match 分别计算 Spearman ρ vs per-instance RE F1\", \"command\": \"python3 code/analyze_component_wise_re.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/e1_component_analysis.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"full_head_sj_rho\": 0.21, \"full_tail_sj_rho\": 0.201, \"full_type_match_rho\": 0.201, \"full_multiplicative_rho\": 0.244, \"full_additive_rho\": 0.243, \"full_fleiss_kappa_rho\": 0.278, \"cond_head_sj_rho\": 0.27, \"cond_tail_sj_rho\": 0.259, \"cond_type_match_rho\": 0.252, \"cond_multiplicative_rho\": 0.316, \"cond_additive_rho\": 0.306, \"cond_fleiss_kappa_rho\": 0.307, \"n_full\": 397, \"n_conditional\": 313, \"diagnosis\": \"head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE.\"}, \"completed_at\": \"2026-05-14T09:22:26.155Z\"}, \"mvp_pilot_005\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:16:14.166Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/s
…[truncated 13899 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T09:47:24.544652+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_pilot_005",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_pilot_005",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T09:47:24.544811+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_pilot_005\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:46:51.772Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 32456, \"tmux_session\": \"mvp_pilot_005\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.0608}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T09:47:24.545058+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_pilot_005",
  "field": "metrics",
  "value": "{'ner_greedy_f1': 0.6619, 'ner_oracle_f1': 0.7585, 'ner_headroom': 0.0966, 'ner_fleiss_kappa_mean': 0.4722, 'ner_soft_jaccard_mean': 0.7757, 'ner_full_rho_sj': 0.3875, 'ner_full_rho_fk': 0.3211, 'ner_full_n': 529, 'ner_cond_rho_sj': 0.3868, 'ner_cond_rho_fk': 0.305, 'ner_cond_n': 504, 'ner_sj_beats_fk_full': True, 'ner_sj_beats_fk_cond': True, 'ner_rho_advantage': 0.0664, 'ner_sample_f1_mean': 0.6243, 'ner_sample_f1_std': 0.3131, 'ner_sample_f1_pct_zero': 11.2, 'ner_gold_empty_filtered': 22, 'ner_all_zero_filtered': 25, 're_greedy_f1': 0.4219, 're_oracle_f1': 0.5532, 're_headroom': 0.1313, 're_fleiss_kappa_mean': 0.3829, 're_soft_jaccard_mean': 0.687, 're_full_rho_sj': 0.2343, 're_full_rho_fk': 0.1835, 're_full_n': 397, 're_cond_rho_sj': 0.3716, 're_cond_rho_fk': 0.2533, 're_cond_n': 301, 're_sj_beats_fk_full': True, 're_sj_beats_fk_cond': True, 're_rho_advantage': 0.0508, 're_sample_f1_mean': 0.3782, 're_sample_f1_std': 0.3845, 're_sample_f1_pct_zero': 42.4, 're_gold_empty_filtered': 154, 're_all_zero_filtered': 96, 'parse_failures': 0, 'verdict': 'FAIL', 'verdict_note': 'RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold'}",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_pilot_005",
    "field": "metrics",
    "value": "{'ner_greedy_f1': 0.6619, 'ner_oracle_f1': 0.7585, 'ner_headroom': 0.0966, 'ner_fleiss_kappa_mean': 0.4722, 'ner_soft_jaccard_mean': 0.7757, 'ner_full_rho_sj': 0.3875, 'ner_full_rho_fk': 0.3211, 'ner_full_n': 529, 'ner_cond_rho_sj': 0.3868, 'ner_cond_rho_fk': 0.305, 'ner_cond_n': 504, 'ner_sj_beats_fk_full': True, 'ner_sj_beats_fk_cond': True, 'ner_rho_advantage': 0.0664, 'ner_sample_f1_mean': 0.6243, 'ner_sample_f1_std': 0.3131, 'ner_sample_f1_pct_zero': 11.2, 'ner_gold_empty_filtered': 22, 'ner_all_zero_filtered': 25, 're_greedy_f1': 0.4219, 're_oracle_f1': 0.5532, 're_headroom': 0.1313, 're_fleiss_kappa_mean': 0.3829, 're_soft_jaccard_mean': 0.687, 're_full_rho_sj': 0.2343, 're_full_rho_fk': 0.1835, 're_full_n': 397, 're_cond_rho_sj': 0.3716, 're_cond_rho_fk': 0.2533, 're_cond_n': 301, 're_sj_beats_fk_full': True, 're_sj_beats_fk_cond': True, 're_rho_advantage': 0.0508, 're_sample_f1_mean': 0.3782, 're_sample_f1_std': 0.3845, 're_sample_f1_pct_zero': 42.4, 're_gold_empty_filtered': 154, 're_all_zero_filtered': 96, 'parse_failures': 0, 'verdict': 'FAIL', 'verdict_note': 'RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold'}",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T09:47:24.545353+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_pilot_005\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:46:58.903Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 32456, \"tmux_session\": \"mvp_pilot_005\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_
…[truncated 613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T09:47:24.545536+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_pilot_005",
  "field": "conclusion",
  "value": "negative",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_pilot_005",
    "field": "conclusion",
    "value": "negative",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T09:47:24.545711+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_pilot_005\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:47:02.251Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 32456, \"tmux_session\": \"mvp_pilot_005\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_
…[truncated 644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T09:47:24.546008+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "mvp_pilot_005",
  "field": "status",
  "value": "DONE",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "mvp_pilot_005",
    "field": "status",
    "value": "DONE",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T09:47:24.546254+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mvp_pilot_005\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:47:06.597Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 32456, \"tmux_session\": \"mvp_pilot_005\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_sj\
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-14T09:47:24.546454+00:00_

Registry 更新完成 (DONE/negative)。

---

## mvp_pilot_005 结果汇总

**Verdict: FAIL** — RE full ρ_sj = 0.234 < 0.30 硬截止线

### NER 指标

| 指标 | pilot_005 (T=0.7) | pilot_004 (T=1.0) | 变化 |
|------|-------|-------|------|
| greedy_f1 | 0.662 | 0.667 | -0.005 |
| oracle_f1 | 0.759 | 0.776 | -0.017 |
| headroom | 9.7pp | 10.9pp | -1.2pp |
| ρ_sj (full) | **0.388** | 0.383 | +0.005 |
| ρ_fk (full) | 0.321 | 0.259 | +0.062 |
| ρ_sj (cond) | **0.387** | 0.376 | +0.011 |
| SJ > FK | ✅ both | ✅ both | — |
| pct_zero | 11.2% | 12.2% | -1.0pp |
| soft_jaccard_mean | 0.776 | 0.701 | +0.075 |

### RE 指标

| 指标 | pilot_005 (T=0.7) | pilot_004 (T=1.0) | 变化 |
|------|-------|-------|------|
| greedy_f1 | 0.422 | 0.421 | +0.001 |
| oracle_f1 | 0.553 | 0.588 | -0.035 |
| headroom | 13.1pp | 16.7pp | **-3.6pp** |
| ρ_sj (full) | **0.234** | 0.244 | **-0.010 ↓** |
| ρ_fk (full) | 0.184 | 0.278 | -0.094 |
| ρ_sj (cond) | **0.372** | 0.316 | **+0.056 ↑** |
| ρ_fk (cond) | 0.253 | 0.307 | -0.054 |
| SJ > FK | ✅ both | ❌full/✅cond | **改善** |
| pct_zero | 42.4% | 44.3% | -1.9pp |
| soft_jaccard_mean | 0.687 | 0.611 | +0.076 |

### 关键发现

1. **RE full ρ_sj = 0.234 < 0.30**：Director 硬截止线未通过，甚至比 pilot_004 (0.244) 更差
2. **RE cond ρ_sj 显著提升**：0.316 → 0.372 (+0.056)，T=0.7 在非零子集上有效
3. **RE zero rate 几乎没变**：44.3% → 42.4%，降温未能实质性解决零值问题
4. **SJ > FK 全面恢复**：T=0.7 下 RE full set 也 SJ > FK（pilot_004 full set 是 FK > SJ）
5. **NER 稳定**：ρ_sj 略升至 0.388，T=0.7 对 NER 无负面影响
6. **Oracle headroom 收窄**：T=0.7 降低了多样性，RE oracle F1 从 0.588 降到 0.553

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_mvp_pilot_005_results_20260514T094607"
}
```

</details>

---
