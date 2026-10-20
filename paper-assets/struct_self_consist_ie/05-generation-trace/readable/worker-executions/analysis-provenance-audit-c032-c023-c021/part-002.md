# analysis provenance audit c032 c023 c021 — Part 2 of 2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-provenance-audit-c032-c023-c021.md) · [Structured JSON](../../../sessions/2a/2ae718891d1ffc73d490.json)

## Round 1

### Tool result

_source line 162 · 2026-05-16T04:55:48.641Z_

<details><summary>↩ Tool result · `toolu_017YDMK7kghf7SXyMFT51Uw1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf\\n/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.png\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.pdf\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "d82d727d-6195-46ba-87da-f1913a1ba16c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf\\\\n/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.png\\\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.pdf\\\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.png\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.pdf\\n/root/autodl-tmp/struct_self_consist_ie/figures/paper/fig_signal_heatmap.png\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.pdf\\n/root/autodl-tmp/struct_self_consist_ie/artifacts/figures/fig_signal_heatmap.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 163_

<details><summary>Logged reasoning block</summary>

```text
Found it! The value 0.011 comes from:
- `/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/report.json` line 100: `rho: 0.011185364740047766`
- `/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/all_signals_5signal.json` line 403: `value: 0.011185364740047766`

This is from exp_012_rerun_1024, which is the corrected (max_tokens=1024) version. 

So the rho value of 0.011 represents the logprob conditional RE rho on the SciERC data. The provenance yaml is outdated—it claims the paper says ρ=0.002, but the paper's been updated to 0.011. The registry shows a different value of 0.1457 from exp_015_metrics_expansion, which used an incorrect conditional filter. Let me check the specific line in the report to confirm.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "9d9d42ea-4ea4-4b1a-924c-a404240bc002",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119WEZx9cweq7XQzMM2538B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 124472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2213
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

_source line 164_

Found it — ρ=0.011 comes from exp_012_rerun_1024. Let me verify the exact context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "8fb24be0-c9be-4c6a-8684-1576f59bb20f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119WEZx9cweq7XQzMM2538B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 124472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2213
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

_source line 165_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_015irSMGg492TPMiWdSbWSH9`</summary>

```json
{
  "server": "autodl-5090",
  "command": "head -120 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/report.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "94c5ff90-f221-4be2-9bd6-6b5dc9d65424",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119WEZx9cweq7XQzMM2538B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 124472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2213
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

_source line 166 · 2026-05-16T04:55:58.464Z_

<details><summary>↩ Tool result · `toolu_015irSMGg492TPMiWdSbWSH9`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"joint\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"ner_greedy_f1\\\": 0.6632805497460412,\\n  \\\"ner_oracle_f1\\\": 0.7775133848899465,\\n  \\\"ner_oracle_headroom\\\": 0.11423283514390525,\\n  \\\"ner_fleiss_kappa_mean\\\": 0.3932668065534345,\\n  \\\"ner_soft_jaccard_mean\\\": 0.6963097751953397,\\n  \\\"ner_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2665109373463269,\\n    \\\"p_value\\\": 4.716829112137585e-10,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.3598905669976535,\\n    \\\"p_value\\\": 1.2752281196882738e-17,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.17607370722783125,\\n    \\\"p_value\\\": 0.00011078924939793821,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3113352549686453,\\n    \\\"p_value\\\": 3.5148620246813462e-12,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_n_gold_empty_filtered\\\": 22,\\n  \\\"ner_n_greedy_f1_zero_filtered\\\": 52,\\n  \\\"ner_structural_beats_surface\\\": true,\\n  \\\"ner_rho_advantage\\\": 0.09337962965132657,\\n  \\\"ner_sample_f1_mean\\\": 0.6077394535406134,\\n  \\\"ner_sample_f1_std\\\": 0.3177849195309394,\\n  \\\"ner_sample_f1_pct_zero\\\": 12.594517958412098,\\n  \\\"ner_logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.20517413101613924,\\n      \\\"p_rho\\\": 1.9498006196855416e-06,\\n      \\\"tau\\\": 0.14782758668777154,\\n      \\\"p_tau\\\": 1.2434769103035355e-06,\\n      \\\"auroc\\\": 0.6115722797477874,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.1537825418721844,\\n      \\\"p_rho\\\": 0.0007519115126420073,\\n      \\\"tau\\\": 0.11105453570642614,\\n      \\\"p_tau\\\": 0.000576950633780567,\\n      \\\"auroc\\\": 0.5929390252479078,\\n      \\\"n\\\": 477\\n    }\\n  },\\n  \\\"re_greedy_f1\\\": 0.42893018583626313,\\n  \\\"re_oracle_f1\\\": 0.5795918367346938,\\n  \\\"re_oracle_headroom\\\": 0.1506616508984307,\\n  \\\"re_fleiss_kappa_mean\\\": 0.29342166441787654,\\n  \\\"re_soft_jaccard_mean\\\": 0.6146283784710029,\\n  \\\"re_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2752041540770546,\\n    \\\"p_value\\\": 2.4879922095201242e-08,\\n    \\\"n\\\": 397\\n  },\\n  \\\"re_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2503364334141933,\\n    \\\"p_value\\\": 4.3522331002259703e-07,\\n    \\\"n\\\": 397\\n  },\\n  \\\"re_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.11387685552692939,\\n    \\\"p_value\\\": 0.07955653487541735,\\n    \\\"n\\\": 238\\n  },\\n  \\\"re_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.24569967508929075,\\n    \\\"p_value\\\": 0.00012846667277061877,\\n    \\\"n\\\": 238\\n  },\\n  \\\"re_n_gold_empty_filtered\\\": 154,\\n  \\\"re_n_greedy_f1_zero_filtered\\\": 159,\\n  \\\"re_structural_beats_surface\\\": false,\\n  \\\"re_rho_advantage\\\": -0.024867720662861303,\\n  \\\"re_sample_f1_mean\\\": 0.3544350077048391,\\n  \\\"re_sample_f1_std\\\": 0.37736734533106986,\\n  \\\"re_sample_f1_pct_zero\\\": 44.395465994962215,\\n  \\\"re_logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.26624475312006335,\\n      \\\"p_rho\\\": 7.217251690334773e-08,\\n      \\\"tau\\\": 0.19508661157044746,\\n      \\\"p_tau\\\": 8.831074413665826e-08,\\n      \\\"auroc\\\": 0.6204557091653866,\\n      \\\"n\\\": 397\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.011185364740047766,\\n      \\\"p_rho\\\": 0.8637077626329154,\\n      \\\"tau\\\": 0.005069639898728457,\\n      \\\"p_tau\\\": 0.9126852484133136,\\n      \\\"auroc\\\": 0.5632929642445214,\\n      \\\"n\\\": 238\\n    }\\n  },\\n  \\\"verdict\\\": \\\"FAIL\\\",\\n  \\\"verdict_note\\\": \\\"Joint mode: verdict requires RE ρ_sj ≥ 0.40 AND ρ_sj > ρ_fk AND any subtask headroom ≥ 2pp\\\",\\n  \\\"warning\\\": \\\"⚠️ >30% samples F1=0, recommend re-running at T=0.7\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "e28e2246-9cfc-46e1-aeb3-51b342f80120",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"dataset\\\\\\\": \\\\\\\"scierc\\\\\\\",\\\\n  \\\\\\\"subtask\\\\\\\": \\\\\\\"joint\\\\\\\",\\\\n  \\\\\\\"n_samples\\\\\\\": 8,\\\\n  \\\\\\\"temperature\\\\\\\": 1.0,\\\\n  \\\\\\\"num_instances\\\\\\\": 551,\\\\n  \\\\\\\"use_train_format\\\\\\\": true,\\\\n  \\\\\\\"ner_greedy_f1\\\\\\\": 0.6632805497460412,\\\\n  \\\\\\\"ner_oracle_f1\\\\\\\": 0.7775133848899465,\\\\n  \\\\\\\"ner_oracle_headroom\\\\\\\": 0.11423283514390525,\\\\n  \\\\\\\"ner_fleiss_kappa_mean\\\\\\\": 0.3932668065534345,\\\\n  \\\\\\\"ner_soft_jaccard_mean\\\\\\\": 0.6963097751953397,\\\\n  \\\\\\\"ner_correlation_fleiss_vs_f1_full\\\\\\\": {\\\\n    \\\\\\\"rho\\\\\\\": 0.2665109373463269,\\\\n    \\\\\\\"p_value\\\\\\\": 4.716829112137585e-10,\\\\n    \\\\\\\"n\\\\\\\": 529\\\\n  },\\\\n  \\\\\\\"ner_correlation_softjaccard_vs_f1_full\\\\\\\": {\\\\n    \\\\\\\"rho\\\\\\\": 0.3598905669976535,\\\\n    \\\\\\\"p_value\\\\\\\": 1.2752281196882738e-17,\\\\n    \\\\\\\"n\\\\\\\": 529\\\\n  },\\\\n  \\\\\\\"ner_correlation_fleiss_vs_f1_conditional\\\\\\\": {\\\\n    \\\\\\\"rho\\\\\\\": 0.17607370722783125,\\\\n    \\\\\\\"p_value\\\\\\\": 0.00011078924939793821,\\\\n    \\\\\\\"n\\\\\\\": 477\\\\n  },\\\\n  \\\\\\\"ner_correlation_softjaccard_vs_f1_conditional\\\\\\\": {\\\\n    \\\\\\\"rho\\\\\\\": 0.3113352549686453,\\\\n    \\\\\\\"p_value\\\\\\\": 3.5148620246813462e-12,\\\\n    \\\\\\\"n\\\\\\\": 477\\\\n  },\\\\n  \\\\\\\"ner_n_gold_empty_filtered\\\\\\\": 22,\\\\n  \\\\\\\"ner_n_greedy_f1_zero_filtered\\\\\\\": 52,\\\\n  \\\\\\\"ner_structural_beats_surface\\\\\\\": true,\\\\n  \\\\\\\"ner_rho_advantage\\\\\\\": 0.09337962965132657,\\\\n  \\\\\\\"ner_sample_f1_mean\\\\\\\": 0.6077394535406134,\\\\n  \\\\\\\"ner_sample_f1_std\\\\\\\": 0.3177849195309394,\\\\n  \\\\\\\"ner_sample_f1_pct_zero\\\\\\\": 12.594517958412098,\\\\n  \\\\\\\"ner_logprob_baseline\\\\\\\": {\\\\n    \\\\\\\"full\\\\\\\": {\\\\n      \\\\\\\"rho\\\\\\\": 0.20517413101613924,\\\\n      \\\\\\\"p_rho\\\\\\\": 1.9498006196855416e-06,\\\\n      \\\\\\\"tau\\\\\\\": 0.14782758668777154,\\\\n      \\\\\\\"p_tau\\\\\\\": 1.2434769103035355e-06,\\\\n      \\\\\\\"auroc\\\\\\\": 0.6115722797477874,\\\\n      \\\\\\\"n\\\\\\\": 529\\\\n    },\\\\n    \\\\\\\"conditional\\\\\\\": {\\\\n      \\\\\\\"rho\\\\\\\": 0.1537825418721844,\\\\n      \\\\\\\"p_rho\\\\\\\": 0.0007519115126420073,\\\\n      \\\\\\\"tau\\\\\\\": 0.11105453570642614,\\\\n      \\\\\\\"p_tau\\\\\\\": 0.000576950633780567,\\\\n      \\\\\\\"auroc\\\\\\\": 0.5929390252479078,\\\\n      \\\\\\\"n\\\\\\\": 477\\\\n    }\\\\n  },\\\\n  \\\\\\\"re_greedy_f1\\\\\\\": 0.42893018583626313,\\\\n  \\\\\\\"re_oracle_f1\\\\\\\": 0.5795918367346938,\\\\n  \\\\\\\"re_oracle_headroom\\\\\\\": 0.1506616508984307,\\\\n  \\\\\\\"re_fleiss_kappa_mean\\\\\\\": 0.29342166441787654,\\\\n  \\\\\\\"re_soft_jaccard_mean\\\\\\\": 0.6146283784710029,\\\\n  \\\\\\\"re_correlation_fleiss_vs_f1_full\\\\\\\": {\\\\n    \\\\\\\"rho\\\\\\\": 0.2752041540770546,\\\\n    \\\\\\\"p_value\\\\\\\": 2.4879922095201242e-08,\\\\n    \\\\\\\"n\\\\\\\": 397\\\\n  },\\\\n  \\\\\\\"re_correlation_softjaccard_vs_f1_full\\\\\\\": {\\\\n    \\\\\\\"rho\\\\\\\": 0.2503364334141933,\\\\n    \\\\\\\"p_value\\\\\\\": 4.3522331002259703e-07,\\\\n    \\\\\\\"n\\\\\\\": 397\\\\n  },\\\\n  \\\\\\\"re_correlation_fleiss_vs_f1_conditional\\\\\\\": {\\\\n    \\\\\\\"rho\\\\\\\": 0.11387685552692939,\\\\n    \\\\\\\"p_value\\\\\\\": 0.07955653487541735,\\\\n    \\\\\\\"n\\\\\\\": 238\\\\n  },\\\\n  \\\\\\\"re_correlation_softjaccard_vs_f1_conditional\\\\\\\": {\\\\n    \\\\\\\"rho\\\\\\\": 0.24569967508929075,\\\\n    \\\\\\\"p_value\\\\\\\": 0.00012846667277061877,\\\\n    \\\\\\\"n\\\\\\\": 238\\\\n  },\\\\n  \\\\\\\"re_n_gold_empty_filtered\\\\\\\": 154,\\\\n  \\\\\\\"re_n_greedy_f1_zero_filtered\\\\\\\": 159,\\\\n  \\\\\\\"re_structural_beats_surface\\\\\\\": false,\\\\n  \\\\\\\"re_rho_advantage\\\\\\\": -0.024867720662861303,\\\\n  \\\\\\\"re_sample_f1_mean\\\\\\\": 0.3544350077048391,\\\\n  \\\\\\\"re_sample_f1_std\\\\\\\": 0.37736734533106986,\\\\n  \\\\\\\"re_sample_f1_pct_zero\\\\\\\": 44.395465994962215,\\\\n  \\\\\\\"re_logprob_baseline\\\\\\\": {\\\\n    \\\\\\\"full\\\\\\\": {\\\\n      \\\\\\\"rho\\\\\\\": 0.26624475312006335,\\\\n      \\\\\\\"p_rho\\\\\\\": 7.217251690334773e-08,\\\\n      \\\\\\\"tau\\\\\\\": 0.19508661157044746,\\\\n      \\\\\\\"p_tau\\\\\\\": 8.831074413665826e-08,\\\\n      \\\\\\\"auroc\\\\\\\": 0.6204557091653866,\\\\n      \\\\\\\"n\\\\\\\": 397\\\\n    },\\\\n    \\\\\\\"conditional\\\\\\\": {\\\\n      \\\\\\\"rho\\\\\\\": 0.011185364740047766,\\\\n      \\\\\\\"p_rho\\\\\\\": 0.8637077626329154,\\\\n      \\\\\\\"tau\\\\\\\": 0.005069639898728457,\\\\n      \\\\\\\"p_tau\\\\\\\": 0.9126852484133136,\\\\n      \\\\\\\"auroc\\\\\\\": 0.5632929642445214,\\\\n      \\\\\\\"n\\\\\\\": 238\\\\n    }\\\\n  },\\\\n  \\\\\\\"verdict\\\\\\\": \\\\\\\"FAIL\\\\\\\",\\\\n  \\\\\\\"verdict_note\\\\\\\": \\\\\\\"Joint mode: verdict requires RE ρ_sj ≥ 0.40 AND ρ_sj > ρ_fk AND any subtask headroom ≥ 2pp\\\\\\\",\\\\n  \\\\\\\"warning\\\\\\\": \\\\\\\"⚠️ >30% samples F1=0, recommend re-running at T=0.7\\\\\\\"\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"dataset\\\": \\\"scierc\\\",\\n  \\\"subtask\\\": \\\"joint\\\",\\n  \\\"n_samples\\\": 8,\\n  \\\"temperature\\\": 1.0,\\n  \\\"num_instances\\\": 551,\\n  \\\"use_train_format\\\": true,\\n  \\\"ner_greedy_f1\\\": 0.6632805497460412,\\n  \\\"ner_oracle_f1\\\": 0.7775133848899465,\\n  \\\"ner_oracle_headroom\\\": 0.11423283514390525,\\n  \\\"ner_fleiss_kappa_mean\\\": 0.3932668065534345,\\n  \\\"ner_soft_jaccard_mean\\\": 0.6963097751953397,\\n  \\\"ner_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2665109373463269,\\n    \\\"p_value\\\": 4.716829112137585e-10,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.3598905669976535,\\n    \\\"p_value\\\": 1.2752281196882738e-17,\\n    \\\"n\\\": 529\\n  },\\n  \\\"ner_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.17607370722783125,\\n    \\\"p_value\\\": 0.00011078924939793821,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.3113352549686453,\\n    \\\"p_value\\\": 3.5148620246813462e-12,\\n    \\\"n\\\": 477\\n  },\\n  \\\"ner_n_gold_empty_filtered\\\": 22,\\n  \\\"ner_n_greedy_f1_zero_filtered\\\": 52,\\n  \\\"ner_structural_beats_surface\\\": true,\\n  \\\"ner_rho_advantage\\\": 0.09337962965132657,\\n  \\\"ner_sample_f1_mean\\\": 0.6077394535406134,\\n  \\\"ner_sample_f1_std\\\": 0.3177849195309394,\\n  \\\"ner_sample_f1_pct_zero\\\": 12.594517958412098,\\n  \\\"ner_logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.20517413101613924,\\n      \\\"p_rho\\\": 1.9498006196855416e-06,\\n      \\\"tau\\\": 0.14782758668777154,\\n      \\\"p_tau\\\": 1.2434769103035355e-06,\\n      \\\"auroc\\\": 0.6115722797477874,\\n      \\\"n\\\": 529\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.1537825418721844,\\n      \\\"p_rho\\\": 0.0007519115126420073,\\n      \\\"tau\\\": 0.11105453570642614,\\n      \\\"p_tau\\\": 0.000576950633780567,\\n      \\\"auroc\\\": 0.5929390252479078,\\n      \\\"n\\\": 477\\n    }\\n  },\\n  \\\"re_greedy_f1\\\": 0.42893018583626313,\\n  \\\"re_oracle_f1\\\": 0.5795918367346938,\\n  \\\"re_oracle_headroom\\\": 0.1506616508984307,\\n  \\\"re_fleiss_kappa_mean\\\": 0.29342166441787654,\\n  \\\"re_soft_jaccard_mean\\\": 0.6146283784710029,\\n  \\\"re_correlation_fleiss_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2752041540770546,\\n    \\\"p_value\\\": 2.4879922095201242e-08,\\n    \\\"n\\\": 397\\n  },\\n  \\\"re_correlation_softjaccard_vs_f1_full\\\": {\\n    \\\"rho\\\": 0.2503364334141933,\\n    \\\"p_value\\\": 4.3522331002259703e-07,\\n    \\\"n\\\": 397\\n  },\\n  \\\"re_correlation_fleiss_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.11387685552692939,\\n    \\\"p_value\\\": 0.07955653487541735,\\n    \\\"n\\\": 238\\n  },\\n  \\\"re_correlation_softjaccard_vs_f1_conditional\\\": {\\n    \\\"rho\\\": 0.24569967508929075,\\n    \\\"p_value\\\": 0.00012846667277061877,\\n    \\\"n\\\": 238\\n  },\\n  \\\"re_n_gold_empty_filtered\\\": 154,\\n  \\\"re_n_greedy_f1_zero_filtered\\\": 159,\\n  \\\"re_structural_beats_surface\\\": false,\\n  \\\"re_rho_advantage\\\": -0.024867720662861303,\\n  \\\"re_sample_f1_mean\\\": 0.3544350077048391,\\n  \\\"re_sample_f1_std\\\": 0.37736734533106986,\\n  \\\"re_sample_f1_pct_zero\\\": 44.395465994962215,\\n  \\\"re_logprob_baseline\\\": {\\n    \\\"full\\\": {\\n      \\\"rho\\\": 0.26624475312006335,\\n      \\\"p_rho\\\": 7.217251690334773e-08,\\n      \\\"tau\\\": 0.19508661157044746,\\n      \\\"p_tau\\\": 8.831074413665826e-08,\\n      \\\"auroc\\\": 0.6204557091653866,\\n      \\\"n\\\": 397\\n    },\\n    \\\"conditional\\\": {\\n      \\\"rho\\\": 0.011185364740047766,\\n      \\\"p_rho\\\": 0.8637077626329154,\\n      \\\"tau\\\": 0.005069639898728457,\\n      \\\"p_tau\\\": 0.9126852484133136,\\n      \\\"auroc\\\": 0.5632929642445214,\\n      \\\"n\\\": 238\\n    }\\n  },\\n  \\\"verdict\\\": \\\"FAIL\\\",\\n  \\\"verdict_note\\\": \\\"Joint mode: verdict requires RE ρ_sj ≥ 0.40 AND ρ_sj > ρ_fk AND any subtask headroom ≥ 2pp\\\",\\n  \\\"warning\\\": \\\"⚠️ >30% samples F1=0, recommend re-running at T=0.7\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 167_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01KHRa1zjc6nDRPuLB92iaBe`</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -n \"0\\.011\" /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/all_signals_5signal.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "a1bec669-ae3a-4f6a-afc0-444519aa8c55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119WEZx9cweq7XQzMM2538B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2213,
      "cache_read_input_tokens": 124472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2213
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

_source line 168 · 2026-05-16T04:55:59.111Z_

<details><summary>↩ Tool result · `toolu_01KHRa1zjc6nDRPuLB92iaBe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"403:            \\\"value\\\": 0.011185364740047766,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "f1fec962-e075-4bc8-952b-6271061cfd60",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"403:            \\\\\\\"value\\\\\\\": 0.011185364740047766,\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"403:            \\\"value\\\": 0.011185364740047766,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 169_

<details><summary>Logged reasoning block</summary>

```text
Now I have the definitive answer for c032:

**exp_012_rerun_1024/report.json** shows:
- `re_logprob_baseline.conditional.rho = 0.011185364740047766` (n=238, p=0.864)
- This uses the CORRECT conditional filter (greedy_f1 > 0, n=238)

So:
- The **current paper** says ρ=0.011 (experiments.tex line 50, appendix.tex line 137) — this is from exp_012_rerun_1024 with correct conditional filter


- The **provenance yaml** is outdated, claiming the paper says 0.002 when it actually says 0.011
- The **registry** shows 0.1457 from exp_015_metrics_expansion, which used an incorrect conditional filter (any sample F1 > 0, n=331)

The paper's current value of 0.011 is correct, sourced from the properly filtered experiment with n=238.

Now looking at c023, I'm checking the RE SJ ρ values across sentence length quartiles — Q1 at 0.110, Q4 at 0.473, with a Fisher p-value of 0.004 from exp_009_v2_re_re.

The registry shows different values (Q1=0.447, Q4=0.540) that came from a different stratification approach using entity count rather than sentence length, which explains the discrepancy. Looking at the v2 rerun with proper gold-filtering, the values shift significantly to Q1=0.110 and Q4=0.473, which is what the paper correctly uses. For the WNUT SJ ρ metric, the paper reports 0.089 in the appendix, matching the exp003 evaluation results, though the provenance note references an older value of 0.062 that appears to come from deprecated experiment files. Looking at the actual experiment results, the pilot run gave 0.082 and the evaluation run gave 0.089 for the WNUT SJ rho value, so neither matches the 0.062 that was documented in the provenance yaml — that older value must have come from a different experimental setup or seed. The grep search confirms 0.062 doesn't appear as a WNUT SJ rho value anywhere in the current paper—only as an LP range metric. So all three discrepancies are resolved: the provenance yaml entries are stale, the paper values are correct and properly sourced, and the untraceable 0.062 isn't actually used. Now I'll compile the audit report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "85d52d04-43a2-4e2e-9fbe-8a21284555a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6EBJuqvbEyvVDDAej2ec7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3035,
      "cache_read_input_tokens": 126685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3035
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

_source line 170_

All three investigations complete. Now I have definitive answers. Let me compile the audit report.

Key findings:
- **c032**: Current paper already says ρ=0.011 (not 0.002). Source: exp_012_rerun_1024, correct conditional filter (n=238). Provenance yaml is stale.
- **c023**: Paper values (Q1=0.110, Q4=0.473) are correct from exp_009_v2_re_rerun. Registry has older exp_009 values without gold-filtering.
- **c021**: Current paper says ρ=0.089 (not 0.062). The 0.062 existed only in old deprecated experiments.tex and is untraceable.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "cd1a9a83-8af1-43a0-a93d-650d2954f78c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6EBJuqvbEyvVDDAej2ec7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3035,
      "cache_read_input_tokens": 126685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3035
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

_source line 171_

<details open><summary>🔧 Tool call — Bash · `toolu_013gFU2VKq2RsryB9nJaQgmM`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "8f0ce8a5-5bce-4957-9947-49f664154e39",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F6EBJuqvbEyvVDDAej2ec7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3035,
      "cache_read_input_tokens": 126685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3035
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

_source line 172 · 2026-05-16T04:56:46.888Z_

<details><summary>↩ Tool result · `toolu_013gFU2VKq2RsryB9nJaQgmM`</summary>

```text
3seed_ner_summary.md
3seed_summary
__pycache__
_project
analysis_fk_bootstrap_ci_full.json
analysis_lp_range_cdf.json
analysis_lp_range_cdf_n16_3seed.json
analysis_scierc_n16_3seed_selection_f1.json
analysis_scierc_re_n16_3seed_selection_f1.json
analysis_unified_rho.json
analysis_unified_rho_full.json
analyze_exp004_re_diagnostic.py
analyze_exp004_v2_re_diagnostic.py
analyze_exp005_v2_temperature.py
analyze_exp015_metrics_expansion.py
analyze_exp016_ensemble.py
analyze_ood_signals.py
audit_autodl5090_loop3.md
audit_gpu5090_4x2_loop3.md
auroc_bug_diagnosis.md
autodl_process_check.md
bjb1_status_report.md
bootstrap_ci_nscaling
bootstrap_ci_summary.json
bootstrap_ci_tables.tex
consistency.py
d072_paper_patch_inventory.md
data
data_utils.py
dream_reports
evaluate_verifier.py
evaluation.py
exp-001
exp-015
exp001_postprocess.py
exp005_temperature
exp009_stratification_analysis.py
exp010_selection_curves
exp_001
exp_001_n16
exp_001_ner_n16_scierc
exp_001_seed456_v2_ner
exp_002
exp_003
exp_004_re_diagnostic
exp_004_v2
exp_005
exp_005_v2
exp_009_capability_stratification
exp_009_v2
exp_009_v2_re_rerun
exp_009_v2_stratification.py
exp_010_selection_curves
exp_011_ood_scierc_to_conll
exp_012_logprob_baseline
exp_012_rerun_1024
exp_015_metrics_expansion
exp_016_rerun_1024
exp_016_rerun_1024_bootstrap
exp_016_signal_ensemble
exp_016_v2
exp_016_v2_ensemble.py
exp_017_llama_conll_n8_t07
exp_018
exp_018_provenance_report.md
exp_freeform_ablation
exp_freeform_conll_4seed
exp_llama3b_scierc_ablation
exp_verbalized_confidence
fig_selection_gap.png
figures
fk_excess_agreement_all_configs.md
freeform_3seed_summary.json
freeform_ablation_appendix_table.tex
freeform_ablation_deep_analysis.md
freeform_ablation_results.md
ft_001
ft_002
greedy_f1_discrepancy_audit.md
heatmap_data_audit.md
logprob_tie_analysis.md
loo_sj_cross_dataset
lp_range_cdf.pdf
lp_range_cdf.png
lp_range_cdf_n16_3seed.pdf
lp_range_cdf_n16_3seed.png
manifest.yaml
multi_seed_stability_table.md
multiseed_flip_overlap_analysis.md
mvp_pilot.py
mvp_pilot_001
mvp_pilot_004
n16_3seed_scs_analysis.md
n16_5signal_comparison.md
n16_readiness_report.md
n8_bootstrap_ci.py
n8_seed123_unified_rho_results.md
n_scaling_appendix_tables.tex
ood_cross_dataset_results.md
pending_exp_readiness.md
plot_length_logprob_scatter.py
q1q6_answer_prep
qwen3_thinking_confirmation.md
re_conditional_analysis.py
re_nonzero_selection_analysis.md
review_issues.yaml
review_reports
rho_consistency_audit.md
rho_paper_impact_list.md
round8_analysis_data_summary.md
run_mvp_pilot.py
sampling.py
tost_breakpoint_delta_star.md
train_supervised_verifier.py
training_config_appendix.md
vc_implementation_rho_diff.md
wnut17_diagnosis_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "e3ad47c8-044e-4423-b6e1-f90df5d79278",
  "tool_use_result": {
    "stdout": "3seed_ner_summary.md\n3seed_summary\n__pycache__\n_project\nanalysis_fk_bootstrap_ci_full.json\nanalysis_lp_range_cdf.json\nanalysis_lp_range_cdf_n16_3seed.json\nanalysis_scierc_n16_3seed_selection_f1.json\nanalysis_scierc_re_n16_3seed_selection_f1.json\nanalysis_unified_rho.json\nanalysis_unified_rho_full.json\nanalyze_exp004_re_diagnostic.py\nanalyze_exp004_v2_re_diagnostic.py\nanalyze_exp005_v2_temperature.py\nanalyze_exp015_metrics_expansion.py\nanalyze_exp016_ensemble.py\nanalyze_ood_signals.py\naudit_autodl5090_loop3.md\naudit_gpu5090_4x2_loop3.md\nauroc_bug_diagnosis.md\nautodl_process_check.md\nbjb1_status_report.md\nbootstrap_ci_nscaling\nbootstrap_ci_summary.json\nbootstrap_ci_tables.tex\nconsistency.py\nd072_paper_patch_inventory.md\ndata\ndata_utils.py\ndream_reports\nevaluate_verifier.py\nevaluation.py\nexp-001\nexp-015\nexp001_postprocess.py\nexp005_temperature\nexp009_stratification_analysis.py\nexp010_selection_curves\nexp_001\nexp_001_n16\nexp_001_ner_n16_scierc\nexp_001_seed456_v2_ner\nexp_002\nexp_003\nexp_004_re_diagnostic\nexp_004_v2\nexp_005\nexp_005_v2\nexp_009_capability_stratification\nexp_009_v2\nexp_009_v2_re_rerun\nexp_009_v2_stratification.py\nexp_010_selection_curves\nexp_011_ood_scierc_to_conll\nexp_012_logprob_baseline\nexp_012_rerun_1024\nexp_015_metrics_expansion\nexp_016_rerun_1024\nexp_016_rerun_1024_bootstrap\nexp_016_signal_ensemble\nexp_016_v2\nexp_016_v2_ensemble.py\nexp_017_llama_conll_n8_t07\nexp_018\nexp_018_provenance_report.md\nexp_freeform_ablation\nexp_freeform_conll_4seed\nexp_llama3b_scierc_ablation\nexp_verbalized_confidence\nfig_selection_gap.png\nfigures\nfk_excess_agreement_all_configs.md\nfreeform_3seed_summary.json\nfreeform_ablation_appendix_table.tex\nfreeform_ablation_deep_analysis.md\nfreeform_ablation_results.md\nft_001\nft_002\ngreedy_f1_discrepancy_audit.md\nheatmap_data_audit.md\nlogprob_tie_analysis.md\nloo_sj_cross_dataset\nlp_range_cdf.pdf\nlp_range_cdf.png\nlp_range_cdf_n16_3seed.pdf\nlp_range_cdf_n16_3seed.png\nmanifest.yaml\nmulti_seed_stability_table.md\nmultiseed_flip_overlap_analysis.md\nmvp_pilot.py\nmvp_pilot_001\nmvp_pilot_004\nn16_3seed_scs_analysis.md\nn16_5signal_comparison.md\nn16_readiness_report.md\nn8_bootstrap_ci.py\nn8_seed123_unified_rho_results.md\nn_scaling_appendix_tables.tex\nood_cross_dataset_results.md\npending_exp_readiness.md\nplot_length_logprob_scatter.py\nq1q6_answer_prep\nqwen3_thinking_confirmation.md\nre_conditional_analysis.py\nre_nonzero_selection_analysis.md\nreview_issues.yaml\nreview_reports\nrho_consistency_audit.md\nrho_paper_impact_list.md\nround8_analysis_data_summary.md\nrun_mvp_pilot.py\nsampling.py\ntost_breakpoint_delta_star.md\ntrain_supervised_verifier.py\ntraining_config_appendix.md\nvc_implementation_rho_diff.md\nwnut17_diagnosis_report.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Tool call

_source line 173_

<details open><summary>🔧 Tool call — Write · `toolu_01DXPeusaupEXReoN2KaNhRq`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/provenance_audit_c032_c023_c021.md",
  "content": "# Provenance Audit: c032 / c023 / c021\n\n**Date**: 2026-05-16\n**Auditor**: automated provenance trace\n**Scope**: Three claims in paper_provenance.yaml where registered values diverge from paper text\n\n---\n\n## c032: logprob conditional RE ρ\n\n- **Provenance yaml claim**: paper says ρ=0.002\n- **Registry value**: exp_015_metrics_expansion → re.logprob_rho_cond = 0.1457\n- **Current paper text**: ρ=0.011 (experiments.tex:50, appendix.tex:137)\n\n### Source trace\n\nThe **current paper** says ρ=0.011 in two places:\n1. `experiments.tex:50` — \"LP †RE collapses to ρ=0.011\"\n2. `appendix.tex:137` — heatmap caption: \"LP RE collapses to near-zero (ρ=0.011)\"\n\nThe value **0.01119** is in:\n- `output/exp_012_rerun_1024/report.json:100` — `re_logprob_baseline.conditional.rho = 0.011185364740047766`\n- `output/exp_012_rerun_1024/all_signals_5signal.json:403` — same value\n- Conditions: SciERC RE, N=8, T=1.0, max_tokens=1024, **correct conditional filter** (greedy_f1 > 0, n=238)\n\n### Why the discrepancy\n\n| Value | Source | Filter | n_cond | Status |\n|-------|--------|--------|--------|--------|\n| 0.002 | provenance yaml claim | unknown | — | **STALE** — paper was updated to 0.011; 0.002 untraceable in any output file |\n| 0.1457 | exp_015_metrics_expansion | WRONG: any sample F1 > 0 | 331 | Wrong filter inflates n, changes correlation |\n| **0.011** | exp_012_rerun_1024 | CORRECT: greedy_f1 > 0 | 238 | Current paper value |\n\nThe `conditional_filter_diagnosis.json` documents that exp_015 (and several other scripts) used the wrong conditional filter (\"any sample F1 > 0\" instead of \"greedy_f1 > 0\"), inflating the conditional set from n=238 to n=331 for RE. This is the root cause of the registry's 0.1457.\n\n### Conclusion\n\n**Provenance yaml is stale.** The paper was already corrected from 0.002 to 0.011. The current paper value (0.011 from exp_012_rerun_1024, correct conditional filter) is correct. The registry value (0.1457) uses a known-wrong conditional filter and should be annotated as deprecated.\n\n---\n\n## c023: RE SJ ρ by sentence length (Q1/Q4)\n\n- **Paper values**: Q1=0.110, Q4=0.473, Fisher z p=0.004\n- **Registry values**: exp_009_capability_stratification → Q1=0.447, Q4=0.540\n\n### Source trace\n\nPaper values match **exp_009_v2_re_rerun** exactly:\n\nFrom `output/exp_009_v2_re_rerun/summary.txt`:\n```\nStratification by Sentence Length QUARTILES (primary, independent)\n  Q1 (low)   n=117  SJ 0.110[-0.08,0.29]\n  Q2         n=93   SJ 0.308[0.09,0.50]\n  Q3         n=92   SJ 0.372[0.18,0.54]\n  Q4 (high)  n=95   SJ 0.473[0.28,0.62]\n\nFisher z-test low_vs_high:\n  sj   z=-2.878  p=0.004*\n```\n\nAll three paper values (Q1=0.110, Q4=0.473, p=0.004) match the v2 rerun output character-for-character.\n\nFrom `output/exp_009_v2_re_rerun/results.json`:\n- `by_sent_len_quartiles.\"Q1 (low)\".signals.sj.rho = 0.10961735` → rounds to 0.110\n- `by_sent_len_quartiles.\"Q4 (high)\".signals.sj.rho = 0.47332...` → rounds to 0.473\n- Fisher z low_vs_high sj p = 0.00435... → rounds to 0.004\n\n### Why the registry differs\n\nThe registry values (Q1=0.447, Q4=0.540) come from the **original exp_009_capability_stratification**, which:\n1. Did NOT apply gold-empty filtering (included 154 instances with empty gold RE annotations)\n2. Used all 551 raw instances instead of the filtered 397\n\nThe v2 rerun applied proper gold-filtering (551 → 397 after removing gold-empty), which is the mandated pipeline for all ρ values in the paper.\n\n| Value set | Source | Gold filter | n_RE | Status |\n|-----------|--------|-------------|------|--------|\n| Q1=0.447, Q4=0.540 | exp_009 original | No | 551 | **Outdated** — pre-gold-filter |\n| **Q1=0.110, Q4=0.473** | exp_009_v2_re_rerun | Yes | 397 | Current paper value |\n\n### Conclusion\n\n**Paper values are correct.** They come from exp_009_v2_re_rerun with proper gold-filtering. The registry entry for exp_009_capability_stratification is outdated and should be annotated as superseded by exp_009_v2_re_rerun.\n\n---\n\n## c021: WNUT SJ ρ\n\n- **Provenance yaml claim**: paper says ρ=0.062 (p=0.106)\n- **Registry values**: exp_003_ner_wnut17 → 0.082; exp_003_wnut17_eval → 0.089\n\n### Source trace — current paper\n\nThe **current paper** (appendix.tex:222, Table tab:wnut) shows:\n```\nSJ  .089  .020  .517  .288  <1e-7\n```\ni.e., SJ full-set ρ = **0.089**, p = 0.020\n\nThis matches `output/exp003_wnut17_eval/report.json`:\n- `correlation_softjaccard_vs_f1_full.rho = 0.08883161` → rounds to 0.089\n- `correlation_softjaccard_vs_f1_full.p_value = 0.01970` → rounds to 0.020\n- n = 689 (after gold-empty filtering)\n\n### Tracing the 0.062\n\nThe value ρ=0.062 appears ONLY in the **old deprecated paper** at:\n- `artifacts/_project/paper/experiments.tex:181` — \"SJ achieves ρ=0.062 (p=0.106, not statistically significant)\"\n\nThis file is in `artifacts/_project/paper/` which is excluded from compilation per constraint C001. The current compiled paper at `docs/paper/sections/` does NOT contain 0.062 for WNUT.\n\nSearching all output files for 0.062 in WNUT context yields **no matches**. The closest values found are:\n- exp003_wnut17_pilot: SJ full rho = 0.0825 (different seed)\n- exp003_wnut17_eval: SJ full rho = 0.0888\n- exp_009_v2 global SJ rho (SciERC RE, not WNUT): 0.0625\n\nThe value 0.062 for WNUT SJ is **untraceable** — it does not appear in any analysis output file. It may have originated from:\n1. An earlier experiment run that was overwritten\n2. A different seed/N configuration\n3. A manual transcription error in the old draft\n\n### Conclusion\n\n**Provenance yaml is stale.** The current paper correctly uses ρ=0.089 from exp003_wnut17_eval (N=16, T=1.0, gold-filtered n=689). The 0.062 value from the old paper draft is untraceable and no longer appears in the compiled paper.\n\n---\n\n## Summary\n\n| Claim | Provenance yaml | Current paper | Ground truth source | Status |\n|-------|----------------|---------------|-------------------|--------|\n| c032 LP cond RE ρ | 0.002 | **0.011** | exp_012_rerun_1024 (correct filter, n=238) | Provenance stale; paper correct |\n| c023 RE SJ Q1/Q4 | Q1=0.447/Q4=0.540 (registry) | **Q1=0.110/Q4=0.473** | exp_009_v2_re_rerun (gold-filtered) | Registry outdated; paper correct |\n| c021 WNUT SJ ρ | 0.062 | **0.089** | exp003_wnut17_eval (n=689) | Provenance stale; paper correct |\n\n**All three paper values are correct in the current compiled paper.** The discrepancies exist only between the provenance yaml / registry entries and the paper — not between the paper and the ground truth data. The provenance yaml and registry entries need updating.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "ba633247-04c1-4a43-a046-210fa444270b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015czKAUn1S9bWysWHUPAF68",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3420,
      "cache_read_input_tokens": 129720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3420
      },
      "output_tokens": 63,
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

_source line 174 · 2026-05-16T04:57:29.531Z_

<details><summary>↩ Tool result · `toolu_01DXPeusaupEXReoN2KaNhRq`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/provenance_audit_c032_c023_c021.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "d7a68959-98d5-487e-a373-7bebc0106774",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/provenance_audit_c032_c023_c021.md",
    "content": "# Provenance Audit: c032 / c023 / c021\n\n**Date**: 2026-05-16\n**Auditor**: automated provenance trace\n**Scope**: Three claims in paper_provenance.yaml where registered values diverge from paper text\n\n---\n\n## c032: logprob conditional RE ρ\n\n- **Provenance yaml claim**: paper says ρ=0.002\n- **Registry value**: exp_015_metrics_expansion → re.logprob_rho_cond = 0.1457\n- **Current paper text**: ρ=0.011 (experiments.tex:50, appendix.tex:137)\n\n### Source trace\n\nThe **current paper** says ρ=0.011 in two places:\n1. `experiments.tex:50` — \"LP †RE collapses to ρ=0.011\"\n2. `appendix.tex:137` — heatmap caption: \"LP RE collapses to near-zero (ρ=0.011)\"\n\nThe value **0.01119** is in:\n- `output/exp_012_rerun_1024/report.json:100` — `re_logprob_baseline.conditional.rho = 0.011185364740047766`\n- `output/exp_012_rerun_1024/all_signals_5signal.json:403` — same value\n- Conditions: SciERC RE, N=8, T=1.0, max_tokens=1024, **correct conditional filter** (greedy_f1 > 0, n=238)\n\n### Why the discrepancy\n\n| Value | Source | Filter | n_cond | Status |\n|-------|--------|--------|--------|--------|\n| 0.002 | provenance yaml claim | unknown | — | **STALE** — paper was updated to 0.011; 0.002 untraceable in any output file |\n| 0.1457 | exp_015_metrics_expansion | WRONG: any sample F1 > 0 | 331 | Wrong filter inflates n, changes correlation |\n| **0.011** | exp_012_rerun_1024 | CORRECT: greedy_f1 > 0 | 238 | Current paper value |\n\nThe `conditional_filter_diagnosis.json` documents that exp_015 (and several other scripts) used the wrong conditional filter (\"any sample F1 > 0\" instead of \"greedy_f1 > 0\"), inflating the conditional set from n=238 to n=331 for RE. This is the root cause of the registry's 0.1457.\n\n### Conclusion\n\n**Provenance yaml is stale.** The paper was already corrected from 0.002 to 0.011. The current paper value (0.011 from exp_012_rerun_1024, correct conditional filter) is correct. The registry value (0.1457) uses a known-wrong conditional filter and should be annotated as deprecated.\n\n---\n\n## c023: RE SJ ρ by sentence length (Q1/Q4)\n\n- **Paper values**: Q1=0.110, Q4=0.473, Fisher z p=0.004\n- **Registry values**: exp_009_capability_stratification → Q1=0.447, Q4=0.540\n\n### Source trace\n\nPaper values match **exp_009_v2_re_rerun** exactly:\n\nFrom `output/exp_009_v2_re_rerun/summary.txt`:\n```\nStratification by Sentence Length QUARTILES (primary, independent)\n  Q1 (low)   n=117  SJ 0.110[-0.08,0.29]\n  Q2         n=93   SJ 0.308[0.09,0.50]\n  Q3         n=92   SJ 0.372[0.18,0.54]\n  Q4 (high)  n=95   SJ 0.473[0.28,0.62]\n\nFisher z-test low_vs_high:\n  sj   z=-2.878  p=0.004*\n```\n\nAll three paper values (Q1=0.110, Q4=0.473, p=0.004) match the v2 rerun output character-for-character.\n\nFrom `output/exp_009_v2_re_rerun/results.json`:\n- `by_sent_len_quartiles.\"Q1 (low)\".signals.sj.rho = 0.10961735` → rounds to 0.110\n- `by_sent_len_quartiles.\"Q4 (high)\".signals.sj.rho = 0.47332...` → rounds to 0.473\n- Fisher z low_vs_high sj p = 0.00435... → rounds to 0.004\n\n### Why the registry differs\n\nThe registry values (Q1=0.447, Q4=0.540) come from the **original exp_009_capability_stratification**, which:\n1. Did NOT apply gold-empty filtering (included 154 instances with empty gold RE annotations)\n2. Used all 551 raw instances instead of the filtered 397\n\nThe v2 rerun applied proper gold-filtering (551 → 397 after removing gold-empty), which is the mandated pipeline for all ρ values in the paper.\n\n| Value set | Source | Gold filter | n_RE | Status |\n|-----------|--------|-------------|------|--------|\n| Q1=0.447, Q4=0.540 | exp_009 original | No | 551 | **Outdated** — pre-gold-filter |\n| **Q1=0.110, Q4=0.473** | exp_009_v2_re_rerun | Yes | 397 | Current paper value |\n\n### Conclusion\n\n**Paper values are correct.** They come from exp_009_v2_re_rerun with proper gold-filtering. The registry entry for exp_009_capability_stratification is outdated and should be annotated as superseded by exp_009_v2_re_rerun.\n\n---\n\n## c021: WNUT SJ ρ\n\n- **Provenance yaml claim**: paper says ρ=0.062 (p=0.106)\n- **Registry values**: exp_003_ner_wnut17 → 0.082; exp_003_wnut17_eval → 0.089\n\n### Source trace — current paper\n\nThe **current paper** (appendix.tex:222, Table tab:wnut) shows:\n```\nSJ  .089  .020  .517  .288  <1e-7\n```\ni.e., SJ full-set ρ = **0.089**, p = 0.020\n\nThis matches `output/exp003_wnut17_eval/report.json`:\n- `correlation_softjaccard_vs_f1_full.rho = 0.08883161` → rounds to 0.089\n- `correlation_softjaccard_vs_f1_full.p_value = 0.01970` → rounds to 0.020\n- n = 689 (after gold-empty filtering)\n\n### Tracing the 0.062\n\nThe value ρ=0.062 appears ONLY in the **old deprecated paper** at:\n- `artifacts/_project/paper/experiments.tex:181` — \"SJ achieves ρ=0.062 (p=0.106, not statistically significant)\"\n\nThis file is in `artifacts/_project/paper/` which is excluded from compilation per constraint C001. The current compiled paper at `docs/paper/sections/` does NOT contain 0.062 for WNUT.\n\nSearching all output files for 0.062 in WNUT context yields **no matches**. The closest values found are:\n- exp003_wnut17_pilot: SJ full rho = 0.0825 (different seed)\n- exp003_wnut17_eval: SJ full rho = 0.0888\n- exp_009_v2 global SJ rho (SciERC RE, not WNUT): 0.0625\n\nThe value 0.062 for WNUT SJ is **untraceable** — it does not appear in any analysis output file. It may have originated from:\n1. An earlier experiment run that was overwritten\n2. A different seed/N configuration\n3. A manual transcription error in the old draft\n\n### Conclusion\n\n**Provenance yaml is stale.** The current paper correctly uses ρ=0.089 from exp003_wnut17_eval (N=16, T=1.0, gold-filtered n=689). The 0.062 value from the old paper draft is untraceable and no longer appears in the compiled paper.\n\n---\n\n## Summary\n\n| Claim | Provenance yaml | Current paper | Ground truth source | Status |\n|-------|----------------|---------------|-------------------|--------|\n| c032 LP cond RE ρ | 0.002 | **0.011** | exp_012_rerun_1024 (correct filter, n=238) | Provenance stale; paper correct |\n| c023 RE SJ Q1/Q4 | Q1=0.447/Q4=0.540 (registry) | **Q1=0.110/Q4=0.473** | exp_009_v2_re_rerun (gold-filtered) | Registry outdated; paper correct |\n| c021 WNUT SJ ρ | 0.062 | **0.089** | exp003_wnut17_eval (n=689) | Provenance stale; paper correct |\n\n**All three paper values are correct in the current compiled paper.** The discrepancies exist only between the provenance yaml / registry entries and the paper — not between the paper and the ground truth data. The provenance yaml and registry entries need updating.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---


### Assistant

_source line 175_

审计完成。报告已写入 `artifacts/provenance_audit_c032_c023_c021.md`。

**结论：三个不一致项全部是 provenance yaml / registry 过时，当前论文值均正确。**

| 项 | Provenance/Registry 值 | 当前论文值 | 真实来源 | 状态 |
|---|---|---|---|---|
| c032 LP cond RE ρ | 0.002 / 0.1457 | **0.011** | exp_012_rerun_1024 (正确 filter, n=238) | 论文已修正 |
| c023 RE SJ Q1/Q4 | Q1=0.447, Q4=0.540 | **Q1=0.110, Q4=0.473** | exp_009_v2_re_rerun (gold-filtered) | 论文正确，registry 未更新 |
| c021 WNUT SJ ρ | 0.062 | **0.089** | exp003_wnut17_eval (n=689) | 论文已修正，0.062 无法追溯 |

关键发现：
- **c032**：registry 的 0.1457 来自 exp_015_metrics_expansion 使用了错误的 conditional filter（any sample F1>0 而非 greedy_f1>0），当前论文的 0.011 使用正确 filter
- **c023**：registry 来自原始 exp_009（未做 gold-filtering），论文使用了 v2 rerun（gold-filtered 后 n=397）
- **c021**：0.062 仅存在于 artifacts/_project/paper/ 旧版本中，在所有实验输出中无法追溯

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "uuid": "ecd9002a-2268-4208-abfb-44b5531663c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H9itunwZvsuEgaBWJLVjVa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2528,
      "cache_read_input_tokens": 133140,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2528
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

_source line 176_

审计完成。报告已写入 `artifacts/provenance_audit_c032_c023_c021.md`。

**结论：三个不一致项全部是 provenance yaml / registry 过时，当前论文值均正确。**

| 项 | Provenance/Registry 值 | 当前论文值 | 真实来源 | 状态 |
|---|---|---|---|---|
| c032 LP cond RE ρ | 0.002 / 0.1457 | **0.011** | exp_012_rerun_1024 (正确 filter, n=238) | 论文已修正 |
| c023 RE SJ Q1/Q4 | Q1=0.447, Q4=0.540 | **Q1=0.110, Q4=0.473** | exp_009_v2_re_rerun (gold-filtered) | 论文正确，registry 未更新 |
| c021 WNUT SJ ρ | 0.062 | **0.089** | exp003_wnut17_eval (n=689) | 论文已修正，0.062 无法追溯 |

关键发现：
- **c032**：registry 的 0.1457 来自 exp_015_metrics_expansion 使用了错误的 conditional filter（any sample F1>0 而非 greedy_f1>0），当前论文的 0.011 使用正确 filter
- **c023**：registry 来自原始 exp_009（未做 gold-filtering），论文使用了 v2 rerun（gold-filtered 后 n=397）
- **c021**：0.062 仅存在于 artifacts/_project/paper/ 旧版本中，在所有实验输出中无法追溯

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 427147,
  "duration_api_ms": 425687,
  "num_turns": 66,
  "stop_reason": "end_turn",
  "session_id": "ff14a560-c52e-4a4a-af53-469861f178d5",
  "total_cost_usd": 2.29202575,
  "usage": {
    "input_tokens": 24,
    "cache_creation_input_tokens": 123827,
    "cache_read_input_tokens": 1794752,
    "output_tokens": 22630,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 123827,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 472,
        "cache_read_input_tokens": 133140,
        "cache_creation_input_tokens": 2528,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2528
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2079,
      "outputTokens": 2192,
      "cacheReadInputTokens": 40320,
      "cacheCreationInputTokens": 30232,
      "webSearchRequests": 0,
      "costUSD": 0.05486099999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 24,
      "outputTokens": 22630,
      "cacheReadInputTokens": 1794752,
      "cacheCreationInputTokens": 123827,
      "webSearchRequests": 0,
      "costUSD": 2.2371647500000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f09072fb-0037-4fad-a164-00c5650c6024"
}
```

</details>

---
