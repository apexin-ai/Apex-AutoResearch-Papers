# ops verify baseline ci — Part 2 of 2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ops-verify-baseline-ci.md) · [Structured JSON](../../../sessions/81/818e8195a37d9b5d542a.json)

## Before a recorded user message

### Tool result

_source line 412 · 2026-05-16T14:21:20.153Z_

<details><summary>↩ Tool result · `toolu_01Tw2bUyGtG7V7ZeHUkPgjiE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"avg_logprob\\\": {\\n    \\\"3class_f1\\\": 0.7085,\\n    \\\"3class_ci\\\": [\\n      0.7037,\\n      0.7127\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5689,\\n      \\\"mistral-7b-v0.3\\\": 0.4696,\\n      \\\"olmo-2-1b\\\": 0.7343,\\n      \\\"pythia-1b\\\": 0.7991,\\n      \\\"pythia-2.8b\\\": 0.7654,\\n      \\\"qwen3-0.6b\\\": 0.7484,\\n      \\\"qwen3-1.7b\\\": 0.7599,\\n      \\\"qwen3-8b\\\": 0.6324\\n    },\\n    \\\"binary_f1\\\": 0.6785,\\n    \\\"binary_ci\\\": [\\n      0.6729,\\n      0.6844\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.4801,\\n      \\\"mistral-7b-v0.3\\\": 0.3682,\\n      \\\"olmo-2-1b\\\": 0.7032,\\n      \\\"pythia-1b\\\": 0.7636,\\n      \\\"pythia-2.8b\\\": 0.7183,\\n      \\\"qwen3-0.6b\\\": 0.7323,\\n      \\\"qwen3-1.7b\\\": 0.7372,\\n      \\\"qwen3-8b\\\": 0.6345\\n    }\\n  },\\n  \\\"fastdetectgpt\\\": {\\n    \\\"3class_f1\\\": 0.6654,\\n    \\\"3class_ci\\\": [\\n      0.6608,\\n      0.6698\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5723,\\n      \\\"mistral-7b-v0.3\\\": 0.5438,\\n      \\\"olmo-2-1b\\\": 0.6622,\\n      \\\"pythia-1b\\\": 0.7361,\\n      \\\"pythia-2.8b\\\": 0.7158,\\n      \\\"qwen3-0.6b\\\": 0.7181,\\n      \\\"qwen3-1.7b\\\": 0.6929,\\n      \\\"qwen3-8b\\\": 0.5953\\n    },\\n    \\\"binary_f1\\\": 0.5805,\\n    \\\"binary_ci\\\": [\\n      0.5747,\\n      0.5863\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.463,\\n      \\\"mistral-7b-v0.3\\\": 0.4119,\\n      \\\"olmo-2-1b\\\": 0.5866,\\n      \\\"pythia-1b\\\": 0.6679,\\n      \\\"pythia-2.8b\\\": 0.6283,\\n      \\\"qwen3-0.6b\\\": 0.6408,\\n      \\\"qwen3-1.7b\\\": 0.6172,\\n      \\\"qwen3-8b\\\": 0.5123\\n    }\\n  },\\n  \\\"binoculars\\\": {\\n    \\\"3class_f1\\\": 0.4094,\\n    \\\"3class_ci\\\": [\\n      0.4042,\\n      0.4138\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.3397,\\n      \\\"mistral-7b-v0.3\\\": 0.3185,\\n      \\\"olmo-2-1b\\\": 0.4137,\\n      \\\"pythia-1b\\\": 0.4205,\\n      \\\"pythia-2.8b\\\": 0.4457,\\n      \\\"qwen3-0.6b\\\": 0.4006,\\n      \\\"qwen3-1.7b\\\": 0.4249,\\n      \\\"qwen3-8b\\\": 0.4161\\n    },\\n    \\\"binary_f1\\\": 0.5327,\\n    \\\"binary_ci\\\": [\\n      0.5267,\\n      0.5389\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.4985,\\n      \\\"mistral-7b-v0.3\\\": 0.3825,\\n      \\\"olmo-2-1b\\\": 0.535,\\n      \\\"pythia-1b\\\": 0.5455,\\n      \\\"pythia-2.8b\\\": 0.5458,\\n      \\\"qwen3-0.6b\\\": 0.547,\\n      \\\"qwen3-1.7b\\\": 0.541,\\n      \\\"qwen3-8b\\\": 0.5285\\n    }\\n  },\\n  \\\"ld_score\\\": {\\n    \\\"3class_f1\\\": 0.6319,\\n    \\\"3class_ci\\\": [\\n      0.6269,\\n      0.6368\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5473,\\n      \\\"mistral-7b-v0.3\\\": 0.4648,\\n      \\\"olmo-2-1b\\\": 0.6356,\\n      \\\"pythia-1b\\\": 0.732,\\n      \\\"pythia-2.8b\\\": 0.6778,\\n      \\\"qwen3-0.6b\\\": 0.6905,\\n      \\\"qwen3-1.7b\\\": 0.6544,\\n      \\\"qwen3-8b\\\": 0.5505\\n    },\\n    \\\"binary_f1\\\": 0.6782,\\n    \\\"binary_ci\\\": [\\n      0.6726,\\n      0.6845\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5769,\\n      \\\"mistral-7b-v0.3\\\": 0.4744,\\n      \\\"olmo-2-1b\\\": 0.6678,\\n      \\\"pythia-1b\\\": 0.7664,\\n      \\\"pythia-2.8b\\\": 0.7227,\\n      \\\"qwen3-0.6b\\\": 0.7232,\\n      \\\"qwen3-1.7b\\\": 0.7121,\\n      \\\"qwen3-8b\\\": 0.6255\\n    }\\n  },\\n  \\\"4det_ensemble\\\": {\\n    \\\"3class_f1\\\": 0.7783,\\n    \\\"3class_ci\\\": [\\n      0.7741,\\n      0.7822\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.7537,\\n      \\\"mistral-7b-v0.3\\\": 0.6044,\\n      \\\"olmo-2-1b\\\": 0.7807,\\n      \\\"pythia-1b\\\": 0.8445,\\n      \\\"pythia-2.8b\\\": 0.8126,\\n      \\\"qwen3-0.6b\\\": 0.8246,\\n      \\\"qwen3-1.7b\\\": 0.8204,\\n      \\\"qwen3-8b\\\": 0.701\\n    },\\n    \\\"binary_f1\\\": 0.6984,\\n    \\\"binary_ci\\\": [\\n      0.6931,\\n      0.7044\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.6898,\\n      \\\"mistral-7b-v0.3\\\": 0.4724,\\n      \\\"olmo-2-1b\\\": 0.6969,\\n      \\\"pythia-1b\\\": 0.7789,\\n      \\\"pythia-2.8b\\\": 0.7245,\\n      \\\"qwen3-0.6b\\\": 0.743,\\n      \\\"qwen3-1.7b\\\": 0.7453,\\n      \\\"qwen3-8b\\\": 0.6348\\n    }\\n  },\\n  \\\"4det_surface\\\": {\\n    \\\"3class_f1\\\": 0.7826,\\n    \\\"3class_ci\\\": [\\n      0.7788,\\n      0.7868\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.7509,\\n      \\\"mistral-7b-v0.3\\\": 0.5909,\\n      \\\"olmo-2-1b\\\": 0.7748,\\n      \\\"pythia-1b\\\": 0.8571,\\n      \\\"pythia-2.8b\\\": 0.8183,\\n      \\\"qwen3-0.6b\\\": 0.8292,\\n      \\\"qwen3-1.7b\\\": 0.8326,\\n      \\\"qwen3-8b\\\": 0.7127\\n    },\\n    \\\"binary_f1\\\": 0.7056,\\n    \\\"binary_ci\\\": [\\n      0.6997,\\n      0.7113\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.6779,\\n      \\\"mistral-7b-v0.3\\\": 0.4586,\\n      \\\"olmo-2-1b\\\": 0.689,\\n      \\\"pythia-1b\\\": 0.7951,\\n      \\\"pythia-2.8b\\\": 0.735,\\n      \\\"qwen3-0.6b\\\": 0.7539,\\n      \\\"qwen3-1.7b\\\": 0.7597,\\n      \\\"qwen3-8b\\\": 0.6534\\n    }\\n  },\\n  \\\"7feature_ours\\\": {\\n    \\\"3class_f1\\\": 0.7347,\\n    \\\"3class_ci\\\": [\\n      0.7299,\\n      0.7392\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5946,\\n      \\\"mistral-7b-v0.3\\\": 0.4519,\\n      \\\"olmo-2-1b\\\": 0.7497,\\n      \\\"pythia-1b\\\": 0.8384,\\n      \\\"pythia-2.8b\\\": 0.7918,\\n      \\\"qwen3-0.6b\\\": 0.7975,\\n      \\\"qwen3-1.7b\\\": 0.7899,\\n      \\\"qwen3-8b\\\": 0.6688\\n    },\\n    \\\"binary_f1\\\": 0.6913,\\n    \\\"binary_ci\\\": [\\n      0.6855,\\n      0.697\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.4715,\\n      \\\"mistral-7b-v0.3\\\": 0.3658,\\n      \\\"olmo-2-1b\\\": 0.6872,\\n      \\\"pythia-1b\\\": 0.799,\\n      \\\"pythia-2.8b\\\": 0.7347,\\n      \\\"qwen3-0.6b\\\": 0.7514,\\n      \\\"qwen3-1.7b\\\": 0.7585,\\n      \\\"qwen3-8b\\\": 0.657\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "c692e160-0384-4c64-b284-c4d4fccdf2f3",
  "uuid": "2dae7ebb-e9e7-4a37-a828-762024a99441",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"{\\\\n  \\\\\\\"avg_logprob\\\\\\\": {\\\\n    \\\\\\\"3class_f1\\\\\\\": 0.7085,\\\\n    \\\\\\\"3class_ci\\\\\\\": [\\\\n      0.7037,\\\\n      0.7127\\\\n    ],\\\\n    \\\\\\\"per_gen_3class\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.5689,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.4696,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.7343,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.7991,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.7654,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.7484,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.7599,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.6324\\\\n    },\\\\n    \\\\\\\"binary_f1\\\\\\\": 0.6785,\\\\n    \\\\\\\"binary_ci\\\\\\\": [\\\\n      0.6729,\\\\n      0.6844\\\\n    ],\\\\n    \\\\\\\"per_gen_binary\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.4801,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.3682,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.7032,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.7636,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.7183,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.7323,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.7372,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.6345\\\\n    }\\\\n  },\\\\n  \\\\\\\"fastdetectgpt\\\\\\\": {\\\\n    \\\\\\\"3class_f1\\\\\\\": 0.6654,\\\\n    \\\\\\\"3class_ci\\\\\\\": [\\\\n      0.6608,\\\\n      0.6698\\\\n    ],\\\\n    \\\\\\\"per_gen_3class\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.5723,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.5438,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.6622,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.7361,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.7158,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.7181,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.6929,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.5953\\\\n    },\\\\n    \\\\\\\"binary_f1\\\\\\\": 0.5805,\\\\n    \\\\\\\"binary_ci\\\\\\\": [\\\\n      0.5747,\\\\n      0.5863\\\\n    ],\\\\n    \\\\\\\"per_gen_binary\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.463,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.4119,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.5866,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.6679,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.6283,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.6408,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.6172,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.5123\\\\n    }\\\\n  },\\\\n  \\\\\\\"binoculars\\\\\\\": {\\\\n    \\\\\\\"3class_f1\\\\\\\": 0.4094,\\\\n    \\\\\\\"3class_ci\\\\\\\": [\\\\n      0.4042,\\\\n      0.4138\\\\n    ],\\\\n    \\\\\\\"per_gen_3class\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.3397,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.3185,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.4137,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.4205,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.4457,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.4006,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.4249,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.4161\\\\n    },\\\\n    \\\\\\\"binary_f1\\\\\\\": 0.5327,\\\\n    \\\\\\\"binary_ci\\\\\\\": [\\\\n      0.5267,\\\\n      0.5389\\\\n    ],\\\\n    \\\\\\\"per_gen_binary\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.4985,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.3825,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.535,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.5455,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.5458,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.547,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.541,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.5285\\\\n    }\\\\n  },\\\\n  \\\\\\\"ld_score\\\\\\\": {\\\\n    \\\\\\\"3class_f1\\\\\\\": 0.6319,\\\\n    \\\\\\\"3class_ci\\\\\\\": [\\\\n      0.6269,\\\\n      0.6368\\\\n    ],\\\\n    \\\\\\\"per_gen_3class\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.5473,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.4648,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.6356,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.732,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.6778,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.6905,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.6544,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.5505\\\\n    },\\\\n    \\\\\\\"binary_f1\\\\\\\": 0.6782,\\\\n    \\\\\\\"binary_ci\\\\\\\": [\\\\n      0.6726,\\\\n      0.6845\\\\n    ],\\\\n    \\\\\\\"per_gen_binary\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.5769,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.4744,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.6678,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.7664,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.7227,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.7232,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.7121,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.6255\\\\n    }\\\\n  },\\\\n  \\\\\\\"4det_ensemble\\\\\\\": {\\\\n    \\\\\\\"3class_f1\\\\\\\": 0.7783,\\\\n    \\\\\\\"3class_ci\\\\\\\": [\\\\n      0.7741,\\\\n      0.7822\\\\n    ],\\\\n    \\\\\\\"per_gen_3class\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.7537,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.6044,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.7807,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.8445,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.8126,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.8246,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.8204,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.701\\\\n    },\\\\n    \\\\\\\"binary_f1\\\\\\\": 0.6984,\\\\n    \\\\\\\"binary_ci\\\\\\\": [\\\\n      0.6931,\\\\n      0.7044\\\\n    ],\\\\n    \\\\\\\"per_gen_binary\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.6898,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.4724,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.6969,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.7789,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.7245,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.743,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.7453,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.6348\\\\n    }\\\\n  },\\\\n  \\\\\\\"4det_surface\\\\\\\": {\\\\n    \\\\\\\"3class_f1\\\\\\\": 0.7826,\\\\n    \\\\\\\"3class_ci\\\\\\\": [\\\\n      0.7788,\\\\n      0.7868\\\\n    ],\\\\n    \\\\\\\"per_gen_3class\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.7509,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.5909,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.7748,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.8571,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.8183,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.8292,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.8326,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.7127\\\\n    },\\\\n    \\\\\\\"binary_f1\\\\\\\": 0.7056,\\\\n    \\\\\\\"binary_ci\\\\\\\": [\\\\n      0.6997,\\\\n      0.7113\\\\n    ],\\\\n    \\\\\\\"per_gen_binary\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.6779,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.4586,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.689,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.7951,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.735,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.7539,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.7597,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.6534\\\\n    }\\\\n  },\\\\n  \\\\\\\"7feature_ours\\\\\\\": {\\\\n    \\\\\\\"3class_f1\\\\\\\": 0.7347,\\\\n    \\\\\\\"3class_ci\\\\\\\": [\\\\n      0.7299,\\\\n      0.7392\\\\n    ],\\\\n    \\\\\\\"per_gen_3class\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.5946,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.4519,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.7497,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.8384,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.7918,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.7975,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.7899,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.6688\\\\n    },\\\\n    \\\\\\\"binary_f1\\\\\\\": 0.6913,\\\\n    \\\\\\\"binary_ci\\\\\\\": [\\\\n      0.6855,\\\\n      0.697\\\\n    ],\\\\n    \\\\\\\"per_gen_binary\\\\\\\": {\\\\n      \\\\\\\"llama-3.2-3b\\\\\\\": 0.4715,\\\\n      \\\\\\\"mistral-7b-v0.3\\\\\\\": 0.3658,\\\\n      \\\\\\\"olmo-2-1b\\\\\\\": 0.6872,\\\\n      \\\\\\\"pythia-1b\\\\\\\": 0.799,\\\\n      \\\\\\\"pythia-2.8b\\\\\\\": 0.7347,\\\\n      \\\\\\\"qwen3-0.6b\\\\\\\": 0.7514,\\\\n      \\\\\\\"qwen3-1.7b\\\\\\\": 0.7585,\\\\n      \\\\\\\"qwen3-8b\\\\\\\": 0.657\\\\n    }\\\\n  }\\\\n}\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.32}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"avg_logprob\\\": {\\n    \\\"3class_f1\\\": 0.7085,\\n    \\\"3class_ci\\\": [\\n      0.7037,\\n      0.7127\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5689,\\n      \\\"mistral-7b-v0.3\\\": 0.4696,\\n      \\\"olmo-2-1b\\\": 0.7343,\\n      \\\"pythia-1b\\\": 0.7991,\\n      \\\"pythia-2.8b\\\": 0.7654,\\n      \\\"qwen3-0.6b\\\": 0.7484,\\n      \\\"qwen3-1.7b\\\": 0.7599,\\n      \\\"qwen3-8b\\\": 0.6324\\n    },\\n    \\\"binary_f1\\\": 0.6785,\\n    \\\"binary_ci\\\": [\\n      0.6729,\\n      0.6844\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.4801,\\n      \\\"mistral-7b-v0.3\\\": 0.3682,\\n      \\\"olmo-2-1b\\\": 0.7032,\\n      \\\"pythia-1b\\\": 0.7636,\\n      \\\"pythia-2.8b\\\": 0.7183,\\n      \\\"qwen3-0.6b\\\": 0.7323,\\n      \\\"qwen3-1.7b\\\": 0.7372,\\n      \\\"qwen3-8b\\\": 0.6345\\n    }\\n  },\\n  \\\"fastdetectgpt\\\": {\\n    \\\"3class_f1\\\": 0.6654,\\n    \\\"3class_ci\\\": [\\n      0.6608,\\n      0.6698\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5723,\\n      \\\"mistral-7b-v0.3\\\": 0.5438,\\n      \\\"olmo-2-1b\\\": 0.6622,\\n      \\\"pythia-1b\\\": 0.7361,\\n      \\\"pythia-2.8b\\\": 0.7158,\\n      \\\"qwen3-0.6b\\\": 0.7181,\\n      \\\"qwen3-1.7b\\\": 0.6929,\\n      \\\"qwen3-8b\\\": 0.5953\\n    },\\n    \\\"binary_f1\\\": 0.5805,\\n    \\\"binary_ci\\\": [\\n      0.5747,\\n      0.5863\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.463,\\n      \\\"mistral-7b-v0.3\\\": 0.4119,\\n      \\\"olmo-2-1b\\\": 0.5866,\\n      \\\"pythia-1b\\\": 0.6679,\\n      \\\"pythia-2.8b\\\": 0.6283,\\n      \\\"qwen3-0.6b\\\": 0.6408,\\n      \\\"qwen3-1.7b\\\": 0.6172,\\n      \\\"qwen3-8b\\\": 0.5123\\n    }\\n  },\\n  \\\"binoculars\\\": {\\n    \\\"3class_f1\\\": 0.4094,\\n    \\\"3class_ci\\\": [\\n      0.4042,\\n      0.4138\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.3397,\\n      \\\"mistral-7b-v0.3\\\": 0.3185,\\n      \\\"olmo-2-1b\\\": 0.4137,\\n      \\\"pythia-1b\\\": 0.4205,\\n      \\\"pythia-2.8b\\\": 0.4457,\\n      \\\"qwen3-0.6b\\\": 0.4006,\\n      \\\"qwen3-1.7b\\\": 0.4249,\\n      \\\"qwen3-8b\\\": 0.4161\\n    },\\n    \\\"binary_f1\\\": 0.5327,\\n    \\\"binary_ci\\\": [\\n      0.5267,\\n      0.5389\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.4985,\\n      \\\"mistral-7b-v0.3\\\": 0.3825,\\n      \\\"olmo-2-1b\\\": 0.535,\\n      \\\"pythia-1b\\\": 0.5455,\\n      \\\"pythia-2.8b\\\": 0.5458,\\n      \\\"qwen3-0.6b\\\": 0.547,\\n      \\\"qwen3-1.7b\\\": 0.541,\\n      \\\"qwen3-8b\\\": 0.5285\\n    }\\n  },\\n  \\\"ld_score\\\": {\\n    \\\"3class_f1\\\": 0.6319,\\n    \\\"3class_ci\\\": [\\n      0.6269,\\n      0.6368\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5473,\\n      \\\"mistral-7b-v0.3\\\": 0.4648,\\n      \\\"olmo-2-1b\\\": 0.6356,\\n      \\\"pythia-1b\\\": 0.732,\\n      \\\"pythia-2.8b\\\": 0.6778,\\n      \\\"qwen3-0.6b\\\": 0.6905,\\n      \\\"qwen3-1.7b\\\": 0.6544,\\n      \\\"qwen3-8b\\\": 0.5505\\n    },\\n    \\\"binary_f1\\\": 0.6782,\\n    \\\"binary_ci\\\": [\\n      0.6726,\\n      0.6845\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5769,\\n      \\\"mistral-7b-v0.3\\\": 0.4744,\\n      \\\"olmo-2-1b\\\": 0.6678,\\n      \\\"pythia-1b\\\": 0.7664,\\n      \\\"pythia-2.8b\\\": 0.7227,\\n      \\\"qwen3-0.6b\\\": 0.7232,\\n      \\\"qwen3-1.7b\\\": 0.7121,\\n      \\\"qwen3-8b\\\": 0.6255\\n    }\\n  },\\n  \\\"4det_ensemble\\\": {\\n    \\\"3class_f1\\\": 0.7783,\\n    \\\"3class_ci\\\": [\\n      0.7741,\\n      0.7822\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.7537,\\n      \\\"mistral-7b-v0.3\\\": 0.6044,\\n      \\\"olmo-2-1b\\\": 0.7807,\\n      \\\"pythia-1b\\\": 0.8445,\\n      \\\"pythia-2.8b\\\": 0.8126,\\n      \\\"qwen3-0.6b\\\": 0.8246,\\n      \\\"qwen3-1.7b\\\": 0.8204,\\n      \\\"qwen3-8b\\\": 0.701\\n    },\\n    \\\"binary_f1\\\": 0.6984,\\n    \\\"binary_ci\\\": [\\n      0.6931,\\n      0.7044\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.6898,\\n      \\\"mistral-7b-v0.3\\\": 0.4724,\\n      \\\"olmo-2-1b\\\": 0.6969,\\n      \\\"pythia-1b\\\": 0.7789,\\n      \\\"pythia-2.8b\\\": 0.7245,\\n      \\\"qwen3-0.6b\\\": 0.743,\\n      \\\"qwen3-1.7b\\\": 0.7453,\\n      \\\"qwen3-8b\\\": 0.6348\\n    }\\n  },\\n  \\\"4det_surface\\\": {\\n    \\\"3class_f1\\\": 0.7826,\\n    \\\"3class_ci\\\": [\\n      0.7788,\\n      0.7868\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.7509,\\n      \\\"mistral-7b-v0.3\\\": 0.5909,\\n      \\\"olmo-2-1b\\\": 0.7748,\\n      \\\"pythia-1b\\\": 0.8571,\\n      \\\"pythia-2.8b\\\": 0.8183,\\n      \\\"qwen3-0.6b\\\": 0.8292,\\n      \\\"qwen3-1.7b\\\": 0.8326,\\n      \\\"qwen3-8b\\\": 0.7127\\n    },\\n    \\\"binary_f1\\\": 0.7056,\\n    \\\"binary_ci\\\": [\\n      0.6997,\\n      0.7113\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.6779,\\n      \\\"mistral-7b-v0.3\\\": 0.4586,\\n      \\\"olmo-2-1b\\\": 0.689,\\n      \\\"pythia-1b\\\": 0.7951,\\n      \\\"pythia-2.8b\\\": 0.735,\\n      \\\"qwen3-0.6b\\\": 0.7539,\\n      \\\"qwen3-1.7b\\\": 0.7597,\\n      \\\"qwen3-8b\\\": 0.6534\\n    }\\n  },\\n  \\\"7feature_ours\\\": {\\n    \\\"3class_f1\\\": 0.7347,\\n    \\\"3class_ci\\\": [\\n      0.7299,\\n      0.7392\\n    ],\\n    \\\"per_gen_3class\\\": {\\n      \\\"llama-3.2-3b\\\": 0.5946,\\n      \\\"mistral-7b-v0.3\\\": 0.4519,\\n      \\\"olmo-2-1b\\\": 0.7497,\\n      \\\"pythia-1b\\\": 0.8384,\\n      \\\"pythia-2.8b\\\": 0.7918,\\n      \\\"qwen3-0.6b\\\": 0.7975,\\n      \\\"qwen3-1.7b\\\": 0.7899,\\n      \\\"qwen3-8b\\\": 0.6688\\n    },\\n    \\\"binary_f1\\\": 0.6913,\\n    \\\"binary_ci\\\": [\\n      0.6855,\\n      0.697\\n    ],\\n    \\\"per_gen_binary\\\": {\\n      \\\"llama-3.2-3b\\\": 0.4715,\\n      \\\"mistral-7b-v0.3\\\": 0.3658,\\n      \\\"olmo-2-1b\\\": 0.6872,\\n      \\\"pythia-1b\\\": 0.799,\\n      \\\"pythia-2.8b\\\": 0.7347,\\n      \\\"qwen3-0.6b\\\": 0.7514,\\n      \\\"qwen3-1.7b\\\": 0.7585,\\n      \\\"qwen3-8b\\\": 0.657\\n    }\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.32}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 413_

## 报告

### 异常原因

`eval_8gen_baselines.py` 中 `logo_eval` 函数的点估计与 CI 使用了**不同统计量**：

- **点估计**（旧）：`mean(per_generator_F1)` — 8 个 hold-out fold 各自 macro-F1 的算术平均
- **CI**：在 pooled predictions 上做 bootstrap 的 macro-F1

由于 pooled macro-F1 系统性地高于 per-gen mean-F1（pooled 数据类别更均衡），导致 CI 下界 > 点估计这一不可能的现象。

**修正**：点估计改为 pooled macro-F1（`f1_score(all_y_true, all_y_pred, average="macro")`），与 CI 统计量一致。

### 修正数值变化

| Method | Metric | 旧值 | 新值 | 变化 |
|--------|--------|------|------|------|
| avg_logprob | 3class_f1 | 0.6847 | **0.7085** | +0.024 |
| avg_logprob | binary_f1 | 0.6422 | **0.6785** | +0.036 |
| fastdetectgpt | 3class_f1 | 0.6546 | **0.6654** | +0.011 |
| fastdetectgpt | binary_f1 | 0.5660 | **0.5805** | +0.015 |
| binoculars | 3class_f1 | 0.3975 | **0.4094** | +0.012 |
| binoculars | binary_f1 | 0.5155 | **0.5327** | +0.017 |
| ld_score | 3class_f1 | 0.6179 | **0.6319** | +0.014 |
| ld_score | binary_f1 | 0.6570 | **0.6782** | +0.021 |
| 4det_ensemble | 3class_f1 | 0.7687 | **0.7783** | +0.010 |
| 4det_ensemble | binary_f1 | 0.6843 | **0.6984** | +0.014 |
| 4det_surface | 3class_f1 | 0.7712 | **0.7826** | +0.011 |
| 4det_surface | binary_f1 | 0.6903 | **0.7056** | +0.015 |
| 7feature_ours | 3class_f1 | 0.7103 | **0.7347** | +0.024 |
| 7feature_ours | binary_f1 | 0.6531 | **0.6913** | +0.038 |

### 修正后完整表格

| Method | 3-class F1 | 3-class 95% CI | Binary F1 | Binary 95% CI |
|--------|-----------|----------------|-----------|---------------|
| avg_logprob | 0.7085 | [0.7037, 0.7127] | 0.6785 | [0.6729, 0.6844] |
| fastdetectgpt | 0.6654 | [0.6608, 0.6698] | 0.5805 | [0.5747, 0.5863] |
| binoculars | 0.4094 | [0.4042, 0.4138] | 0.5327 | [0.5267, 0.5389] |
| ld_score | 0.6319 | [0.6269, 0.6368] | 0.6782 | [0.6726, 0.6845] |
| 4det_ensemble | 0.7783 | [0.7741, 0.7822] | 0.6984 | [0.6931, 0.7044] |
| 4det_surface | 0.7826 | [0.7788, 0.7868] | 0.7056 | [0.6997, 0.7113] |
| 7feature_ours | 0.7347 | [0.7299, 0.7392] | 0.6913 | [0.6855, 0.6970] |

所有点估计现在都落在各自 CI 内。脚本 `eval_8gen_baselines.py` 已同步修复（pooled F1 + 向量化 JSD 加速）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "c692e160-0384-4c64-b284-c4d4fccdf2f3",
  "uuid": "660ee3f5-89d8-4081-b0c0-b83ebfe82956",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pv3UrbAEBERET3rab4BWXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3836,
      "cache_read_input_tokens": 120476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3836
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

_source line 414_

## 报告

### 异常原因

`eval_8gen_baselines.py` 中 `logo_eval` 函数的点估计与 CI 使用了**不同统计量**：

- **点估计**（旧）：`mean(per_generator_F1)` — 8 个 hold-out fold 各自 macro-F1 的算术平均
- **CI**：在 pooled predictions 上做 bootstrap 的 macro-F1

由于 pooled macro-F1 系统性地高于 per-gen mean-F1（pooled 数据类别更均衡），导致 CI 下界 > 点估计这一不可能的现象。

**修正**：点估计改为 pooled macro-F1（`f1_score(all_y_true, all_y_pred, average="macro")`），与 CI 统计量一致。

### 修正数值变化

| Method | Metric | 旧值 | 新值 | 变化 |
|--------|--------|------|------|------|
| avg_logprob | 3class_f1 | 0.6847 | **0.7085** | +0.024 |
| avg_logprob | binary_f1 | 0.6422 | **0.6785** | +0.036 |
| fastdetectgpt | 3class_f1 | 0.6546 | **0.6654** | +0.011 |
| fastdetectgpt | binary_f1 | 0.5660 | **0.5805** | +0.015 |
| binoculars | 3class_f1 | 0.3975 | **0.4094** | +0.012 |
| binoculars | binary_f1 | 0.5155 | **0.5327** | +0.017 |
| ld_score | 3class_f1 | 0.6179 | **0.6319** | +0.014 |
| ld_score | binary_f1 | 0.6570 | **0.6782** | +0.021 |
| 4det_ensemble | 3class_f1 | 0.7687 | **0.7783** | +0.010 |
| 4det_ensemble | binary_f1 | 0.6843 | **0.6984** | +0.014 |
| 4det_surface | 3class_f1 | 0.7712 | **0.7826** | +0.011 |
| 4det_surface | binary_f1 | 0.6903 | **0.7056** | +0.015 |
| 7feature_ours | 3class_f1 | 0.7103 | **0.7347** | +0.024 |
| 7feature_ours | binary_f1 | 0.6531 | **0.6913** | +0.038 |

### 修正后完整表格

| Method | 3-class F1 | 3-class 95% CI | Binary F1 | Binary 95% CI |
|--------|-----------|----------------|-----------|---------------|
| avg_logprob | 0.7085 | [0.7037, 0.7127] | 0.6785 | [0.6729, 0.6844] |
| fastdetectgpt | 0.6654 | [0.6608, 0.6698] | 0.5805 | [0.5747, 0.5863] |
| binoculars | 0.4094 | [0.4042, 0.4138] | 0.5327 | [0.5267, 0.5389] |
| ld_score | 0.6319 | [0.6269, 0.6368] | 0.6782 | [0.6726, 0.6845] |
| 4det_ensemble | 0.7783 | [0.7741, 0.7822] | 0.6984 | [0.6931, 0.7044] |
| 4det_surface | 0.7826 | [0.7788, 0.7868] | 0.7056 | [0.6997, 0.7113] |
| 7feature_ours | 0.7347 | [0.7299, 0.7392] | 0.6913 | [0.6855, 0.6970] |

所有点估计现在都落在各自 CI 内。脚本 `eval_8gen_baselines.py` 已同步修复（pooled F1 + 向量化 JSD 加速）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1410571,
  "duration_api_ms": 1175574,
  "num_turns": 175,
  "stop_reason": "end_turn",
  "session_id": "c692e160-0384-4c64-b284-c4d4fccdf2f3",
  "total_cost_usd": 9.101745250000004,
  "usage": {
    "input_tokens": 176,
    "cache_creation_input_tokens": 112471,
    "cache_read_input_tokens": 14810275,
    "output_tokens": 39658,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 112471,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1218,
        "cache_read_input_tokens": 120476,
        "cache_creation_input_tokens": 3836,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3836
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1229,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0013340000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 176,
      "outputTokens": 39658,
      "cacheReadInputTokens": 14810275,
      "cacheCreationInputTokens": 112471,
      "webSearchRequests": 0,
      "costUSD": 9.100411250000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ba0a8a77-b9b8-4d2d-ac55-ac3ac6c6fe53"
}
```

</details>

---
