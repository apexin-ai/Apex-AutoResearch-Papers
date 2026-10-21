# analysis alpha ablation mf3 — Part 2 of 2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-alpha-ablation-mf3.md) · [Structured JSON](../../../sessions/e2/e28104116cf6708c67b3.json)

## Before a recorded user message

### Tool result

_source line 318 · 2026-05-22T08:18:57.756Z_

<details><summary>↩ Tool result · `toolu_01Apq2reEQDQR6i3q9HbNQrY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Alpha Ablation: MAX-SAT vs Count-only Agreement Sensitivity\\n============================================================\\n\\nCondition: Mistral-7B x FOLIO (BR=4.97)\\n|   a | SICA_acc |   CO_acc |  Agree% |  SC_acc | D(SICA-SC) |\\n|-----|----------|----------|---------|---------|------------|\\n| 0.1 |  54.90% |  54.90% | 100.0% | 53.92% |    +0.98pp |\\n| 0.3 |  54.90% |  54.90% | 100.0% | 53.92% |    +0.98pp |\\n| 0.5 |  54.90% |  54.90% | 100.0% | 53.92% |    +0.98pp |\\n| 0.7 |  53.92% |  54.41% |  99.0% | 53.92% |    +0.00pp |\\n| 0.9 |  54.90% |  55.39% |  99.0% | 53.92% |    +0.98pp |\\n\\nCondition: Qwen2.5-14B x FOLIO (seed123)\\n|   a | SICA_acc |   CO_acc |  Agree% |  SC_acc | D(SICA-SC) |\\n|-----|----------|----------|---------|---------|------------|\\n| 0.1 |  75.00% |  75.00% | 100.0% | 74.51% |    +0.49pp |\\n| 0.3 |  75.00% |  75.00% | 100.0% | 74.51% |    +0.49pp |\\n| 0.5 |  75.00% |  75.00% | 100.0% | 74.51% |    +0.49pp |\\n| 0.7 |  74.51% |  74.51% | 100.0% | 74.51% |    +0.00pp |\\n| 0.9 |  74.02% |  74.02% | 100.0% | 74.51% |    -0.49pp |\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "d4c318f1-18bf-4736-821d-b41b1a634ee1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Alpha Ablation: MAX-SAT vs Count-only Agreement Sensitivity\\\\n============================================================\\\\n\\\\nCondition: Mistral-7B x FOLIO (BR=4.97)\\\\n|   a | SICA_acc |   CO_acc |  Agree% |  SC_acc | D(SICA-SC) |\\\\n|-----|----------|----------|---------|---------|------------|\\\\n| 0.1 |  54.90% |  54.90% | 100.0% | 53.92% |    +0.98pp |\\\\n| 0.3 |  54.90% |  54.90% | 100.0% | 53.92% |    +0.98pp |\\\\n| 0.5 |  54.90% |  54.90% | 100.0% | 53.92% |    +0.98pp |\\\\n| 0.7 |  53.92% |  54.41% |  99.0% | 53.92% |    +0.00pp |\\\\n| 0.9 |  54.90% |  55.39% |  99.0% | 53.92% |    +0.98pp |\\\\n\\\\nCondition: Qwen2.5-14B x FOLIO (seed123)\\\\n|   a | SICA_acc |   CO_acc |  Agree% |  SC_acc | D(SICA-SC) |\\\\n|-----|----------|----------|---------|---------|------------|\\\\n| 0.1 |  75.00% |  75.00% | 100.0% | 74.51% |    +0.49pp |\\\\n| 0.3 |  75.00% |  75.00% | 100.0% | 74.51% |    +0.49pp |\\\\n| 0.5 |  75.00% |  75.00% | 100.0% | 74.51% |    +0.49pp |\\\\n| 0.7 |  74.51% |  74.51% | 100.0% | 74.51% |    +0.00pp |\\\\n| 0.9 |  74.02% |  74.02% | 100.0% | 74.51% |    -0.49pp |\\\\n\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.49}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Alpha Ablation: MAX-SAT vs Count-only Agreement Sensitivity\\n============================================================\\n\\nCondition: Mistral-7B x FOLIO (BR=4.97)\\n|   a | SICA_acc |   CO_acc |  Agree% |  SC_acc | D(SICA-SC) |\\n|-----|----------|----------|---------|---------|------------|\\n| 0.1 |  54.90% |  54.90% | 100.0% | 53.92% |    +0.98pp |\\n| 0.3 |  54.90% |  54.90% | 100.0% | 53.92% |    +0.98pp |\\n| 0.5 |  54.90% |  54.90% | 100.0% | 53.92% |    +0.98pp |\\n| 0.7 |  53.92% |  54.41% |  99.0% | 53.92% |    +0.00pp |\\n| 0.9 |  54.90% |  55.39% |  99.0% | 53.92% |    +0.98pp |\\n\\nCondition: Qwen2.5-14B x FOLIO (seed123)\\n|   a | SICA_acc |   CO_acc |  Agree% |  SC_acc | D(SICA-SC) |\\n|-----|----------|----------|---------|---------|------------|\\n| 0.1 |  75.00% |  75.00% | 100.0% | 74.51% |    +0.49pp |\\n| 0.3 |  75.00% |  75.00% | 100.0% | 74.51% |    +0.49pp |\\n| 0.5 |  75.00% |  75.00% | 100.0% | 74.51% |    +0.49pp |\\n| 0.7 |  74.51% |  74.51% | 100.0% | 74.51% |    +0.00pp |\\n| 0.9 |  74.02% |  74.02% | 100.0% | 74.51% |    -0.49pp |\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 319_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Gn2FiMpkudnRuKm4NBBYqg`</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /root/symb_invariant_consensus/results/alpha_ablation/alpha_ablation_combined.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "d1c8193c-f7ea-49ac-906c-b74c19623930",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XUZzcrdg7B1DuCAbRp4Tr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 922,
      "cache_read_input_tokens": 120019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 922
      },
      "output_tokens": 9,
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

_source line 320 · 2026-05-22T08:18:58.300Z_

<details><summary>↩ Tool result · `toolu_01Gn2FiMpkudnRuKm4NBBYqg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Mistral-7B_FOLIO\\\": {\\n    \\\"label\\\": \\\"Mistral-7B x FOLIO (BR=4.97)\\\",\\n    \\\"summary\\\": {\\n      \\\"0.1\\\": {\\n        \\\"alpha\\\": 0.1,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 54.9,\\n        \\\"countonly_acc\\\": 54.9,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.98\\n      },\\n      \\\"0.3\\\": {\\n        \\\"alpha\\\": 0.3,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 54.9,\\n        \\\"countonly_acc\\\": 54.9,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.98\\n      },\\n      \\\"0.5\\\": {\\n        \\\"alpha\\\": 0.5,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 54.9,\\n        \\\"countonly_acc\\\": 54.9,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.98\\n      },\\n      \\\"0.7\\\": {\\n        \\\"alpha\\\": 0.7,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 53.92,\\n        \\\"countonly_acc\\\": 54.41,\\n        \\\"agreement_pct\\\": 99.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.0\\n      },\\n      \\\"0.9\\\": {\\n        \\\"alpha\\\": 0.9,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 54.9,\\n        \\\"countonly_acc\\\": 55.39,\\n        \\\"agreement_pct\\\": 99.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.98\\n      }\\n    }\\n  },\\n  \\\"Qwen25-14B_FOLIO\\\": {\\n    \\\"label\\\": \\\"Qwen2.5-14B x FOLIO (seed123)\\\",\\n    \\\"summary\\\": {\\n      \\\"0.1\\\": {\\n        \\\"alpha\\\": 0.1,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 75.0,\\n        \\\"countonly_acc\\\": 75.0,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": 0.49\\n      },\\n      \\\"0.3\\\": {\\n        \\\"alpha\\\": 0.3,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 75.0,\\n        \\\"countonly_acc\\\": 75.0,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": 0.49\\n      },\\n      \\\"0.5\\\": {\\n        \\\"alpha\\\": 0.5,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 75.0,\\n        \\\"countonly_acc\\\": 75.0,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": 0.49\\n      },\\n      \\\"0.7\\\": {\\n        \\\"alpha\\\": 0.7,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 74.51,\\n        \\\"countonly_acc\\\": 74.51,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": 0.0\\n      },\\n      \\\"0.9\\\": {\\n        \\\"alpha\\\": 0.9,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 74.02,\\n        \\\"countonly_acc\\\": 74.02,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": -0.49\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "abd82f61-8705-4109-98df-ed9e6dd40586",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"Mistral-7B_FOLIO\\\\\\\": {\\\\n    \\\\\\\"label\\\\\\\": \\\\\\\"Mistral-7B x FOLIO (BR=4.97)\\\\\\\",\\\\n    \\\\\\\"summary\\\\\\\": {\\\\n      \\\\\\\"0.1\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.1,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 54.9,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 54.9,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 100.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 53.92,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": 0.98\\\\n      },\\\\n      \\\\\\\"0.3\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.3,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 54.9,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 54.9,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 100.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 53.92,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": 0.98\\\\n      },\\\\n      \\\\\\\"0.5\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.5,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 54.9,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 54.9,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 100.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 53.92,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": 0.98\\\\n      },\\\\n      \\\\\\\"0.7\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.7,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 53.92,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 54.41,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 99.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 53.92,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": 0.0\\\\n      },\\\\n      \\\\\\\"0.9\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.9,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 54.9,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 55.39,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 99.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 53.92,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": 0.98\\\\n      }\\\\n    }\\\\n  },\\\\n  \\\\\\\"Qwen25-14B_FOLIO\\\\\\\": {\\\\n    \\\\\\\"label\\\\\\\": \\\\\\\"Qwen2.5-14B x FOLIO (seed123)\\\\\\\",\\\\n    \\\\\\\"summary\\\\\\\": {\\\\n      \\\\\\\"0.1\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.1,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 75.0,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 75.0,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 100.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 74.51,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": 0.49\\\\n      },\\\\n      \\\\\\\"0.3\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.3,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 75.0,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 75.0,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 100.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 74.51,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": 0.49\\\\n      },\\\\n      \\\\\\\"0.5\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.5,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 75.0,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 75.0,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 100.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 74.51,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": 0.49\\\\n      },\\\\n      \\\\\\\"0.7\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.7,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 74.51,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 74.51,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 100.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 74.51,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": 0.0\\\\n      },\\\\n      \\\\\\\"0.9\\\\\\\": {\\\\n        \\\\\\\"alpha\\\\\\\": 0.9,\\\\n        \\\\\\\"n\\\\\\\": 204,\\\\n        \\\\\\\"maxsat_acc\\\\\\\": 74.02,\\\\n        \\\\\\\"countonly_acc\\\\\\\": 74.02,\\\\n        \\\\\\\"agreement_pct\\\\\\\": 100.0,\\\\n        \\\\\\\"sc_acc\\\\\\\": 74.51,\\\\n        \\\\\\\"delta_sica_sc_pp\\\\\\\": -0.49\\\\n      }\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"Mistral-7B_FOLIO\\\": {\\n    \\\"label\\\": \\\"Mistral-7B x FOLIO (BR=4.97)\\\",\\n    \\\"summary\\\": {\\n      \\\"0.1\\\": {\\n        \\\"alpha\\\": 0.1,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 54.9,\\n        \\\"countonly_acc\\\": 54.9,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.98\\n      },\\n      \\\"0.3\\\": {\\n        \\\"alpha\\\": 0.3,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 54.9,\\n        \\\"countonly_acc\\\": 54.9,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.98\\n      },\\n      \\\"0.5\\\": {\\n        \\\"alpha\\\": 0.5,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 54.9,\\n        \\\"countonly_acc\\\": 54.9,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.98\\n      },\\n      \\\"0.7\\\": {\\n        \\\"alpha\\\": 0.7,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 53.92,\\n        \\\"countonly_acc\\\": 54.41,\\n        \\\"agreement_pct\\\": 99.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.0\\n      },\\n      \\\"0.9\\\": {\\n        \\\"alpha\\\": 0.9,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 54.9,\\n        \\\"countonly_acc\\\": 55.39,\\n        \\\"agreement_pct\\\": 99.0,\\n        \\\"sc_acc\\\": 53.92,\\n        \\\"delta_sica_sc_pp\\\": 0.98\\n      }\\n    }\\n  },\\n  \\\"Qwen25-14B_FOLIO\\\": {\\n    \\\"label\\\": \\\"Qwen2.5-14B x FOLIO (seed123)\\\",\\n    \\\"summary\\\": {\\n      \\\"0.1\\\": {\\n        \\\"alpha\\\": 0.1,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 75.0,\\n        \\\"countonly_acc\\\": 75.0,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": 0.49\\n      },\\n      \\\"0.3\\\": {\\n        \\\"alpha\\\": 0.3,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 75.0,\\n        \\\"countonly_acc\\\": 75.0,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": 0.49\\n      },\\n      \\\"0.5\\\": {\\n        \\\"alpha\\\": 0.5,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 75.0,\\n        \\\"countonly_acc\\\": 75.0,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": 0.49\\n      },\\n      \\\"0.7\\\": {\\n        \\\"alpha\\\": 0.7,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 74.51,\\n        \\\"countonly_acc\\\": 74.51,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": 0.0\\n      },\\n      \\\"0.9\\\": {\\n        \\\"alpha\\\": 0.9,\\n        \\\"n\\\": 204,\\n        \\\"maxsat_acc\\\": 74.02,\\n        \\\"countonly_acc\\\": 74.02,\\n        \\\"agreement_pct\\\": 100.0,\\n        \\\"sc_acc\\\": 74.51,\\n        \\\"delta_sica_sc_pp\\\": -0.49\\n      }\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 321_

<details><summary>Logged reasoning block</summary>

```text
Excellent! The results are very clear and the output is correct. Let me also look at the 2 disagreement cases in Mistral at α=0.7 and α=0.9 to understand what's happening.

Let me also check if the process is fully done.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "415a9900-f6c5-4928-94d5-e8ae0fe3bfa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2pZiNdghPzbhuD1a9NEc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4142,
      "cache_read_input_tokens": 120941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4142
      },
      "output_tokens": 32,
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

_source line 322_

Let me check the specific disagreement cases and verify the process is complete.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "4f07e3be-5042-43a2-95e1-601314675d26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2pZiNdghPzbhuD1a9NEc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4142,
      "cache_read_input_tokens": 120941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4142
      },
      "output_tokens": 32,
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

_source line 323_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01DgV5uQCQ2NMurvecSETsw2`</summary>

```json
{
  "server": "westd-16639",
  "command": "ps -p 558721 -o pid,etime,cputime,rss"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "e4b8c701-5b8a-4351-b9d6-4fb430db8b09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V2pZiNdghPzbhuD1a9NEc8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4142,
      "cache_read_input_tokens": 120941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4142
      },
      "output_tokens": 32,
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

_source line 324 · 2026-05-22T08:19:03.833Z_

<details><summary>↩ Tool result · `toolu_01DgV5uQCQ2NMurvecSETsw2`</summary>

```text
{"result":"{\"success\": false, \"data\": {\"stdout\": \"   PID     ELAPSED     TIME   RSS\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "3888f151-e72c-4615-bd66-795066713ecf",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {\\\"stdout\\\": \\\"   PID     ELAPSED     TIME   RSS\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 1}, \\\"error\\\": \\\"exit code 1\\\", \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {\"stdout\": \"   PID     ELAPSED     TIME   RSS\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 325_

Process completed. Let me check the disagreement cases in Mistral at α=0.7/0.9.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "7614cfd0-c281-4559-bc6d-e4d0a8b0b2b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1VAbHaikVu6KWE2hoEWiK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 125083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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


### Tool call

_source line 326_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_019vPDpBxtBzxp4apLSmd8ye`</summary>

```json
{
  "server": "westd-16639",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\nwith open('/root/symb_invariant_consensus/results/alpha_ablation/Mistral-7B_FOLIO_detail.json') as f:\n    data = json.load(f)\n# Find disagreement cases at alpha=0.7 and 0.9\nfor p in data['per_problem']:\n    for a in ['a0.7', 'a0.9']:\n        if a in p and not p[a]['agree']:\n            print(f'{p[\\\"pid\\\"]} gt={p[\\\"gt\\\"]} sc={p[\\\"sc\\\"]} {a}: maxsat={p[a][\\\"maxsat\\\"]} countonly={p[a][\\\"countonly\\\"]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "33d0b8e5-c46b-4a47-80a2-c0dfeb29f32d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S1VAbHaikVu6KWE2hoEWiK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 125083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 287
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


### Tool result

_source line 327 · 2026-05-22T08:19:10.992Z_

<details><summary>↩ Tool result · `toolu_019vPDpBxtBzxp4apLSmd8ye`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"folio_83 gt=False sc=Unknown a0.7: maxsat=Unknown countonly=False\\nfolio_129 gt=True sc=Unknown a0.9: maxsat=Unknown countonly=True\\nfolio_159 gt=True sc=True a0.7: maxsat=Unknown countonly=False\\nfolio_159 gt=True sc=True a0.9: maxsat=Unknown countonly=False\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "7cdd04d9-1f5b-427b-91ad-aba16db3c5d4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"folio_83 gt=False sc=Unknown a0.7: maxsat=Unknown countonly=False\\\\nfolio_129 gt=True sc=Unknown a0.9: maxsat=Unknown countonly=True\\\\nfolio_159 gt=True sc=True a0.7: maxsat=Unknown countonly=False\\\\nfolio_159 gt=True sc=True a0.9: maxsat=Unknown countonly=False\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.55}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"folio_83 gt=False sc=Unknown a0.7: maxsat=Unknown countonly=False\\nfolio_129 gt=True sc=Unknown a0.9: maxsat=Unknown countonly=True\\nfolio_159 gt=True sc=True a0.7: maxsat=Unknown countonly=False\\nfolio_159 gt=True sc=True a0.9: maxsat=Unknown countonly=False\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 328_

<details><summary>Logged reasoning block</summary>

```text
So the disagreement cases are:
- folio_83: at α=0.7, maxsat picks Unknown but countonly picks False (gt=False → countonly is right)
- folio_129: at α=0.9, maxsat picks Unknown but countonly picks True (gt=True → countonly is right)
- folio_159: at both α=0.7 and α=0.9, maxsat picks Unknown but countonly picks False (gt=True → both wrong, but differently)

These are the 2 questions (folio_83, folio_129, folio_159 - actually 3 questions at different α values but only 2 disagreements at each α).


At α=0.7 I see folio_83 and folio_159 disagreeing, which is 2 out of 204 cases or 99.0% agreement. At α=0.9 it's folio_129 and folio_159 that disagree, also 2 out of 204 or 99.0%. The data really shows that MAX-SAT and count-only stay remarkably aligned regardless of α, with agreement consistently above 99% and only a handful of edge cases appearing at higher α values where the constraint component starts to dominate.

Now I need to format the final results properly. The task requires the branching ratio, so I have Mistral-7B × FOLIO with BR=4.97 from the task description, and for Qwen2.5-14B × FOLIO the task mentions "中等 BR" but I'm working with seed123 data since the original experiment didn't have constraint caching. Let me compile the final results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "c3c35161-825f-4baa-a0df-1fb1b8e8c0b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013QnEuzVMess75MJfH2hZqx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 125370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 485
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

_source line 329_

All done. Here are the results:

---

**Condition: Mistral-7B × FOLIO (BR=4.97)**

| α   | SICA_acc | Count-only_acc | Agreement% | Δ(SICA-SC) |
|-----|---------|----------------|------------|------------|
| 0.1 | 54.90%  | 54.90%         | 100.0%     | +0.98pp    |
| 0.3 | 54.90%  | 54.90%         | 100.0%     | +0.98pp    |
| 0.5 | 54.90%  | 54.90%         | 100.0%     | +0.98pp    |
| 0.7 | 53.92%  | 54.41%         | 99.0%      | +0.00pp    |
| 0.9 | 54.90%  | 55.39%         | 99.0%      | +0.98pp    |

**Condition: Qwen2.5-14B × FOLIO (seed123)**

| α   | SICA_acc | Count-only_acc | Agreement% | Δ(SICA-SC) |
|-----|---------|----------------|------------|------------|
| 0.1 | 75.00%  | 75.00%         | 100.0%     | +0.49pp    |
| 0.3 | 75.00%  | 75.00%         | 100.0%     | +0.49pp    |
| 0.5 | 75.00%  | 75.00%         | 100.0%     | +0.49pp    |
| 0.7 | 74.51%  | 74.51%         | 100.0%     | +0.00pp    |
| 0.9 | 74.02%  | 74.02%         | 100.0%     | -0.49pp    |

---

**核心发现**：MAX-SAT ≡ count-only 退化对 α **不敏感**。

- Agreement ≥ 99.0% across all α for both conditions (Mistral 最低 99.0%, Qwen 全程 100%)
- 仅 Mistral 在 α ≥ 0.7 时出现 2 例分歧（folio_83, folio_129, folio_159），占 204 的 ~1%
- 两个条件一致：Z3 MAX-SAT solver 几乎不影响最终答案，无论 α 如何设置

**注意**：Qwen2.5-14B 使用 seed123 数据（exp036 无 constraint cache，multi_seed 有 per-trace constraints）。SC accuracy 采用 alphabetical tiebreak，与原始实验略有差异（Mistral 53.92% vs 原始 54.41%）。

结果已保存至 `/root/symb_invariant_consensus/results/alpha_ablation/`（JSON + txt）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "uuid": "2f6a96cc-7b15-441e-88a9-e7fc9aa22e35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013QnEuzVMess75MJfH2hZqx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 125370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 485
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


### Task result

_source line 330_

All done. Here are the results:

---

**Condition: Mistral-7B × FOLIO (BR=4.97)**

| α   | SICA_acc | Count-only_acc | Agreement% | Δ(SICA-SC) |
|-----|---------|----------------|------------|------------|
| 0.1 | 54.90%  | 54.90%         | 100.0%     | +0.98pp    |
| 0.3 | 54.90%  | 54.90%         | 100.0%     | +0.98pp    |
| 0.5 | 54.90%  | 54.90%         | 100.0%     | +0.98pp    |
| 0.7 | 53.92%  | 54.41%         | 99.0%      | +0.00pp    |
| 0.9 | 54.90%  | 55.39%         | 99.0%      | +0.98pp    |

**Condition: Qwen2.5-14B × FOLIO (seed123)**

| α   | SICA_acc | Count-only_acc | Agreement% | Δ(SICA-SC) |
|-----|---------|----------------|------------|------------|
| 0.1 | 75.00%  | 75.00%         | 100.0%     | +0.49pp    |
| 0.3 | 75.00%  | 75.00%         | 100.0%     | +0.49pp    |
| 0.5 | 75.00%  | 75.00%         | 100.0%     | +0.49pp    |
| 0.7 | 74.51%  | 74.51%         | 100.0%     | +0.00pp    |
| 0.9 | 74.02%  | 74.02%         | 100.0%     | -0.49pp    |

---

**核心发现**：MAX-SAT ≡ count-only 退化对 α **不敏感**。

- Agreement ≥ 99.0% across all α for both conditions (Mistral 最低 99.0%, Qwen 全程 100%)
- 仅 Mistral 在 α ≥ 0.7 时出现 2 例分歧（folio_83, folio_129, folio_159），占 204 的 ~1%
- 两个条件一致：Z3 MAX-SAT solver 几乎不影响最终答案，无论 α 如何设置

**注意**：Qwen2.5-14B 使用 seed123 数据（exp036 无 constraint cache，multi_seed 有 per-trace constraints）。SC accuracy 采用 alphabetical tiebreak，与原始实验略有差异（Mistral 53.92% vs 原始 54.41%）。

结果已保存至 `/root/symb_invariant_consensus/results/alpha_ablation/`（JSON + txt）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 771986,
  "duration_api_ms": 676231,
  "num_turns": 134,
  "stop_reason": "end_turn",
  "session_id": "5c8c009e-a5dc-4e18-a1fc-fd5bed2eada4",
  "total_cost_usd": 4.7822284999999995,
  "usage": {
    "input_tokens": 72,
    "cache_creation_input_tokens": 114014,
    "cache_read_input_tokens": 6259654,
    "output_tokens": 37483,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 114014,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1262,
        "cache_read_input_tokens": 125370,
        "cache_creation_input_tokens": 485,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 485
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2289,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0023789999999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 72,
      "outputTokens": 37483,
      "cacheReadInputTokens": 6259654,
      "cacheCreationInputTokens": 114014,
      "webSearchRequests": 0,
      "costUSD": 4.779849499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3e018108-ce38-4e63-aabd-30ad497daedd"
}
```

</details>

---
