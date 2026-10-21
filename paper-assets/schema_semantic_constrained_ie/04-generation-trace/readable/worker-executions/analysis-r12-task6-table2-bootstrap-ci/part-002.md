# analysis r12 task6 table2 bootstrap ci — Part 2 of 2

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../analysis-r12-task6-table2-bootstrap-ci.md) · [Structured JSON](../../../sessions/a2/a27575c139176053fba6.json)

## Round 1

### Assistant

_source line 204_

<details><summary>Logged reasoning block</summary>

```text
The JSON is saved correctly. Now let me register the artifact and provide the caption/footnote text.

Let me summarize the key findings:

**Paper Table 2 (SciERC composability):**

| Setting | ΔR-F1 (pp) | 95% CI | p | ΔDR% (pp) | 95% CI | p |
|---------|-----------|--------|---|-----------|--------|---|
| Qwen SciERC | -0.10 | [-0.30, 0.00] | 0.726 | -1.95 | [-2.87, -1.11] | <0.001 |


| Llama SciERC | +0.02 | [0.00, +0.07] | 0.736 | -1.02 | [-1.98, -0.29] | <0.001 |

**Extended (DocRED):**
| Setting | ΔR-F1 (pp) | 95% CI | p | ΔDR% (pp) | 95% CI | p |
|---------|-----------|--------|---|-----------|--------|---|
| Qwen DocRED | -0.31 | [-0.69, +0.01] | 0.056 | -0.75 |

Generating results table...

The key takeaway is that R-F1 scores remain stable across all settings with no statistical significance, while the constraint violations drop dramatically and significantly, which validates that the approach achieves composability without sacrificing performance. Now I'm ready to write the caption and finalize the artifact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "885d0dc2-fe44-4f69-8a62-85dbf90d4d53",
  "uuid": "7ba7543a-7a5c-4eed-b274-e2cf53042470",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vKpQKVfEQQcsKTfp8PYPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3569,
      "cache_read_input_tokens": 116152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3569
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

_source line 205_

结果完全匹配 d066 eval。现在注册 artifact 并生成论文 caption/footnote。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "885d0dc2-fe44-4f69-8a62-85dbf90d4d53",
  "uuid": "09958052-ed7d-4af5-9bc9-dccdc2a21f67",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vKpQKVfEQQcsKTfp8PYPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3569,
      "cache_read_input_tokens": 116152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3569
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

_source line 206_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01DB1a6TkhPNDtoFXWm5XNeQ`</summary>

```json
{
  "name": "r12_table2_bootstrap_ci",
  "type": "data",
  "description": "Bootstrap CI (10k iterations) for Table 2 composability: R-F1 delta and DR% delta with p-values for all 4 model-dataset pairs",
  "project": "schema_semantic_constrained_ie",
  "source_path": "/root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json",
  "tags": [
    "bootstrap",
    "table2",
    "composability",
    "significance"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "885d0dc2-fe44-4f69-8a62-85dbf90d4d53",
  "uuid": "0366c39b-f8dd-4931-8b51-28a79f0fe1cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vKpQKVfEQQcsKTfp8PYPh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3569,
      "cache_read_input_tokens": 116152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3569
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

_source line 207 · 2026-05-20T18:17:45.762Z_

<details><summary>↩ Tool result · `toolu_01DB1a6TkhPNDtoFXWm5XNeQ`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "885d0dc2-fe44-4f69-8a62-85dbf90d4d53",
  "uuid": "1aa8d55e-5f96-4e80-95dc-745083c8f53c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"source_path not found: /root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"source_path not found: /root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 208_

<details><summary>Logged reasoning block</summary>

```text
The source_path is on the remote server, not local. I need to use the `content` parameter instead to register the artifact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "885d0dc2-fe44-4f69-8a62-85dbf90d4d53",
  "uuid": "be8eb6c3-8671-4e31-ae56-1d8bf63af36e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFofzmhX9KhgV6B9iXyz6z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 119721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 949
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


### Tool call

_source line 209_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01CtA7j5Te14kYVgNB3NA6N1`</summary>

```json
{
  "name": "r12_table2_bootstrap_ci",
  "type": "data",
  "description": "Bootstrap CI (10k iterations) for Table 2 composability: R-F1 delta and DR% delta with p-values for all 4 model-dataset pairs",
  "project": "schema_semantic_constrained_ie",
  "content": "See /root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json on westd-16980. Script: /root/schema_semantic_constrained_ie/scripts/r12_bootstrap_ci_table2.py",
  "content_filename": "r12_table2_bootstrap_ci_pointer.txt",
  "tags": [
    "bootstrap",
    "table2",
    "composability",
    "significance"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "885d0dc2-fe44-4f69-8a62-85dbf90d4d53",
  "uuid": "73e760f1-0107-4675-b2b0-368e475a34eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PFofzmhX9KhgV6B9iXyz6z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 949,
      "cache_read_input_tokens": 119721,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 949
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

_source line 210 · 2026-05-20T18:17:54.108Z_

<details><summary>↩ Tool result · `toolu_01CtA7j5Te14kYVgNB3NA6N1`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_69cf8e\", \"name\": \"r12_table2_bootstrap_ci\", \"type\": \"data\", \"description\": \"Bootstrap CI (10k iterations) for Table 2 composability: R-F1 delta and DR% delta with p-values for all 4 model-dataset pairs\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/data/r12_table2_bootstrap_ci_pointer.txt\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T18:17:53.814948+00:00\", \"tags\": [\"bootstrap\", \"table2\", \"composability\", \"significance\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "885d0dc2-fe44-4f69-8a62-85dbf90d4d53",
  "uuid": "2375cd6a-850d-4aee-abaf-ee5a61606db0",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260520_69cf8e\\\", \\\"name\\\": \\\"r12_table2_bootstrap_ci\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Bootstrap CI (10k iterations) for Table 2 composability: R-F1 delta and DR% delta with p-values for all 4 model-dataset pairs\\\", \\\"path\\\": \\\"projects/schema_semantic_constrained_ie/artifacts/_project/data/r12_table2_bootstrap_ci_pointer.txt\\\", \\\"url\\\": null, \\\"project\\\": \\\"schema_semantic_constrained_ie\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-20T18:17:53.814948+00:00\\\", \\\"tags\\\": [\\\"bootstrap\\\", \\\"table2\\\", \\\"composability\\\", \\\"significance\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_69cf8e\", \"name\": \"r12_table2_bootstrap_ci\", \"type\": \"data\", \"description\": \"Bootstrap CI (10k iterations) for Table 2 composability: R-F1 delta and DR% delta with p-values for all 4 model-dataset pairs\", \"path\": \"projects/schema_semantic_constrained_ie/artifacts/_project/data/r12_table2_bootstrap_ci_pointer.txt\", \"url\": null, \"project\": \"schema_semantic_constrained_ie\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T18:17:53.814948+00:00\", \"tags\": [\"bootstrap\", \"table2\", \"composability\", \"significance\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 211_

完成。以下是结果总结和论文 caption 文本。

## 结果

**R-F1 差异（constrained − unconstrained）：所有 n.s.**

| Setting | ΔR-F1 (pp) | 95% CI | p |
|---------|-----------|--------|---|
| Qwen SciERC (n=551) | −0.10 | [−0.30, 0.00] | 0.726 |
| Llama SciERC (n=551) | +0.02 | [0.00, +0.07] | 0.736 |
| Qwen DocRED (n=998) | −0.31 | [−0.69, +0.01] | 0.056 |
| Llama DocRED (n=998) | +0.06 | [−0.11, +0.25] | 0.535 |

**DR% 差异：全部 p < 0.001**

| Setting | ΔDR% (pp) | 95% CI | p |
|---------|-----------|--------|---|
| Qwen SciERC | −1.95 | [−2.87, −1.11] | <0.001 |
| Llama SciERC | −1.02 | [−1.98, −0.29] | <0.001 |
| Qwen DocRED | −0.75 | [−1.07, −0.48] | <0.001 |
| Llama DocRED | −0.29 | [−0.53, −0.10] | <0.001 |

**数据验证**：聚合 TP/FP/FN 与 d066_unified eval 完全一致（e.g. Qwen SciERC unc: tp=461, fp=667, fn=513 → R-F1=43.86%）。

## 论文 Caption/Footnote 文本

用于 Table 2 caption（SciERC composability table）：

> Paired bootstrap test (10{,}000 iterations, document-level resampling): $\Delta$R-F1 between constrained and unconstrained decoding is not statistically significant for either model ($p{>}0.5$, two-sided), while DR reduction is significant for both ($p{<}0.001$, one-sided).

如果需要更详细的 footnote（含 DocRED 的扩展版）：

> Bootstrap significance (10{,}000 iterations, document-level resampling, seed=42): No R-F1 difference reaches significance at $\alpha{=}0.05$ (Qwen $\Delta{=}{-}0.10$\,pp, $p{=}0.73$; Llama $\Delta{=}{+}0.02$\,pp, $p{=}0.74$). DR\% reduction is significant in all settings ($p{<}0.001$). On DocRED (998 docs), results are consistent: R-F1 $\Delta$ ranges from $-0.31$ to $+0.06$\,pp (all $p{>}0.05$) while DR\% reduction remains significant.

**文件位置**：
- JSON: `westd-16980:/root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json`
- 脚本: `westd-16980:/root/schema_semantic_constrained_ie/scripts/r12_bootstrap_ci_table2.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "885d0dc2-fe44-4f69-8a62-85dbf90d4d53",
  "uuid": "2e23d502-01ef-43d7-a139-fc3f14f60938",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMubSsmTZc9qpNwSDZ1ucj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 120670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 641
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

_source line 212_

完成。以下是结果总结和论文 caption 文本。

## 结果

**R-F1 差异（constrained − unconstrained）：所有 n.s.**

| Setting | ΔR-F1 (pp) | 95% CI | p |
|---------|-----------|--------|---|
| Qwen SciERC (n=551) | −0.10 | [−0.30, 0.00] | 0.726 |
| Llama SciERC (n=551) | +0.02 | [0.00, +0.07] | 0.736 |
| Qwen DocRED (n=998) | −0.31 | [−0.69, +0.01] | 0.056 |
| Llama DocRED (n=998) | +0.06 | [−0.11, +0.25] | 0.535 |

**DR% 差异：全部 p < 0.001**

| Setting | ΔDR% (pp) | 95% CI | p |
|---------|-----------|--------|---|
| Qwen SciERC | −1.95 | [−2.87, −1.11] | <0.001 |
| Llama SciERC | −1.02 | [−1.98, −0.29] | <0.001 |
| Qwen DocRED | −0.75 | [−1.07, −0.48] | <0.001 |
| Llama DocRED | −0.29 | [−0.53, −0.10] | <0.001 |

**数据验证**：聚合 TP/FP/FN 与 d066_unified eval 完全一致（e.g. Qwen SciERC unc: tp=461, fp=667, fn=513 → R-F1=43.86%）。

## 论文 Caption/Footnote 文本

用于 Table 2 caption（SciERC composability table）：

> Paired bootstrap test (10{,}000 iterations, document-level resampling): $\Delta$R-F1 between constrained and unconstrained decoding is not statistically significant for either model ($p{>}0.5$, two-sided), while DR reduction is significant for both ($p{<}0.001$, one-sided).

如果需要更详细的 footnote（含 DocRED 的扩展版）：

> Bootstrap significance (10{,}000 iterations, document-level resampling, seed=42): No R-F1 difference reaches significance at $\alpha{=}0.05$ (Qwen $\Delta{=}{-}0.10$\,pp, $p{=}0.73$; Llama $\Delta{=}{+}0.02$\,pp, $p{=}0.74$). DR\% reduction is significant in all settings ($p{<}0.001$). On DocRED (998 docs), results are consistent: R-F1 $\Delta$ ranges from $-0.31$ to $+0.06$\,pp (all $p{>}0.05$) while DR\% reduction remains significant.

**文件位置**：
- JSON: `westd-16980:/root/autodl-tmp/schema_outputs/r12_table2_bootstrap_ci.json`
- 脚本: `westd-16980:/root/schema_semantic_constrained_ie/scripts/r12_bootstrap_ci_table2.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 783659,
  "duration_api_ms": 769171,
  "num_turns": 45,
  "stop_reason": "end_turn",
  "session_id": "885d0dc2-fe44-4f69-8a62-85dbf90d4d53",
  "total_cost_usd": 2.6278170000000007,
  "usage": {
    "input_tokens": 27,
    "cache_creation_input_tokens": 109470,
    "cache_read_input_tokens": 1579992,
    "output_tokens": 36423,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 109470,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 896,
        "cache_read_input_tokens": 120670,
        "cache_creation_input_tokens": 641,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 641
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2258,
      "outputTokens": 4678,
      "cacheReadInputTokens": 1061030,
      "cacheCreationInputTokens": 88938,
      "webSearchRequests": 0,
      "costUSD": 0.24292349999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 27,
      "outputTokens": 36423,
      "cacheReadInputTokens": 1579992,
      "cacheCreationInputTokens": 109470,
      "webSearchRequests": 0,
      "costUSD": 2.3848935000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8e095444-6e92-4c0c-9468-acdc8968ba5d"
}
```

</details>

---
