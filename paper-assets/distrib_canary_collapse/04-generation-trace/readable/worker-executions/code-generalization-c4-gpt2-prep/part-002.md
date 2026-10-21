# code generalization c4 gpt2 prep — Part 2 of 2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-generalization-c4-gpt2-prep.md) · [Structured JSON](../../../sessions/b2/b2c861b696b2dd374144.json)

## Before a recorded user message

### Task result

_source line 456_

任务完成。总结：

**环境准备结果：**
- **C4 数据集** — 已下载并准备好 `data/c4_5k/`（train:4500, eval:500, prompts:500），从 allenai/c4 第一个 json.gz 分片提取
- **GPT-2-medium** — 已缓存（355M params, vocab 50257）
- **脚本兼容性** — `iterative_train.py` 已完全支持 `--model_name` 和 `--data_dir` 参数，**无需任何修改**

**关键发现：**
- wikitext103_5k/train 实际包含完整 WikiText-103 训练集（~1.8M 样本），而 C4 子集仅 4500 样本。每代训练 5000 steps × bs=4 = 20k 访问时，C4 样本会被遍历 ~4.4 次 vs WikiText 仅覆盖 ~1.1%。这可能影响对比公平性，已在报告中标注。

**产出文件：** `artifacts/generalization_prep.md`，包含：
- 4 个完整训练命令（2 数据 × 2 α）
- 时间估算：每个实验 ~3.5-4.5h，串行 2 组 ~8h
- 推荐先跑 B 组（WikiText + GPT-2-medium），因为与现有 Pythia baseline 直接可比且模型更小更快

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1052523,
  "duration_api_ms": 794718,
  "num_turns": 168,
  "stop_reason": "end_turn",
  "session_id": "d4f0124e-d2fc-4ba0-9d0a-8c13b6f126a7",
  "total_cost_usd": 5.8303037500000015,
  "usage": {
    "input_tokens": 111,
    "cache_creation_input_tokens": 106471,
    "cache_read_input_tokens": 8181218,
    "output_tokens": 42844,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 106471,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 508,
        "cache_read_input_tokens": 117962,
        "cache_creation_input_tokens": 350,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 350
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2476,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002596,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 111,
      "outputTokens": 42844,
      "cacheReadInputTokens": 8181218,
      "cacheCreationInputTokens": 106471,
      "webSearchRequests": 0,
      "costUSD": 5.827707750000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "acdd176e-9f61-4817-831c-fb3136878305"
}
```

</details>

---
