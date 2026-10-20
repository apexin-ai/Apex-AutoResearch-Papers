# research llama3b results — Part 2 of 2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../research-llama3b-results.md) · [Structured JSON](../../../sessions/34/34e2340885a12430dda2.json)

## Round 2

### Tool result

_source line 155 · 2026-05-19T05:22:00.184Z_

<details><summary>↩ Tool result · `toolu_01DZjhRTQmKn7spACvDUdN8F`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    \\\"mmlu_humanities\\\": {\\n      \\\"acc,none\\\": 0.46482465462274175,\\n      \\\"acc_stderr,none\\\": 0.006906849403390851,\\n      \\\"alias\\\": \\\" - humanities\\\"\\n    },\\n--\\n    \\\"mmlu_other\\\": {\\n      \\\"acc,none\\\": 0.5841647891857097,\\n      \\\"acc_stderr,none\\\": 0.00858719547180611,\\n      \\\"alias\\\": \\\" - other\\\"\\n    },\\n--\\n    \\\"mmlu_social_sciences\\\": {\\n      \\\"acc,none\\\": 0.5970100747481313,\\n      \\\"acc_stderr,none\\\": 0.00869725213947898,\\n      \\\"alias\\\": \\\" - social sciences\\\"\\n    },\\n--\\n    \\\"mmlu_stem\\\": {\\n      \\\"acc,none\\\": 0.45734221376466855,\\n      \\\"acc_stderr,none\\\": 0.00868307644112023,\\n      \\\"alias\\\": \\\" - stem\\\"\\n    },\\n--\\n    \\\"mmlu_humanities\\\": {\\n      \\\"acc,none\\\": 0.46482465462274175,\\n      \\\"acc_stderr,none\\\": 0.006906849403390851,\\n      \\\"alias\\\": \\\" - humanities\\\"\\n    },\\n    \\\"mmlu_other\\\": {\\n      \\\"acc,none\\\": 0.5841647891857097,\\n      \\\"acc_stderr,none\\\": 0.00858719547180611,\\n      \\\"alias\\\": \\\" - other\\\"\\n    },\\n    \\\"mmlu_social_sciences\\\": {\\n      \\\"acc,none\\\": 0.5970100747481313,\\n      \\\"acc_stderr,none\\\": 0.00869725213947898,\\n      \\\"alias\\\": \\\" - social sciences\\\"\\n    },\\n    \\\"mmlu_stem\\\": {\\n      \\\"acc,none\\\": 0.45734221376466855,\\n      \\\"acc_stderr,none\\\": 0.00868307644112023,\\n      \\\"alias\\\": \\\" - stem\\\"\\n    }\\n--\\n    \\\"mmlu_humanities\\\": [\\n      \\\"mmlu_formal_logic\\\",\\n      \\\"mmlu_high_school_european_history\\\",\\n      \\\"mmlu_high_school_us_history\\\",\\n      \\\"mmlu_high_school_world_history\\\",\\n--\\n    \\\"mmlu_social_sciences\\\": [\\n      \\\"mmlu_econometrics\\\",\\n      \\\"mmlu_high_school_geography\\\",\\n      \\\"mmlu_high_school_government_and_politics\\\",\\n      \\\"mmlu_high_school_macroeconomics\\\",\\n--\\n    \\\"mmlu_other\\\": [\\n      \\\"mmlu_business_ethics\\\",\\n      \\\"mmlu_clinical_knowledge\\\",\\n      \\\"mmlu_college_medicine\\\",\\n      \\\"mmlu_global_facts\\\",\\n--\\n    \\\"mmlu_stem\\\": [\\n      \\\"mmlu_abstract_algebra\\\",\\n      \\\"mmlu_anatomy\\\",\\n      \\\"mmlu_astronomy\\\",\\n      \\\"mmlu_college_biology\\\",\\n--\\n      \\\"mmlu_stem\\\",\\n      \\\"mmlu_other\\\",\\n      \\\"mmlu_social_sciences\\\",\\n      \\\"mmlu_humanities\\\"\\n    ]\\n  },\\n  \\\"configs\\\": {\\n    \\\"mmlu_abstract_algebra\\\": {\\n--\\n    \\\"mmlu_humanities\\\": 2,\\n    \\\"mmlu_international_law\\\": 1.0,\\n    \\\"mmlu_jurisprudence\\\": 1.0,\\n    \\\"mmlu_logical_fallacies\\\": 1.0,\\n    \\\"mmlu_machine_learning\\\": 1.0,\\n--\\n    \\\"mmlu_other\\\": 2,\\n    \\\"mmlu_philosophy\\\": 1.0,\\n    \\\"mmlu_prehistory\\\": 1.0,\\n    \\\"mmlu_professional_accounting\\\": 1.0,\\n    \\\"mmlu_professional_law\\\": 1.0,\\n--\\n    \\\"mmlu_social_sciences\\\": 2,\\n    \\\"mmlu_sociology\\\": 1.0,\\n    \\\"mmlu_stem\\\": 2,\\n    \\\"mmlu_us_foreign_policy\\\": 1.0,\\n    \\\"mmlu_virology\\\": 1.0,\\n    \\\"mmlu_world_religions\\\": 1.0\\n  },\\n--\\n    \\\"mmlu_humanities\\\": {\\n      \\\"acc\\\": true\\n    },\\n    \\\"mmlu_international_law\\\": {\\n      \\\"acc\\\": true\\n--\\n    \\\"mmlu_other\\\": {\\n      \\\"acc\\\": true\\n    },\\n    \\\"mmlu_philosophy\\\": {\\n      \\\"acc\\\": true\\n--\\n    \\\"mmlu_social_sciences\\\": {\\n      \\\"acc\\\": true\\n    },\\n    \\\"mmlu_sociology\\\": {\\n      \\\"acc\\\": true\\n--\\n    \\\"mmlu_stem\\\": {\\n      \\\"acc\\\": true\\n    },\\n    \\\"mmlu_us_foreign_policy\\\": {\\n      \\\"acc\\\": true\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1240aaf6-101c-4508-aac4-6d4b47f22c2b",
  "uuid": "32080836-4bfd-4741-83dc-731ef5afedf6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    \\\\\\\"mmlu_humanities\\\\\\\": {\\\\n      \\\\\\\"acc,none\\\\\\\": 0.46482465462274175,\\\\n      \\\\\\\"acc_stderr,none\\\\\\\": 0.006906849403390851,\\\\n      \\\\\\\"alias\\\\\\\": \\\\\\\" - humanities\\\\\\\"\\\\n    },\\\\n--\\\\n    \\\\\\\"mmlu_other\\\\\\\": {\\\\n      \\\\\\\"acc,none\\\\\\\": 0.5841647891857097,\\\\n      \\\\\\\"acc_stderr,none\\\\\\\": 0.00858719547180611,\\\\n      \\\\\\\"alias\\\\\\\": \\\\\\\" - other\\\\\\\"\\\\n    },\\\\n--\\\\n    \\\\\\\"mmlu_social_sciences\\\\\\\": {\\\\n      \\\\\\\"acc,none\\\\\\\": 0.5970100747481313,\\\\n      \\\\\\\"acc_stderr,none\\\\\\\": 0.00869725213947898,\\\\n      \\\\\\\"alias\\\\\\\": \\\\\\\" - social sciences\\\\\\\"\\\\n    },\\\\n--\\\\n    \\\\\\\"mmlu_stem\\\\\\\": {\\\\n      \\\\\\\"acc,none\\\\\\\": 0.45734221376466855,\\\\n      \\\\\\\"acc_stderr,none\\\\\\\": 0.00868307644112023,\\\\n      \\\\\\\"alias\\\\\\\": \\\\\\\" - stem\\\\\\\"\\\\n    },\\\\n--\\\\n    \\\\\\\"mmlu_humanities\\\\\\\": {\\\\n      \\\\\\\"acc,none\\\\\\\": 0.46482465462274175,\\\\n      \\\\\\\"acc_stderr,none\\\\\\\": 0.006906849403390851,\\\\n      \\\\\\\"alias\\\\\\\": \\\\\\\" - humanities\\\\\\\"\\\\n    },\\\\n    \\\\\\\"mmlu_other\\\\\\\": {\\\\n      \\\\\\\"acc,none\\\\\\\": 0.5841647891857097,\\\\n      \\\\\\\"acc_stderr,none\\\\\\\": 0.00858719547180611,\\\\n      \\\\\\\"alias\\\\\\\": \\\\\\\" - other\\\\\\\"\\\\n    },\\\\n    \\\\\\\"mmlu_social_sciences\\\\\\\": {\\\\n      \\\\\\\"acc,none\\\\\\\": 0.5970100747481313,\\\\n      \\\\\\\"acc_stderr,none\\\\\\\": 0.00869725213947898,\\\\n      \\\\\\\"alias\\\\\\\": \\\\\\\" - social sciences\\\\\\\"\\\\n    },\\\\n    \\\\\\\"mmlu_stem\\\\\\\": {\\\\n      \\\\\\\"acc,none\\\\\\\": 0.45734221376466855,\\\\n      \\\\\\\"acc_stderr,none\\\\\\\": 0.00868307644112023,\\\\n      \\\\\\\"alias\\\\\\\": \\\\\\\" - stem\\\\\\\"\\\\n    }\\\\n--\\\\n    \\\\\\\"mmlu_humanities\\\\\\\": [\\\\n      \\\\\\\"mmlu_formal_logic\\\\\\\",\\\\n      \\\\\\\"mmlu_high_school_european_history\\\\\\\",\\\\n      \\\\\\\"mmlu_high_school_us_history\\\\\\\",\\\\n      \\\\\\\"mmlu_high_school_world_history\\\\\\\",\\\\n--\\\\n    \\\\\\\"mmlu_social_sciences\\\\\\\": [\\\\n      \\\\\\\"mmlu_econometrics\\\\\\\",\\\\n      \\\\\\\"mmlu_high_school_geography\\\\\\\",\\\\n      \\\\\\\"mmlu_high_school_government_and_politics\\\\\\\",\\\\n      \\\\\\\"mmlu_high_school_macroeconomics\\\\\\\",\\\\n--\\\\n    \\\\\\\"mmlu_other\\\\\\\": [\\\\n      \\\\\\\"mmlu_business_ethics\\\\\\\",\\\\n      \\\\\\\"mmlu_clinical_knowledge\\\\\\\",\\\\n      \\\\\\\"mmlu_college_medicine\\\\\\\",\\\\n      \\\\\\\"mmlu_global_facts\\\\\\\",\\\\n--\\\\n    \\\\\\\"mmlu_stem\\\\\\\": [\\\\n      \\\\\\\"mmlu_abstract_algebra\\\\\\\",\\\\n      \\\\\\\"mmlu_anatomy\\\\\\\",\\\\n      \\\\\\\"mmlu_astronomy\\\\\\\",\\\\n      \\\\\\\"mmlu_college_biology\\\\\\\",\\\\n--\\\\n      \\\\\\\"mmlu_stem\\\\\\\",\\\\n      \\\\\\\"mmlu_other\\\\\\\",\\\\n      \\\\\\\"mmlu_social_sciences\\\\\\\",\\\\n      \\\\\\\"mmlu_humanities\\\\\\\"\\\\n    ]\\\\n  },\\\\n  \\\\\\\"configs\\\\\\\": {\\\\n    \\\\\\\"mmlu_abstract_algebra\\\\\\\": {\\\\n--\\\\n    \\\\\\\"mmlu_humanities\\\\\\\": 2,\\\\n    \\\\\\\"mmlu_international_law\\\\\\\": 1.0,\\\\n    \\\\\\\"mmlu_jurisprudence\\\\\\\": 1.0,\\\\n    \\\\\\\"mmlu_logical_fallacies\\\\\\\": 1.0,\\\\n    \\\\\\\"mmlu_machine_learning\\\\\\\": 1.0,\\\\n--\\\\n    \\\\\\\"mmlu_other\\\\\\\": 2,\\\\n    \\\\\\\"mmlu_philosophy\\\\\\\": 1.0,\\\\n    \\\\\\\"mmlu_prehistory\\\\\\\": 1.0,\\\\n    \\\\\\\"mmlu_professional_accounting\\\\\\\": 1.0,\\\\n    \\\\\\\"mmlu_professional_law\\\\\\\": 1.0,\\\\n--\\\\n    \\\\\\\"mmlu_social_sciences\\\\\\\": 2,\\\\n    \\\\\\\"mmlu_sociology\\\\\\\": 1.0,\\\\n    \\\\\\\"mmlu_stem\\\\\\\": 2,\\\\n    \\\\\\\"mmlu_us_foreign_policy\\\\\\\": 1.0,\\\\n    \\\\\\\"mmlu_virology\\\\\\\": 1.0,\\\\n    \\\\\\\"mmlu_world_religions\\\\\\\": 1.0\\\\n  },\\\\n--\\\\n    \\\\\\\"mmlu_humanities\\\\\\\": {\\\\n      \\\\\\\"acc\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"mmlu_international_law\\\\\\\": {\\\\n      \\\\\\\"acc\\\\\\\": true\\\\n--\\\\n    \\\\\\\"mmlu_other\\\\\\\": {\\\\n      \\\\\\\"acc\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"mmlu_philosophy\\\\\\\": {\\\\n      \\\\\\\"acc\\\\\\\": true\\\\n--\\\\n    \\\\\\\"mmlu_social_sciences\\\\\\\": {\\\\n      \\\\\\\"acc\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"mmlu_sociology\\\\\\\": {\\\\n      \\\\\\\"acc\\\\\\\": true\\\\n--\\\\n    \\\\\\\"mmlu_stem\\\\\\\": {\\\\n      \\\\\\\"acc\\\\\\\": true\\\\n    },\\\\n    \\\\\\\"mmlu_us_foreign_policy\\\\\\\": {\\\\n      \\\\\\\"acc\\\\\\\": true\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    \\\"mmlu_humanities\\\": {\\n      \\\"acc,none\\\": 0.46482465462274175,\\n      \\\"acc_stderr,none\\\": 0.006906849403390851,\\n      \\\"alias\\\": \\\" - humanities\\\"\\n    },\\n--\\n    \\\"mmlu_other\\\": {\\n      \\\"acc,none\\\": 0.5841647891857097,\\n      \\\"acc_stderr,none\\\": 0.00858719547180611,\\n      \\\"alias\\\": \\\" - other\\\"\\n    },\\n--\\n    \\\"mmlu_social_sciences\\\": {\\n      \\\"acc,none\\\": 0.5970100747481313,\\n      \\\"acc_stderr,none\\\": 0.00869725213947898,\\n      \\\"alias\\\": \\\" - social sciences\\\"\\n    },\\n--\\n    \\\"mmlu_stem\\\": {\\n      \\\"acc,none\\\": 0.45734221376466855,\\n      \\\"acc_stderr,none\\\": 0.00868307644112023,\\n      \\\"alias\\\": \\\" - stem\\\"\\n    },\\n--\\n    \\\"mmlu_humanities\\\": {\\n      \\\"acc,none\\\": 0.46482465462274175,\\n      \\\"acc_stderr,none\\\": 0.006906849403390851,\\n      \\\"alias\\\": \\\" - humanities\\\"\\n    },\\n    \\\"mmlu_other\\\": {\\n      \\\"acc,none\\\": 0.5841647891857097,\\n      \\\"acc_stderr,none\\\": 0.00858719547180611,\\n      \\\"alias\\\": \\\" - other\\\"\\n    },\\n    \\\"mmlu_social_sciences\\\": {\\n      \\\"acc,none\\\": 0.5970100747481313,\\n      \\\"acc_stderr,none\\\": 0.00869725213947898,\\n      \\\"alias\\\": \\\" - social sciences\\\"\\n    },\\n    \\\"mmlu_stem\\\": {\\n      \\\"acc,none\\\": 0.45734221376466855,\\n      \\\"acc_stderr,none\\\": 0.00868307644112023,\\n      \\\"alias\\\": \\\" - stem\\\"\\n    }\\n--\\n    \\\"mmlu_humanities\\\": [\\n      \\\"mmlu_formal_logic\\\",\\n      \\\"mmlu_high_school_european_history\\\",\\n      \\\"mmlu_high_school_us_history\\\",\\n      \\\"mmlu_high_school_world_history\\\",\\n--\\n    \\\"mmlu_social_sciences\\\": [\\n      \\\"mmlu_econometrics\\\",\\n      \\\"mmlu_high_school_geography\\\",\\n      \\\"mmlu_high_school_government_and_politics\\\",\\n      \\\"mmlu_high_school_macroeconomics\\\",\\n--\\n    \\\"mmlu_other\\\": [\\n      \\\"mmlu_business_ethics\\\",\\n      \\\"mmlu_clinical_knowledge\\\",\\n      \\\"mmlu_college_medicine\\\",\\n      \\\"mmlu_global_facts\\\",\\n--\\n    \\\"mmlu_stem\\\": [\\n      \\\"mmlu_abstract_algebra\\\",\\n      \\\"mmlu_anatomy\\\",\\n      \\\"mmlu_astronomy\\\",\\n      \\\"mmlu_college_biology\\\",\\n--\\n      \\\"mmlu_stem\\\",\\n      \\\"mmlu_other\\\",\\n      \\\"mmlu_social_sciences\\\",\\n      \\\"mmlu_humanities\\\"\\n    ]\\n  },\\n  \\\"configs\\\": {\\n    \\\"mmlu_abstract_algebra\\\": {\\n--\\n    \\\"mmlu_humanities\\\": 2,\\n    \\\"mmlu_international_law\\\": 1.0,\\n    \\\"mmlu_jurisprudence\\\": 1.0,\\n    \\\"mmlu_logical_fallacies\\\": 1.0,\\n    \\\"mmlu_machine_learning\\\": 1.0,\\n--\\n    \\\"mmlu_other\\\": 2,\\n    \\\"mmlu_philosophy\\\": 1.0,\\n    \\\"mmlu_prehistory\\\": 1.0,\\n    \\\"mmlu_professional_accounting\\\": 1.0,\\n    \\\"mmlu_professional_law\\\": 1.0,\\n--\\n    \\\"mmlu_social_sciences\\\": 2,\\n    \\\"mmlu_sociology\\\": 1.0,\\n    \\\"mmlu_stem\\\": 2,\\n    \\\"mmlu_us_foreign_policy\\\": 1.0,\\n    \\\"mmlu_virology\\\": 1.0,\\n    \\\"mmlu_world_religions\\\": 1.0\\n  },\\n--\\n    \\\"mmlu_humanities\\\": {\\n      \\\"acc\\\": true\\n    },\\n    \\\"mmlu_international_law\\\": {\\n      \\\"acc\\\": true\\n--\\n    \\\"mmlu_other\\\": {\\n      \\\"acc\\\": true\\n    },\\n    \\\"mmlu_philosophy\\\": {\\n      \\\"acc\\\": true\\n--\\n    \\\"mmlu_social_sciences\\\": {\\n      \\\"acc\\\": true\\n    },\\n    \\\"mmlu_sociology\\\": {\\n      \\\"acc\\\": true\\n--\\n    \\\"mmlu_stem\\\": {\\n      \\\"acc\\\": true\\n    },\\n    \\\"mmlu_us_foreign_policy\\\": {\\n      \\\"acc\\\": true\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 156_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data. Let me compile the complete results table.

## Summary of all collected data

### Training Config (both models)
- Model: `unsloth/Llama-3.2-3B` (3.21B params)
- Data: `data/scored_data.jsonl` (371,499 samples, ρ=0.4 contamination)
- Tokens: 200M
- Batch size: 4, grad_accum: 4
- LR: 5e-5


- Max length: 2048
- Seed: 42
- bf16, gradient checkpointing
- Steps: 6,103
- Training time: ~26h each
- Server: westd-41312

### PPL Results

Generating markdown table...

I'm noticing the PPL results aren't directly comparable since the eval token counts differ significantly—the adaptive model evaluated on 2.6x more tokens than uniform. There's also a discrepancy in the reported numbers: Memory.md claims uniform PPL is 10.53, but that value doesn't appear in any server logs—the only verifiable uniform result is 10.38.

### MMLU (5-shot)

Generating markdown table... Generating benchmark comparison table...

Now I'm noting several critical issues with these results. The perplexity evaluations aren't directly comparable since the uniform model was tested on 1.5M tokens while the adaptive used 4.0M, and there's a discrepancy with the reported PPL value for uniform that I can't verify from the server files. The adaptive model is missing 0-shot results for ARC, PIQA, and WinoGrande entirely, and the HellaSwag scores come from different experimental configurations. There's also a concerning pattern in the registry where the adaptive model is marked as "negative" while uniform shows "success," plus the adaptive training had reliability issues with multiple process failures.

The metrics I'm recovering from memory.md suggest the adaptive model's results may be incomplete due to those training interruptions and lack of proper logging.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1240aaf6-101c-4508-aac4-6d4b47f22c2b",
  "uuid": "55bf0715-02e6-41f8-ba97-8da688f8bc15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JymxN1hW3JgiYM93KemRc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4818,
      "cache_read_input_tokens": 82705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4818
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

_source line 157_

数据收集完成。以下是完整结果表。

---

## Llama-3.2-3B Cross-Architecture 实验完整结果

### 训练配置

| 参数 | 值 |
|------|-----|
| Model | `unsloth/Llama-3.2-3B` (3.21B params) |
| Data | `data/scored_data.jsonl` (371,499 samples, ρ=0.4) |
| Tokens | 200M |
| Batch size | 4 (grad_accum=4, effective=16) |
| LR | 5e-5 |
| Max length | 2048 |
| Seed | 42 |
| Precision | bf16 + gradient checkpointing |
| Steps | 6,103 |
| Runtime | ~26h each |
| Server | westd-41312 (RTX PRO 6000 Blackwell) |
| Adaptive τ | 0.8, n_min=2 |

---

### PPL (Holdout Perplexity)

| exp_id | Method | Eval Loss | PPL | Eval Tokens | Source |
|--------|--------|-----------|-----|-------------|--------|
| `llama3b_uniform_seed42` | Uniform | 2.3397 | **10.38** | 1,526,195 | eval log + registry |
| `llama3b_adaptive_seed42` | Adaptive | 2.3590 | **10.58** | 4,017,316 | reeval JSON + registry |

> **⚠️ PPL 不可直接比较**: eval tokens 差 2.6x（1.5M vs 4.0M），说明使用了不同 eval 配置。memory.md 记录的 uniform PPL=10.53 在服务器上找不到对应 eval 文件，唯一可验证值为 10.38。

---

### MMLU (5-shot, lm-eval-harness v0.4.11)

| Category | Uniform (%) | Adaptive (%) | Δ (pp) |
|----------|-------------|--------------|--------|
| **Overall** | **51.85** ± 0.41 | **53.42** ± 0.41 | **+1.57** |
| Humanities | 46.48 ± 0.69 | 48.88 ± 0.70 | +2.40 |
| Social Sciences | 59.70 ± 0.87 | 61.39 ± 0.86 | +1.69 |
| STEM | 45.73 ± 0.87 | 45.99 ± 0.87 | +0.25 |
| Other | 58.42 ± 0.86 | 59.93 ± 0.85 | +1.51 |

Source: `llama3b_uniform_mmlu` / `llama3b_adaptive_lm_eval` (westd-41312)

---

### HellaSwag (10-shot)

| Model | acc (%) | acc_norm (%) | Source |
|-------|---------|-------------|--------|
| Uniform | 54.08 ± 0.50 | **73.08** ± 0.44 | `llama3b_uniform_hellaswag` |
| Adaptive | 53.63 ± 0.50 | **72.49** ± 0.45 | `llama3b_adaptive_lm_eval` (first run) |
| **Δ** | **-0.45** | **-0.60** | |

---

### 0-shot Downstream (uniform only)

| Benchmark | acc (%) | acc_norm (%) | Source |
|-----------|---------|-------------|--------|
| ARC-Easy | 72.18 ± 0.92 | 68.43 ± 0.95 | `qwen_uniform_downstream` |
| HellaSwag | 52.77 ± 0.50 | 70.46 ± 0.46 | `qwen_uniform_downstream` |
| PIQA | 76.22 ± 0.99 | 76.93 ± 0.98 | `qwen_uniform_downstream` |
| WinoGrande | 68.90 ± 1.30 | — | `qwen_uniform_downstream` |

> **Adaptive 模型缺少 0-shot ARC/PIQA/WinoGrande 评测。**

---

### 总结

| Metric | Uniform | Adaptive | Δ | 方向 |
|--------|---------|----------|---|------|
| PPL | 10.38* | 10.58* | +0.20* | ❌ adaptive worse |
| MMLU (5-shot) | 51.85% | 53.42% | +1.57pp | ✅ adaptive better |
| HellaSwag (10-shot, acc_norm) | 73.08% | 72.49% | -0.60pp | ❌ adaptive worse |

\* PPL eval 配置不一致，需要用相同数据重新评测才能公平比较。

---

### 需要注意的问题

1. **PPL eval 不一致**: uniform 用 2000 docs (1.5M tokens)，adaptive 用 4.0M tokens。需要统一 eval 才能比较。
2. **memory.md PPL=10.53 来源不明**: 服务器上没有对应文件，可能是某次未保存的 eval 或记录错误。
3. **Adaptive 缺少 0-shot downstream**: ARC/PIQA/WinoGrande 只有 uniform 的结果。
4. **Registry 结论**: adaptive 标记为 `negative`，uniform 标记为 `success`。Adaptive 训练过程中 process died 5 次，W&B 缺失。
5. **第三个脚本 `run_llama3b_adaptive_tau09_seed42.sh`**: 使用 τ=0.9, ρ=0.2 的配置（数据为 `scored_data_rho02.jsonl`），但 registry 中没有对应实验记录，可能未运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1240aaf6-101c-4508-aac4-6d4b47f22c2b",
  "uuid": "1d495eca-d14d-46d7-9f61-f88bd923f6d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JymxN1hW3JgiYM93KemRc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4818,
      "cache_read_input_tokens": 82705,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4818
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

_source line 158_

数据收集完成。以下是完整结果表。

---

## Llama-3.2-3B Cross-Architecture 实验完整结果

### 训练配置

| 参数 | 值 |
|------|-----|
| Model | `unsloth/Llama-3.2-3B` (3.21B params) |
| Data | `data/scored_data.jsonl` (371,499 samples, ρ=0.4) |
| Tokens | 200M |
| Batch size | 4 (grad_accum=4, effective=16) |
| LR | 5e-5 |
| Max length | 2048 |
| Seed | 42 |
| Precision | bf16 + gradient checkpointing |
| Steps | 6,103 |
| Runtime | ~26h each |
| Server | westd-41312 (RTX PRO 6000 Blackwell) |
| Adaptive τ | 0.8, n_min=2 |

---

### PPL (Holdout Perplexity)

| exp_id | Method | Eval Loss | PPL | Eval Tokens | Source |
|--------|--------|-----------|-----|-------------|--------|
| `llama3b_uniform_seed42` | Uniform | 2.3397 | **10.38** | 1,526,195 | eval log + registry |
| `llama3b_adaptive_seed42` | Adaptive | 2.3590 | **10.58** | 4,017,316 | reeval JSON + registry |

> **⚠️ PPL 不可直接比较**: eval tokens 差 2.6x（1.5M vs 4.0M），说明使用了不同 eval 配置。memory.md 记录的 uniform PPL=10.53 在服务器上找不到对应 eval 文件，唯一可验证值为 10.38。

---

### MMLU (5-shot, lm-eval-harness v0.4.11)

| Category | Uniform (%) | Adaptive (%) | Δ (pp) |
|----------|-------------|--------------|--------|
| **Overall** | **51.85** ± 0.41 | **53.42** ± 0.41 | **+1.57** |
| Humanities | 46.48 ± 0.69 | 48.88 ± 0.70 | +2.40 |
| Social Sciences | 59.70 ± 0.87 | 61.39 ± 0.86 | +1.69 |
| STEM | 45.73 ± 0.87 | 45.99 ± 0.87 | +0.25 |
| Other | 58.42 ± 0.86 | 59.93 ± 0.85 | +1.51 |

Source: `llama3b_uniform_mmlu` / `llama3b_adaptive_lm_eval` (westd-41312)

---

### HellaSwag (10-shot)

| Model | acc (%) | acc_norm (%) | Source |
|-------|---------|-------------|--------|
| Uniform | 54.08 ± 0.50 | **73.08** ± 0.44 | `llama3b_uniform_hellaswag` |
| Adaptive | 53.63 ± 0.50 | **72.49** ± 0.45 | `llama3b_adaptive_lm_eval` (first run) |
| **Δ** | **-0.45** | **-0.60** | |

---

### 0-shot Downstream (uniform only)

| Benchmark | acc (%) | acc_norm (%) | Source |
|-----------|---------|-------------|--------|
| ARC-Easy | 72.18 ± 0.92 | 68.43 ± 0.95 | `qwen_uniform_downstream` |
| HellaSwag | 52.77 ± 0.50 | 70.46 ± 0.46 | `qwen_uniform_downstream` |
| PIQA | 76.22 ± 0.99 | 76.93 ± 0.98 | `qwen_uniform_downstream` |
| WinoGrande | 68.90 ± 1.30 | — | `qwen_uniform_downstream` |

> **Adaptive 模型缺少 0-shot ARC/PIQA/WinoGrande 评测。**

---

### 总结

| Metric | Uniform | Adaptive | Δ | 方向 |
|--------|---------|----------|---|------|
| PPL | 10.38* | 10.58* | +0.20* | ❌ adaptive worse |
| MMLU (5-shot) | 51.85% | 53.42% | +1.57pp | ✅ adaptive better |
| HellaSwag (10-shot, acc_norm) | 73.08% | 72.49% | -0.60pp | ❌ adaptive worse |

\* PPL eval 配置不一致，需要用相同数据重新评测才能公平比较。

---

### 需要注意的问题

1. **PPL eval 不一致**: uniform 用 2000 docs (1.5M tokens)，adaptive 用 4.0M tokens。需要统一 eval 才能比较。
2. **memory.md PPL=10.53 来源不明**: 服务器上没有对应文件，可能是某次未保存的 eval 或记录错误。
3. **Adaptive 缺少 0-shot downstream**: ARC/PIQA/WinoGrande 只有 uniform 的结果。
4. **Registry 结论**: adaptive 标记为 `negative`，uniform 标记为 `success`。Adaptive 训练过程中 process died 5 次，W&B 缺失。
5. **第三个脚本 `run_llama3b_adaptive_tau09_seed42.sh`**: 使用 τ=0.9, ρ=0.2 的配置（数据为 `scored_data_rho02.jsonl`），但 registry 中没有对应实验记录，可能未运行。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 445192,
  "duration_api_ms": 439956,
  "num_turns": 47,
  "stop_reason": "end_turn",
  "session_id": "1240aaf6-101c-4508-aac4-6d4b47f22c2b",
  "total_cost_usd": 1.888212,
  "usage": {
    "input_tokens": 22,
    "cache_creation_input_tokens": 75682,
    "cache_read_input_tokens": 913215,
    "output_tokens": 16774,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 75682,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2842,
        "cache_read_input_tokens": 82705,
        "cache_creation_input_tokens": 4818,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4818
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1121,
      "outputTokens": 25,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0012460000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 35,
      "outputTokens": 25425,
      "cacheReadInputTokens": 1049632,
      "cacheCreationInputTokens": 116216,
      "webSearchRequests": 0,
      "costUSD": 1.8869660000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5d5357aa-933b-4df3-bd7b-7f92f45e152b"
}
```

</details>

---
