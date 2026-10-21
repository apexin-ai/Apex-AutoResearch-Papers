# code ced reranker poc — Part 2 of 2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-ced-reranker-poc.md) · [Structured JSON](../../../sessions/06/0674e50c69172cd96bb7.json)

## Before a recorded user message

### Tool result

_source line 239 · 2026-05-15T09:52:05.118Z_

<details><summary>↩ Tool result · `toolu_01HJaQ6W4gq62fMe5LdmND9P`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 17:50:33,502 INFO Preparing dev data...\\n2026-05-15 17:50:33,568 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-15 17:50:33,936 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-15 17:50:34,064 INFO Prepared 985 documents for generation\\n2026-05-15 17:50:34,074 INFO Dev docs to process: 2\\n2026-05-15 17:50:34,075 INFO Sampled generation: 2 total, 0 done, 2 remaining\\n\\rGenerating (sampled):   0%|          | 0/2 [00:00<?, ?it/s]\\rGenerating (sampled):  50%|█████     | 1/2 [00:08<00:08,  8.79s/it]\\rGenerating (sampled): 100%|██████████| 2/2 [00:40<00:00, 22.38s/it]\\rGenerating (sampled): 100%|██████████| 2/2 [00:40<00:00, 20.34s/it]\\n\\rGenerating (greedy):   0%|          | 0/2 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rGenerating (greedy):  50%|��████     | 1/2 [00:05<00:05,  5.83s/it]\\rGenerating (greedy): 100%|██████████| 2/2 [00:39<00:00, 22.14s/it]\\rGenerating (greedy): 100%|██████████| 2/2 [00:39<00:00, 19.69s/it]\\n2026-05-15 17:51:54,145 INFO Generation done: 80.1s (40.04 s/doc)\\n2026-05-15 17:51:54,256 INFO Loading NLI model for CED scoring: cross-encoder/nli-deberta-v3-base\\n2026-05-15 17:51:54,259 INFO Loading NLI model: cross-encoder/nli-deberta-v3-base\\n2026-05-15 17:51:54,752 INFO Entailment index: 1 (id2label={0: 'contradiction', 1: 'entailment', 2: 'neutral'})\\n\\rCED scoring:   0%|          | 0/2 [00:00<?, ?it/s]\\rCED scoring:  50%|█████     | 1/2 [00:01<00:01,  1.64s/it]\\rCED scoring: 100%|██████████| 2/2 [00:05<00:00,  3.23s/it]\\rCED scoring: 100%|██████████| 2/2 [00:05<00:00,  2.99s/it]\\n2026-05-15 17:52:00,827 INFO Evaluating strategies...\\n2026-05-15 17:52:01,454 INFO Loaded 37785 training triples for Ign-F1\\n2026-05-15 17:52:01,484 INFO greedy_baseline: f1=0.4267 evi_f1=0.7500 edcr=0.6970 prec=0.3137 rec=0.6667 preds=51\\n2026-05-15 17:52:01,724 INFO Loaded 37785 training triples for Ign-F1\\n2026-05-15 17:52:01,753 INFO ced_reranker: f1=0.5333 evi_f1=0.7077 edcr=0.7356 prec=0.4444 rec=0.6667 preds=41\\n2026-05-15 17:52:02,271 INFO Loaded 37785 training triples for Ign-F1\\n2026-05-15 17:52:02,301 INFO oracle_reranker: f1=0.9091 evi_f1=0.7368 edcr=0.0345 prec=1.0000 rec=0.8333 preds=25\\n2026-05-15 17:52:02,512 INFO Loaded 37785 training triples for Ign-F1\\n2026-05-15 17:52:02,542 INFO random_baseline: f1=0.5600 evi_f1=0.7037 edcr=0.6042 prec=0.5385 rec=0.5833 preds=26\\n2026-05-15 17:52:02,543 INFO CED-F1 Spearman r=-0.3923 (p=1.33e-01, n=16)\\n2026-05-15 17:52:02,544 INFO Results → /root/autodl-tmp/eval_results/ced_reranker_dryrun/results.json\\n\\n================================================================================\\n  CED-as-Reranker  (N=8, T=0.7, tau=0.5, docs=2)\\n================================================================================\\n  Strategy               rel_f1   evi_f1     EDCR     prec   recall   ign_f1  preds\\n--------------------------------------------------------------------------------\\n  Greedy baseline        0.4267   0.7500   0.6970   0.3137   0.6667   0.4267     51\\n  Random (N=8)           0.5600   0.7037   0.6042   0.5385   0.5833   0.5600     26\\n  CED reranker           0.5333   0.7077   0.7356   0.4444   0.6667   0.5333     41\\n  Oracle (upper)         0.9091   0.7368   0.0345   1.0000   0.8333   0.9091     25\\n--------------------------------------------------------------------------------\\n  CED-F1 Spearman r = -0.3923  (p = 0.133)\\n  CED vs Greedy: Δrel_f1=+0.1067, Δevi_f1=-0.0423\\n  Oracle headroom:  Δrel_f1=+0.4824\\n================================================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "00f54375-a47c-4667-a0ad-9c2d04571af4",
  "uuid": "7b91691b-efba-419c-a926-07f5ed46d4ad",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"2026-05-15 17:50:33,502 INFO Preparing dev data...\\\\n2026-05-15 17:50:33,568 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\\\n2026-05-15 17:50:33,936 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\\\n2026-05-15 17:50:34,064 INFO Prepared 985 documents for generation\\\\n2026-05-15 17:50:34,074 INFO Dev docs to process: 2\\\\n2026-05-15 17:50:34,075 INFO Sampled generation: 2 total, 0 done, 2 remaining\\\\n\\\\rGenerating (sampled):   0%|          | 0/2 [00:00<?, ?it/s]\\\\rGenerating (sampled):  50%|█████     | 1/2 [00:08<00:08,  8.79s/it]\\\\rGenerating (sampled): 100%|██████████| 2/2 [00:40<00:00, 22.38s/it]\\\\rGenerating (sampled): 100%|██████████| 2/2 [00:40<00:00, 20.34s/it]\\\\n\\\\rGenerating (greedy):   0%|          | 0/2 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\\\n\\\\rGenerating (greedy):  50%|��████     | 1/2 [00:05<00:05,  5.83s/it]\\\\rGenerating (greedy): 100%|██████████| 2/2 [00:39<00:00, 22.14s/it]\\\\rGenerating (greedy): 100%|██████████| 2/2 [00:39<00:00, 19.69s/it]\\\\n2026-05-15 17:51:54,145 INFO Generation done: 80.1s (40.04 s/doc)\\\\n2026-05-15 17:51:54,256 INFO Loading NLI model for CED scoring: cross-encoder/nli-deberta-v3-base\\\\n2026-05-15 17:51:54,259 INFO Loading NLI model: cross-encoder/nli-deberta-v3-base\\\\n2026-05-15 17:51:54,752 INFO Entailment index: 1 (id2label={0: 'contradiction', 1: 'entailment', 2: 'neutral'})\\\\n\\\\rCED scoring:   0%|          | 0/2 [00:00<?, ?it/s]\\\\rCED scoring:  50%|█████     | 1/2 [00:01<00:01,  1.64s/it]\\\\rCED scoring: 100%|██████████| 2/2 [00:05<00:00,  3.23s/it]\\\\rCED scoring: 100%|██████████| 2/2 [00:05<00:00,  2.99s/it]\\\\n2026-05-15 17:52:00,827 INFO Evaluating strategies...\\\\n2026-05-15 17:52:01,454 INFO Loaded 37785 training triples for Ign-F1\\\\n2026-05-15 17:52:01,484 INFO greedy_baseline: f1=0.4267 evi_f1=0.7500 edcr=0.6970 prec=0.3137 rec=0.6667 preds=51\\\\n2026-05-15 17:52:01,724 INFO Loaded 37785 training triples for Ign-F1\\\\n2026-05-15 17:52:01,753 INFO ced_reranker: f1=0.5333 evi_f1=0.7077 edcr=0.7356 prec=0.4444 rec=0.6667 preds=41\\\\n2026-05-15 17:52:02,271 INFO Loaded 37785 training triples for Ign-F1\\\\n2026-05-15 17:52:02,301 INFO oracle_reranker: f1=0.9091 evi_f1=0.7368 edcr=0.0345 prec=1.0000 rec=0.8333 preds=25\\\\n2026-05-15 17:52:02,512 INFO Loaded 37785 training triples for Ign-F1\\\\n2026-05-15 17:52:02,542 INFO random_baseline: f1=0.5600 evi_f1=0.7037 edcr=0.6042 prec=0.5385 rec=0.5833 preds=26\\\\n2026-05-15 17:52:02,543 INFO CED-F1 Spearman r=-0.3923 (p=1.33e-01, n=16)\\\\n2026-05-15 17:52:02,544 INFO Results → /root/autodl-tmp/eval_results/ced_reranker_dryrun/results.json\\\\n\\\\n================================================================================\\\\n  CED-as-Reranker  (N=8, T=0.7, tau=0.5, docs=2)\\\\n================================================================================\\\\n  Strategy               rel_f1   evi_f1     EDCR     prec   recall   ign_f1  preds\\\\n--------------------------------------------------------------------------------\\\\n  Greedy baseline        0.4267   0.7500   0.6970   0.3137   0.6667   0.4267     51\\\\n  Random (N=8)           0.5600   0.7037   0.6042   0.5385   0.5833   0.5600     26\\\\n  CED reranker           0.5333   0.7077   0.7356   0.4444   0.6667   0.5333     41\\\\n  Oracle (upper)         0.9091   0.7368   0.0345   1.0000   0.8333   0.9091     25\\\\n--------------------------------------------------------------------------------\\\\n  CED-F1 Spearman r = -0.3923  (p = 0.133)\\\\n  CED vs Greedy: Δrel_f1=+0.1067, Δevi_f1=-0.0423\\\\n  Oracle headroom:  Δrel_f1=+0.4824\\\\n================================================================================\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.31}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"2026-05-15 17:50:33,502 INFO Preparing dev data...\\n2026-05-15 17:50:33,568 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-15 17:50:33,936 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-15 17:50:34,064 INFO Prepared 985 documents for generation\\n2026-05-15 17:50:34,074 INFO Dev docs to process: 2\\n2026-05-15 17:50:34,075 INFO Sampled generation: 2 total, 0 done, 2 remaining\\n\\rGenerating (sampled):   0%|          | 0/2 [00:00<?, ?it/s]\\rGenerating (sampled):  50%|█████     | 1/2 [00:08<00:08,  8.79s/it]\\rGenerating (sampled): 100%|██████████| 2/2 [00:40<00:00, 22.38s/it]\\rGenerating (sampled): 100%|██████████| 2/2 [00:40<00:00, 20.34s/it]\\n\\rGenerating (greedy):   0%|          | 0/2 [00:00<?, ?it/s]The following generation flags are not valid and may be ignored: ['top_p', 'top_k']. Set `TRANSFORMERS_VERBOSITY=info` for more details.\\n\\rGenerating (greedy):  50%|��████     | 1/2 [00:05<00:05,  5.83s/it]\\rGenerating (greedy): 100%|██████████| 2/2 [00:39<00:00, 22.14s/it]\\rGenerating (greedy): 100%|██████████| 2/2 [00:39<00:00, 19.69s/it]\\n2026-05-15 17:51:54,145 INFO Generation done: 80.1s (40.04 s/doc)\\n2026-05-15 17:51:54,256 INFO Loading NLI model for CED scoring: cross-encoder/nli-deberta-v3-base\\n2026-05-15 17:51:54,259 INFO Loading NLI model: cross-encoder/nli-deberta-v3-base\\n2026-05-15 17:51:54,752 INFO Entailment index: 1 (id2label={0: 'contradiction', 1: 'entailment', 2: 'neutral'})\\n\\rCED scoring:   0%|          | 0/2 [00:00<?, ?it/s]\\rCED scoring:  50%|█████     | 1/2 [00:01<00:01,  1.64s/it]\\rCED scoring: 100%|██████████| 2/2 [00:05<00:00,  3.23s/it]\\rCED scoring: 100%|██████████| 2/2 [00:05<00:00,  2.99s/it]\\n2026-05-15 17:52:00,827 INFO Evaluating strategies...\\n2026-05-15 17:52:01,454 INFO Loaded 37785 training triples for Ign-F1\\n2026-05-15 17:52:01,484 INFO greedy_baseline: f1=0.4267 evi_f1=0.7500 edcr=0.6970 prec=0.3137 rec=0.6667 preds=51\\n2026-05-15 17:52:01,724 INFO Loaded 37785 training triples for Ign-F1\\n2026-05-15 17:52:01,753 INFO ced_reranker: f1=0.5333 evi_f1=0.7077 edcr=0.7356 prec=0.4444 rec=0.6667 preds=41\\n2026-05-15 17:52:02,271 INFO Loaded 37785 training triples for Ign-F1\\n2026-05-15 17:52:02,301 INFO oracle_reranker: f1=0.9091 evi_f1=0.7368 edcr=0.0345 prec=1.0000 rec=0.8333 preds=25\\n2026-05-15 17:52:02,512 INFO Loaded 37785 training triples for Ign-F1\\n2026-05-15 17:52:02,542 INFO random_baseline: f1=0.5600 evi_f1=0.7037 edcr=0.6042 prec=0.5385 rec=0.5833 preds=26\\n2026-05-15 17:52:02,543 INFO CED-F1 Spearman r=-0.3923 (p=1.33e-01, n=16)\\n2026-05-15 17:52:02,544 INFO Results → /root/autodl-tmp/eval_results/ced_reranker_dryrun/results.json\\n\\n================================================================================\\n  CED-as-Reranker  (N=8, T=0.7, tau=0.5, docs=2)\\n================================================================================\\n  Strategy               rel_f1   evi_f1     EDCR     prec   recall   ign_f1  preds\\n--------------------------------------------------------------------------------\\n  Greedy baseline        0.4267   0.7500   0.6970   0.3137   0.6667   0.4267     51\\n  Random (N=8)           0.5600   0.7037   0.6042   0.5385   0.5833   0.5600     26\\n  CED reranker           0.5333   0.7077   0.7356   0.4444   0.6667   0.5333     41\\n  Oracle (upper)         0.9091   0.7368   0.0345   1.0000   0.8333   0.9091     25\\n--------------------------------------------------------------------------------\\n  CED-F1 Spearman r = -0.3923  (p = 0.133)\\n  CED vs Greedy: Δrel_f1=+0.1067, Δevi_f1=-0.0423\\n  Oracle headroom:  Δrel_f1=+0.4824\\n================================================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 240_

Dry-run 完全成功。结果：

```
  Strategy               rel_f1   evi_f1     EDCR     prec   recall   ign_f1  preds
  Greedy baseline        0.4267   0.7500   0.6970   0.3137   0.6667   0.4267     51
  Random (N=8)           0.5600   0.7037   0.6042   0.5385   0.5833   0.5600     26
  CED reranker           0.5333   0.7077   0.7356   0.4444   0.6667   0.5333     41
  Oracle (upper)         0.9091   0.7368   0.0345   1.0000   0.8333   0.9091     25
  CED vs Greedy: Δrel_f1=+0.1067
  Oracle headroom: Δrel_f1=+0.4824
```

**报告：**

- **脚本路径**：`/root/autodl-tmp/freige/eval/ced_reranker.py`
- **功能验证**：2 docs dry-run 通过，全流程正常（sampled gen → greedy gen → CED scoring → eval → results.json + console summary）
- **已有 full run (PID 178055)**：旧版脚本在 GPU 0 上跑全部 985 docs，已完成 ~30%（294/985），预估 ~4h 后完成。旧版的 `generations.jsonl` 格式兼容新脚本，可直接 resume
- **速度估算**（单卡 RTX 5090）：
  - Sampled generation (N=8): ~20s/doc → 50 docs ≈ 17min，985 docs ≈ 5.5h
  - Greedy generation: ~6s/doc → 50 docs ≈ 5min
  - CED scoring: ~3s/doc → 50 docs ≈ 2.5min
  - **50 docs 总计 ≈ 25 min 单卡**
- **GPU 需求**：1 张卡足够（Qwen3-4B bf16 ≈ 8GB，deberta-base ≈ 0.5GB）。多卡可通过 `CUDA_VISIBLE_DEVICES` 隔离
- **NLI 模型**：使用已缓存的 `cross-encoder/nli-deberta-v3-base`（任务指定的 `deberta-v3-large-zeroshot-v2.0` 服务器上不存在）
- **注意**：greedy 生成时 transformers 会打 warning（`top_p, top_k` not valid for greedy），不影响结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "00f54375-a47c-4667-a0ad-9c2d04571af4",
  "uuid": "41b89097-91bb-42be-abbc-b5bc256c5de4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VLwLdx33ZUpPKuzwkEUKfu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2277,
      "cache_read_input_tokens": 125882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2277
      },
      "output_tokens": 2,
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

_source line 241_

Dry-run 完全成功。结果：

```
  Strategy               rel_f1   evi_f1     EDCR     prec   recall   ign_f1  preds
  Greedy baseline        0.4267   0.7500   0.6970   0.3137   0.6667   0.4267     51
  Random (N=8)           0.5600   0.7037   0.6042   0.5385   0.5833   0.5600     26
  CED reranker           0.5333   0.7077   0.7356   0.4444   0.6667   0.5333     41
  Oracle (upper)         0.9091   0.7368   0.0345   1.0000   0.8333   0.9091     25
  CED vs Greedy: Δrel_f1=+0.1067
  Oracle headroom: Δrel_f1=+0.4824
```

**报告：**

- **脚本路径**：`/root/autodl-tmp/freige/eval/ced_reranker.py`
- **功能验证**：2 docs dry-run 通过，全流程正常（sampled gen → greedy gen → CED scoring → eval → results.json + console summary）
- **已有 full run (PID 178055)**：旧版脚本在 GPU 0 上跑全部 985 docs，已完成 ~30%（294/985），预估 ~4h 后完成。旧版的 `generations.jsonl` 格式兼容新脚本，可直接 resume
- **速度估算**（单卡 RTX 5090）：
  - Sampled generation (N=8): ~20s/doc → 50 docs ≈ 17min，985 docs ≈ 5.5h
  - Greedy generation: ~6s/doc → 50 docs ≈ 5min
  - CED scoring: ~3s/doc → 50 docs ≈ 2.5min
  - **50 docs 总计 ≈ 25 min 单卡**
- **GPU 需求**：1 张卡足够（Qwen3-4B bf16 ≈ 8GB，deberta-base ≈ 0.5GB）。多卡可通过 `CUDA_VISIBLE_DEVICES` 隔离
- **NLI 模型**：使用已缓存的 `cross-encoder/nli-deberta-v3-base`（任务指定的 `deberta-v3-large-zeroshot-v2.0` 服务器上不存在）
- **注意**：greedy 生成时 transformers 会打 warning（`top_p, top_k` not valid for greedy），不影响结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 780838,
  "duration_api_ms": 630890,
  "num_turns": 88,
  "stop_reason": "end_turn",
  "session_id": "00f54375-a47c-4667-a0ad-9c2d04571af4",
  "total_cost_usd": 4.386691000000001,
  "usage": {
    "input_tokens": 66,
    "cache_creation_input_tokens": 116318,
    "cache_read_input_tokens": 5674163,
    "output_tokens": 32817,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 116318,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 739,
        "cache_read_input_tokens": 125882,
        "cache_creation_input_tokens": 2277,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2277
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1767,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001867,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 66,
      "outputTokens": 32817,
      "cacheReadInputTokens": 5674163,
      "cacheCreationInputTokens": 116318,
      "webSearchRequests": 0,
      "costUSD": 4.384824000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b77a1d5b-4066-4546-b019-8e85bc1dbf93"
}
```

</details>

---
