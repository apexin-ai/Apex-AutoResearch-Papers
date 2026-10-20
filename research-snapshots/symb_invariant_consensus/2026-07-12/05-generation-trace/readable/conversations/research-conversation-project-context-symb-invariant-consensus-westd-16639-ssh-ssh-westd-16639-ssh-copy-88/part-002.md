# Research conversation: <project_context> # 项目: symb_invariant_consensus ## 运行环境 - 服务器名: westd-16639 - SSH 连接命令: ssh westd-16639 # 必须用此命令，~/.ssh — Part 2 of 2

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-project-context-symb-invariant-consensus-westd-16639-ssh-ssh-westd-16639-ssh-copy-88.md) · [Structured JSON](../../../sessions/4b/4b47f8feeea7d0b66c3c.json)

## Round 1

### Tool call

_source line 252 · 2026-05-22T20:23:29.797Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_0157hswV8eN5PZXr5x6y7tMd`</summary>

```json
{
  "server": "westd-16639",
  "command": "cat /tmp/folio_combo_d061.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7a48d4d-a943-4c19-89cc-5c6011c1fc34",
  "isSidechain": false,
  "requestId": "req_011CbJEQDWY2fcatCtMJFixV",
  "type": "assistant",
  "uuid": "0ce52fa4-89fb-407a-93c9-295ffed8c77b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "11ccc702-e627-476f-a5de-a6db6e180e22",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JrukTH4nwiBSKWHxTyZ295",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 123735,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 311,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 123735,
          "cache_creation_input_tokens": 311,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 311
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 253 · 2026-05-22T20:23:30.253Z_

<details><summary>↩ Tool result · `toolu_0157hswV8eN5PZXr5x6y7tMd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loaded 204 FOLIO problems\\n\\nLoading DeBERTa-large-MNLI from /root/autodl-tmp/models/deberta-large-mnli...\\n\\rLoading weights:   0%|          | 0/392 [00:00<?, ?it/s]\\rLoading weights: 100%|██████████| 392/392 [00:00<00:00, 10997.63it/s]\\n  processed 50/204\\n  processed 100/204\\n  processed 150/204\\n  processed 200/204\\n\\nDeBERTa-large-MNLI zero-shot on FOLIO: 101/204 = 49.51%\\nInference time: 58.0s (0.284s/sample)\\nNLI pred distribution: {'False': 99, 'True': 83, 'Unknown': 22}\\nGold distribution: {'False': 63, 'True': 72, 'Unknown': 69}\\n\\n==================================================================================================================================\\nModel                  SC(D061)        NLI   combo_w1      Dw1        pw1   combo_w3      Dw3        pw3   combo_w5      Dw5        pw5\\n==================================================================================================================================\\nMistral-7B                55.88      49.51      56.37    +0.49     1.0000      58.82    +2.94     0.2101      59.80    +3.92     0.2005\\nLLaMA-3.1-8B              66.18      49.51      65.69    -0.49     1.0000      65.20    -0.98     0.8238      64.22    -1.96     0.6076\\nQwen2.5-14B               75.98      49.51      76.96    +0.98     0.5000      75.49    -0.49     1.0000      73.53    -2.45     0.1797\\nQwen3-14B                 83.33      49.51      83.33    +0.00     1.0000      84.80    +1.47     0.2500      83.33    +0.00     1.0000\\n\\nSaved to /root/symb_invariant_consensus/results/folio_zeroshot_nli_combo_d061.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ce52fa4-89fb-407a-93c9-295ffed8c77b",
  "isSidechain": false,
  "promptId": "b7011f93-406d-4183-b4e1-89ef06a7d2b4",
  "type": "user",
  "uuid": "59d890e0-8a98-4e54-842f-2212abb91ba3",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"Loaded 204 FOLIO problems\\\\n\\\\nLoading DeBERTa-large-MNLI from /root/autodl-tmp/models/deberta-large-mnli...\\\\n\\\\rLoading weights:   0%|          | 0/392 [00:00<?, ?it/s]\\\\rLoading weights: 100%|██████████| 392/392 [00:00<00:00, 10997.63it/s]\\\\n  processed 50/204\\\\n  processed 100/204\\\\n  processed 150/204\\\\n  processed 200/204\\\\n\\\\nDeBERTa-large-MNLI zero-shot on FOLIO: 101/204 = 49.51%\\\\nInference time: 58.0s (0.284s/sample)\\\\nNLI pred distribution: {'False': 99, 'True': 83, 'Unknown': 22}\\\\nGold distribution: {'False': 63, 'True': 72, 'Unknown': 69}\\\\n\\\\n==================================================================================================================================\\\\nModel                  SC(D061)        NLI   combo_w1      Dw1        pw1   combo_w3      Dw3        pw3   combo_w5      Dw5        pw5\\\\n==================================================================================================================================\\\\nMistral-7B                55.88      49.51      56.37    +0.49     1.0000      58.82    +2.94     0.2101      59.80    +3.92     0.2005\\\\nLLaMA-3.1-8B              66.18      49.51      65.69    -0.49     1.0000      65.20    -0.98     0.8238      64.22    -1.96     0.6076\\\\nQwen2.5-14B               75.98      49.51      76.96    +0.98     0.5000      75.49    -0.49     1.0000      73.53    -2.45     0.1797\\\\nQwen3-14B                 83.33      49.51      83.33    +0.00     1.0000      84.80    +1.47     0.2500      83.33    +0.00     1.0000\\\\n\\\\nSaved to /root/symb_invariant_consensus/results/folio_zeroshot_nli_combo_d061.json\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"Loaded 204 FOLIO problems\\n\\nLoading DeBERTa-large-MNLI from /root/autodl-tmp/models/deberta-large-mnli...\\n\\rLoading weights:   0%|          | 0/392 [00:00<?, ?it/s]\\rLoading weights: 100%|██████████| 392/392 [00:00<00:00, 10997.63it/s]\\n  processed 50/204\\n  processed 100/204\\n  processed 150/204\\n  processed 200/204\\n\\nDeBERTa-large-MNLI zero-shot on FOLIO: 101/204 = 49.51%\\nInference time: 58.0s (0.284s/sample)\\nNLI pred distribution: {'False': 99, 'True': 83, 'Unknown': 22}\\nGold distribution: {'False': 63, 'True': 72, 'Unknown': 69}\\n\\n==================================================================================================================================\\nModel                  SC(D061)        NLI   combo_w1      Dw1        pw1   combo_w3      Dw3        pw3   combo_w5      Dw5        pw5\\n==================================================================================================================================\\nMistral-7B                55.88      49.51      56.37    +0.49     1.0000      58.82    +2.94     0.2101      59.80    +3.92     0.2005\\nLLaMA-3.1-8B              66.18      49.51      65.69    -0.49     1.0000      65.20    -0.98     0.8238      64.22    -1.96     0.6076\\nQwen2.5-14B               75.98      49.51      76.96    +0.98     0.5000      75.49    -0.49     1.0000      73.53    -2.45     0.1797\\nQwen3-14B                 83.33      49.51      83.33    +0.00     1.0000      84.80    +1.47     0.2500      83.33    +0.00     1.0000\\n\\nSaved to /root/symb_invariant_consensus/results/folio_zeroshot_nli_combo_d061.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  },
  "sourceToolAssistantUUID": "0ce52fa4-89fb-407a-93c9-295ffed8c77b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "11ccc702-e627-476f-a5de-a6db6e180e22",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 254 · 2026-05-22T20:24:00.963Z_

<details><summary>Logged reasoning block</summary>

```text
The FOLIO combo results are complete. Let me summarize:

**DeBERTa-large-MNLI zero-shot on FOLIO**: 49.51% (101/204) - barely above random for a 3-class task (33.3%). The prediction distribution is very skewed: 99 False, 83 True, 22 Unknown. Gold is more balanced: 63F, 72T, 69U. So the model massively under-predicts "Unknown".

**FOLIO combo results (with D061 tiebreaking):**

| Model | SC(D061) | combo w=1 | Δ | p | combo w=3 | Δ | p | combo w=5 | Δ | p |


|-------|---------|-----------|---|---|-----------|---|---|-----------|---|---|
| Mistral-7B | 55.88% | 56.37% | +0.49 | 1.000 | 58.82% | +2.94 | 0.210 | 59.80% | +3.92 | 0.200 |
| LLaMA-3.1-8B | 66.18% | 65.69% | -0.49 | 1.000 | 65.20% | -0.98 | 0.824 | 64.22% | -1.96 | 0.608 |
| Qwen2.5-14B | 75.98% | 76.96% | +0.98 | 0.500 |

Generating results table...

The DeBERTa-large-MNLI model shows a significant performance gap between FOLIO and ProofWriter datasets, likely because FOLIO contains more varied natural language premises that don't align as well with the model's training. Looking at the combined approach results, none of the improvements reach statistical significance—the zero-shot NLI component just isn't strong enough to provide meaningful gains to the semantic composition baseline.

Interestingly, Mistral-7B achieves the best combo improvement at +3.92 percentage points when weighted at 5, which fits the pattern that weaker semantic composition models benefit more from external signals, though this improvement still doesn't reach significance. In contrast, the stronger models like LLaMA, Qwen2.5, and Qwen3 either see no benefit or actually perform worse when combining approaches.

I'm also noticing some discrepancies between the reported scores and what I'm seeing in the combo results—Qwen2.5-14B shows 75.98% on FOLIO D061 rather than the 75.49% from the main table, and Qwen3-14B shows 83.33% instead of 84.80%. These differences suggest I need to verify the baseline scores before finalizing the summary. Looking at the Qwen3-14B results more carefully, the stored and D061 values both show 83.33%, but Table 1 lists 84.80% for the SC column—which actually matches the SICA accuracy from the summary. This suggests the table might have mixed up the SC and SICA values, or the exp_folio_2x2_qwen3 file isn't the actual source for these numbers. I've identified the discrepancy—the Table 1 entry appears to be mixing metrics, likely showing SICA instead of SC for the Qwen3-14B FOLIO result. Now I'm ready to put together the complete analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59d890e0-8a98-4e54-842f-2212abb91ba3",
  "isSidechain": false,
  "requestId": "req_011CbJEQf7A3csQcE9gYpnL3",
  "type": "assistant",
  "uuid": "09040635-cb98-4c1c-af72-7388beba7fd4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "11ccc702-e627-476f-a5de-a6db6e180e22",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nr2uhaBtAYdA1AuNZXV5sq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 124046,
      "output_tokens": 3212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3212,
          "cache_read_input_tokens": 124046,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 255 · 2026-05-22T20:24:26.497Z_

All data collected. Let me compile the complete summary.

---

## Part 1: Table 1 D061 SC 重算结果

### 已确认使用 D061 的条目（无需修改）

| Model × Dataset | Stored SC | D061 SC | Table 1 SC | Match? |
|---|---|---|---|---|
| Mistral-7B × FOLIO (default) | 54.41% | 55.88% | 55.88% | ✓ D061 |
| Mistral-7B × FOLIO (s123) | 53.92% | 54.41% | 54.41% | ✓ D061 |
| Mistral-7B × FOLIO (s456) | 56.37% | 55.88% | 55.88% | ✓ D061 |
| Qwen2.5-14B × PW-D5 | 73.50% | 74.00% | 74.00% | ✓ D061 |
| LLaMA-8B × FOLIO | 66.18% | 66.18% | 66.18% | ✓ 无tie变化 |

### ⚠️ 需要更新的条目（Table 1 仍使用 stored SC）

**1. Mistral-7B × LogiQA (7 samples affected)**
- SC: 51.00% → **50.00%**
- SICA: 51.50% (不变)
- Δ: +0.50 → **+1.50pp**
- p: 1.000 → **0.581**

**2. Qwen2.5-14B × LogiQA (1 sample affected)**
- SC: 78.50% → **79.00%**
- SICA: 78.00% (不变)
- Δ: -0.50 → **-1.00pp**
- p: 1.000 → **0.625**

**3. Qwen3-14B × PW-D5 (9 samples affected)** ← 方向翻转！
- SC: 85.00% → **85.83%**
- SICA: 85.67% (不变)
- Δ: **+0.67 → -0.17pp** (正变负)
- p: 1.000 → 1.000

### ⚠️ 存在 discrepancy 的条目

**Qwen2.5-14B × FOLIO**
- Stored=77.45%, D061=75.98%, Table=75.49%（都不match）
- SICA: stored=75.49%, Table=74.51%（也不match）
- exp036 文件数据和 Table 1 数值不一致，差 1 sample

**Qwen3-14B × FOLIO**
- Stored=83.33%, D061=83.33% (无tie变化), Table=84.80%
- Table 的 "SC=84.80%" 实际上等于 exp_folio_2x2_qwen3 的 **SICA** accuracy
- 疑似 SC/SICA 列值填反

### 无法验证的条目（文件不在 westd-16639）

| Entry | Table SC | Status |
|---|---|---|
| Mistral-7B × PW-D5 | 39.33% | 所有 multi_seed PW 均不匹配 |
| Mistral-7B × FOLIO (s789) | 54.41% | multi_seed=59.31%, 不匹配 |
| LLaMA-8B × StrategyQA | 72.00% | 文件不存在 |
| Qwen2.5-14B × FOLIO ICL | 74.37% | 文件不存在 |
| Qwen2.5-7B × FOLIO | 75.98% | 文件不存在 |
| Degenerate entries | — | 文件不存在 |

---

## Part 2: FOLIO zero-shot DeBERTa combo D061 结果

**DeBERTa-large-MNLI zero-shot standalone**: 49.51% (101/204)
- 预测分布严重偏移：False=99, True=83, Unknown=22 (gold: F=63, T=72, U=69)

| Model × FOLIO | SC(D061) | combo w=1 | Δ | p | combo w=3 | Δ | p | combo w=5 | Δ | p |
|---|---|---|---|---|---|---|---|---|---|---|
| Mistral-7B | 55.88% | 56.37% | +0.49 | 1.000 | 58.82% | +2.94 | 0.210 | 59.80% | +3.92 | 0.201 |
| LLaMA-3.1-8B | 66.18% | 65.69% | -0.49 | 1.000 | 65.20% | -0.98 | 0.824 | 64.22% | -1.96 | 0.608 |
| Qwen2.5-14B | 75.98% | 76.96% | +0.98 | 0.500 | 75.49% | -0.49 | 1.000 | 73.53% | -2.45 | 0.180 |
| Qwen3-14B | 83.33% | 83.33% | +0.00 | 1.000 | 84.80% | +1.47 | 0.250 | 83.33% | +0.00 | 1.000 |

**所有 combo 均不显著**（p > 0.05）。零样本 NLI (49.51%) 太弱，无法改善 FOLIO 上的 SC。

---

## 总结

**必须更新 Table 1 的 3 行：**
1. Mistral-7B × LogiQA: SC 51.00→50.00, Δ +0.50→+1.50
2. Qwen2.5-14B × LogiQA: SC 78.50→79.00, Δ -0.50→-1.00
3. Qwen3-14B × PW-D5: SC 85.00→85.83, **Δ 从 +0.67 翻转为 -0.17**

**需要排查的 2 行：**
1. Qwen2.5-14B × FOLIO: Table 数值和 exp036 数据不一致
2. Qwen3-14B × FOLIO: 疑似 SC/SICA 列填反

结果已保存到 `results/folio_zeroshot_nli_combo_d061.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09040635-cb98-4c1c-af72-7388beba7fd4",
  "isSidechain": false,
  "requestId": "req_011CbJEQf7A3csQcE9gYpnL3",
  "type": "assistant",
  "uuid": "8f4fe07b-cb5f-49ee-a3ac-9c27dd280478",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus",
  "sessionId": "11ccc702-e627-476f-a5de-a6db6e180e22",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nr2uhaBtAYdA1AuNZXV5sq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 124046,
      "output_tokens": 3212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3212,
          "cache_read_input_tokens": 124046,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 764
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 256_

```json
{
  "type": "last-prompt",
  "leafUuid": "8f4fe07b-cb5f-49ee-a3ac-9c27dd280478",
  "sessionId": "11ccc702-e627-476f-a5de-a6db6e180e22"
}
```

---


### Runtime record

_source line 257_

```json
{
  "type": "ai-title",
  "aiTitle": "Recompute Table 1 SC with D061 tiebreaking",
  "sessionId": "11ccc702-e627-476f-a5de-a6db6e180e22"
}
```

---
