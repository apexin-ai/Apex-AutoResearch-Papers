# reanalyze gpt2m s43 s42 unified pairs — Part 2 of 2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../reanalyze-gpt2m-s43-s42-unified-pairs.md) · [Structured JSON](../../../sessions/8a/8aeb408fc97587cbad4a.json)

## Before a recorded user message

### Tool result

_source line 162 · 2026-05-19T15:40:42.928Z_

<details><summary>↩ Tool result · `toolu_01SE1EMp2EFFxJoMCRXcGmvi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"exp_id\": \"gen_wiki_gpt2m_a100_s42_v4\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:20:50.055Z\", \"updated_at\": \"2026-05-19T15:40:42.722Z\", \"hypothesis\": \"GPT-2-medium 重跑以产出可审计 artifact：用统一参数 (n_perm=5000, xcorr_lag=5) 验证跨架构泛化，填充 Table 7 GPT-2m 行\", \"parent\": \"\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v4.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T11:28:28.313Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T11:28:30.486134+00:00\"}]}, \"metrics\": {\"pair_config\": \"unified_8pair (ent/ece→d1/d2/d3/mauve)\", \"n_perm\": 5000, \"xcorr_lag\": 5, \"granger_lag\": 1, \"perm_granger_fwd\": \"6/8\", \"perm_granger_rev\": \"3/8\", \"diff_xcorr_fwd\": \"6/8\", \"threshold_onset_fwd\": \"0/8\", \"ty_granger_fwd\": \"2/8\", \"robust_pairs_K3\": \"2/8\", \"robust_pairs_K4\": \"0/8\", \"mmct_uniform_fwd\": 0.25, \"mmct_wpair_fwd\": 0.75, \"final_ppl\": 16520.5, \"final_entropy_drift\": \"-86.6%\", \"final_ppl_drift\": \"+50527.6%\", \"D101_note\": \"Rerun with unified pairs (mauve replaces perplexity). mauve pairs weak (1/5 votes max). Old: pg_fwd=6/8, ty=5/8, k_gte4=6/8 (with perplexity as downstream).\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:34:34.397Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4817}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5067784d-e0df-4fea-af4e-29911a648d18",
  "uuid": "594d7ce3-e5ea-46d6-9cec-a31ea235ad3c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"exp_id\\\": \\\"gen_wiki_gpt2m_a100_s42_v4\\\", \\\"experiment\\\": {\\\"status\\\": \\\"DONE\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-18T01:20:50.055Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:40:42.722Z\\\", \\\"hypothesis\\\": \\\"GPT-2-medium 重跑以产出可审计 artifact：用统一参数 (n_perm=5000, xcorr_lag=5) 验证跨架构泛化，填充 Table 7 GPT-2m 行\\\", \\\"parent\\\": \\\"\\\", \\\"spec\\\": {\\\"checkpoint_path\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/\\\", \\\"log_path\\\": \\\"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v4.log\\\"}, \\\"reproduce\\\": {\\\"finished_at\\\": \\\"2026-05-18T11:28:28.313Z\\\"}, \\\"extra\\\": {\\\"hook_events\\\": [{\\\"event\\\": \\\"on_complete\\\", \\\"action\\\": \\\"agent\\\", \\\"ts\\\": \\\"2026-05-18T11:28:30.486134+00:00\\\"}]}, \\\"metrics\\\": {\\\"pair_config\\\": \\\"unified_8pair (ent/ece→d1/d2/d3/mauve)\\\", \\\"n_perm\\\": 5000, \\\"xcorr_lag\\\": 5, \\\"granger_lag\\\": 1, \\\"perm_granger_fwd\\\": \\\"6/8\\\", \\\"perm_granger_rev\\\": \\\"3/8\\\", \\\"diff_xcorr_fwd\\\": \\\"6/8\\\", \\\"threshold_onset_fwd\\\": \\\"0/8\\\", \\\"ty_granger_fwd\\\": \\\"2/8\\\", \\\"robust_pairs_K3\\\": \\\"2/8\\\", \\\"robust_pairs_K4\\\": \\\"0/8\\\", \\\"mmct_uniform_fwd\\\": 0.25, \\\"mmct_wpair_fwd\\\": 0.75, \\\"final_ppl\\\": 16520.5, \\\"final_entropy_drift\\\": \\\"-86.6%\\\", \\\"final_ppl_drift\\\": \\\"+50527.6%\\\", \\\"D101_note\\\": \\\"Rerun with unified pairs (mauve replaces perplexity). mauve pairs weak (1/5 votes max). Old: pg_fwd=6/8, ty=5/8, k_gte4=6/8 (with perplexity as downstream).\\\"}, \\\"conclusion\\\": \\\"success\\\", \\\"completed_at\\\": \\\"2026-05-18T11:34:34.397Z\\\"}}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.4817}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"exp_id\": \"gen_wiki_gpt2m_a100_s42_v4\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T01:20:50.055Z\", \"updated_at\": \"2026-05-19T15:40:42.722Z\", \"hypothesis\": \"GPT-2-medium 重跑以产出可审计 artifact：用统一参数 (n_perm=5000, xcorr_lag=5) 验证跨架构泛化，填充 Table 7 GPT-2m 行\", \"parent\": \"\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/distrib_canary_collapse/results/generalize/gpt2m_wiki_a100_s42/\", \"log_path\": \"~/runs/distrib_canary_collapse/gen_wiki_gpt2m_a100_s42_v4.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T11:28:28.313Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T11:28:30.486134+00:00\"}]}, \"metrics\": {\"pair_config\": \"unified_8pair (ent/ece→d1/d2/d3/mauve)\", \"n_perm\": 5000, \"xcorr_lag\": 5, \"granger_lag\": 1, \"perm_granger_fwd\": \"6/8\", \"perm_granger_rev\": \"3/8\", \"diff_xcorr_fwd\": \"6/8\", \"threshold_onset_fwd\": \"0/8\", \"ty_granger_fwd\": \"2/8\", \"robust_pairs_K3\": \"2/8\", \"robust_pairs_K4\": \"0/8\", \"mmct_uniform_fwd\": 0.25, \"mmct_wpair_fwd\": 0.75, \"final_ppl\": 16520.5, \"final_entropy_drift\": \"-86.6%\", \"final_ppl_drift\": \"+50527.6%\", \"D101_note\": \"Rerun with unified pairs (mauve replaces perplexity). mauve pairs weak (1/5 votes max). Old: pg_fwd=6/8, ty=5/8, k_gte4=6/8 (with perplexity as downstream).\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T11:34:34.397Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4817}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 163_

Registry 更新完成。汇总报告：

---

## D101 结果：GPT-2m 统一 Downstream Pair 重分析

### Pair 配置变更
- **旧**: ent/ece → d1, d2, d3, **perplexity** (8 pairs)
- **新**: ent/ece → d1, d2, d3, **mauve** (8 pairs)

### GPT-2m s43 新旧对比

| 指标 | 旧 (含 ppl) | 新 (含 mauve) | 变化原因 |
|------|-----------|-------------|---------|
| PermG fwd | 8/8 | **6/8** | mauve 2 pairs 不显著 (p=0.33, 0.49) |
| PermG rev | 5/8 | **4/8** | mauve→ece 丢失 |
| Diff XCorr fwd | 8/8 | **6/8** | mauve pairs DiffFDR=0.24 |
| TY fwd | 4/8 | 4/8 | 不变 |
| Threshold | 0/8 | 0/8 | 不变 |
| K≥3 | 4/8 | 4/8 | 不变 |
| K≥4 | 1/8 | 1/8 | 不变 |
| MMCT uniform | — | 4/8 (50%) | |
| MMCT wpair | — | 6/8 (75%) | |

### GPT-2m s42 新旧对比

| 指标 | 旧 (含 ppl) | 新 (含 mauve) | 变化原因 |
|------|-----------|-------------|---------|
| PermG fwd | 6/8 | 6/8 | 不变 (ppl/mauve 都不 sig) |
| PermG rev | 3/8 | 3/8 | 不变 |
| TY fwd | 5/8 | **2/8** | ppl 的 TY 显著被 mauve 的不显著取代 |
| K≥3 (5method) | — | 2/8 | 保守 consensus |
| K≥4 (5method) | — | 0/8 | |
| MMCT uniform | — | 2/8 (25%) | |
| MMCT wpair | — | 6/8 (75%) | |

### 跨 Seed 一致性

| 指标 | s43 | s42 |
|------|-----|-----|
| PermG fwd | 6/8 | 6/8 | **一致** |
| PermG rev | 4/8 | 3/8 | 近似 |
| K≥3 | 4/8 | 2/8 | s42 较弱（ece→d2/d3 在 s42 中 TY 不显著） |
| MMCT wpair | 75% | 75% | **一致** |

### 关键发现

1. **Mauve 作为 downstream 在 T=11 下信号极弱**：所有 mauve pair 的 PermG p>0.10，DiffXCorr FDR>0.07。mauve 变化幅度仅 +7.9% (s43) / +7.9% (s42)，相比 distinct 指标 -12~-14% 的 drift，信噪比不足。

2. **Core distinct pairs 不受影响**：K≥3 和 K≥4 的 robust pairs 完全由 distinct 指标驱动，不含 ppl 或 mauve。统一 pair 后这些核心结论不变。

3. **PermG fwd 从 8/8 降到 6/8（s43）**：纯粹因为去掉了 ppl pairs（ppl drift +50527% 信号极强），换成 mauve（drift 仅 ~8%）。这是 apples-to-apples 对比的正确代价。

4. **MMCT wpair 跨 seed 稳定在 75%**：FPR 逆加权后，distinct pairs 的强信号补偿了 mauve 的弱信号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5067784d-e0df-4fea-af4e-29911a648d18",
  "uuid": "f40f446d-0c2d-4118-829d-d235b5846e1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013iSKmxmcnEMoL8dCWHA9Kw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9215,
      "cache_read_input_tokens": 131032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9215
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

_source line 164_

Registry 更新完成。汇总报告：

---

## D101 结果：GPT-2m 统一 Downstream Pair 重分析

### Pair 配置变更
- **旧**: ent/ece → d1, d2, d3, **perplexity** (8 pairs)
- **新**: ent/ece → d1, d2, d3, **mauve** (8 pairs)

### GPT-2m s43 新旧对比

| 指标 | 旧 (含 ppl) | 新 (含 mauve) | 变化原因 |
|------|-----------|-------------|---------|
| PermG fwd | 8/8 | **6/8** | mauve 2 pairs 不显著 (p=0.33, 0.49) |
| PermG rev | 5/8 | **4/8** | mauve→ece 丢失 |
| Diff XCorr fwd | 8/8 | **6/8** | mauve pairs DiffFDR=0.24 |
| TY fwd | 4/8 | 4/8 | 不变 |
| Threshold | 0/8 | 0/8 | 不变 |
| K≥3 | 4/8 | 4/8 | 不变 |
| K≥4 | 1/8 | 1/8 | 不变 |
| MMCT uniform | — | 4/8 (50%) | |
| MMCT wpair | — | 6/8 (75%) | |

### GPT-2m s42 新旧对比

| 指标 | 旧 (含 ppl) | 新 (含 mauve) | 变化原因 |
|------|-----------|-------------|---------|
| PermG fwd | 6/8 | 6/8 | 不变 (ppl/mauve 都不 sig) |
| PermG rev | 3/8 | 3/8 | 不变 |
| TY fwd | 5/8 | **2/8** | ppl 的 TY 显著被 mauve 的不显著取代 |
| K≥3 (5method) | — | 2/8 | 保守 consensus |
| K≥4 (5method) | — | 0/8 | |
| MMCT uniform | — | 2/8 (25%) | |
| MMCT wpair | — | 6/8 (75%) | |

### 跨 Seed 一致性

| 指标 | s43 | s42 |
|------|-----|-----|
| PermG fwd | 6/8 | 6/8 | **一致** |
| PermG rev | 4/8 | 3/8 | 近似 |
| K≥3 | 4/8 | 2/8 | s42 较弱（ece→d2/d3 在 s42 中 TY 不显著） |
| MMCT wpair | 75% | 75% | **一致** |

### 关键发现

1. **Mauve 作为 downstream 在 T=11 下信号极弱**：所有 mauve pair 的 PermG p>0.10，DiffXCorr FDR>0.07。mauve 变化幅度仅 +7.9% (s43) / +7.9% (s42)，相比 distinct 指标 -12~-14% 的 drift，信噪比不足。

2. **Core distinct pairs 不受影响**：K≥3 和 K≥4 的 robust pairs 完全由 distinct 指标驱动，不含 ppl 或 mauve。统一 pair 后这些核心结论不变。

3. **PermG fwd 从 8/8 降到 6/8（s43）**：纯粹因为去掉了 ppl pairs（ppl drift +50527% 信号极强），换成 mauve（drift 仅 ~8%）。这是 apples-to-apples 对比的正确代价。

4. **MMCT wpair 跨 seed 稳定在 75%**：FPR 逆加权后，distinct pairs 的强信号补偿了 mauve 的弱信号。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 498090,
  "duration_api_ms": 464097,
  "num_turns": 55,
  "stop_reason": "end_turn",
  "session_id": "5067784d-e0df-4fea-af4e-29911a648d18",
  "total_cost_usd": 2.6428554999999996,
  "usage": {
    "input_tokens": 41,
    "cache_creation_input_tokens": 128406,
    "cache_read_input_tokens": 2309124,
    "output_tokens": 27311,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 128406,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1160,
        "cache_read_input_tokens": 131032,
        "cache_creation_input_tokens": 9215,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 9215
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2661,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0027760000000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 41,
      "outputTokens": 27311,
      "cacheReadInputTokens": 2309124,
      "cacheCreationInputTokens": 128406,
      "webSearchRequests": 0,
      "costUSD": 2.6400794999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "16f89710-0b9c-4761-ac31-1423ad41a598"
}
```

</details>

---
