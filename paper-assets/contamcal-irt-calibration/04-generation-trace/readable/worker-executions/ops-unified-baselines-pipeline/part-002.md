# ops unified baselines pipeline — Part 2 of 2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../ops-unified-baselines-pipeline.md) · [Structured JSON](../../../sessions/87/8776715fb387d7412e88.json)

## Before a recorded user message

### Task result

_source line 192_

## 完整 Baseline 对比表

**Ground truth** = per-scale d=0 model accuracy, MAE = mean|calibrated - GT|, τ = Kendall(calibrated, GT), * = p<0.05

### MMLU + ARC: J=16 (1.5B+3B, 300 items)

| Method | MMLU MAE | MMLU τ | ARC MAE | ARC τ |
|--------|----------|--------|---------|-------|
| B0: Raw Accuracy | 0.0056 | 0.767* | 0.0067 | 0.695* |
| B1: DRC (oracle) | 0.1955 | 0.178 | 0.2605 | 0.217 |
| B1b: Remove & Rescore | 0.0258 | 0.783* | 0.0143 | 0.673* |
| B3: Vanilla 2PL | 0.0080 | 0.731* | 0.0145 | 0.597* |
| B4: Linear Regression | 0.0096 | 0.751* | 0.0123 | 0.731* |
| B5: Threshold | 0.0373 | -0.030 | 0.0177 | 0.628* |
| B5b: Emperor | 0.0060 | 0.789* | 0.0067 | 0.674* |
| B6: DCR Fuzzy | 0.1081 | 0.654* | 0.3138 | 0.173 |
| ContamCal (2PL+γ) | 0.0091 | 0.731* | 0.0196 | 0.609* |

### GSM8K (excl 3B): J=16 (0.5B+1.5B, 300 items)

| Method | GSM8K MAE | GSM8K τ |
|--------|-----------|---------|
| B0: Raw Accuracy | 0.0213 | 0.647* |
| B1: DRC (oracle) | 0.1456 | 0.415* |
| B1b: Remove & Rescore | 0.0306 | 0.705* |
| B3: Vanilla 2PL | 0.0246 | 0.635* |
| B4: Linear Regression | 0.0702 | 0.654* |
| B5: Threshold | 0.0298 | 0.725* |
| B5b: Emperor | 0.0218 | 0.654* |
| B6: DCR Fuzzy | 0.1575 | 0.654* |
| ContamCal (2PL+γ) | 0.0233 | 0.635* |

### 关键发现

1. **Contamination 对 aggregate accuracy 的影响很小** — MMLU/ARC 上 d=100 模型与 d=0 模型的 accuracy 差异仅 ~0.01，因此 Raw Accuracy 已是强 baseline（MAE=0.006）。这说明 aggregate accuracy 不是衡量 contamination 严重程度的好指标。

2. **ContamCal 的 MAE 未优于 Raw** — 因 contamination 对 aggregate score 的影响太小，IRT 校准反而轻微 overcorrect。ContamCal 的价值在于 γ 估计（检测 contamination 存在）和 per-item 分析，而非 aggregate MAE 改善。

3. **GSM8K 3B d000 异常** — 3B d000 模型 GSM8K accuracy 仅 0.11-0.16（LoRA damage），使 ground truth 无效。排除 3B 后 GSM8K 结果正常（MAE ~0.02）。

4. **γ 值**: MMLU γ=0.698 [-0.42, 1.81], ARC γ=0.727 [0.02, 1.44] (CI excludes 0), GSM8K γ=0.064 (接近 0)

5. **B1 DRC 和 B6 DCR 系统性高估** contamination 影响，MAE > 0.1。

**结果已保存**: `/root/autodl-tmp/exp006/unified_baselines_n16/`
- `all_results.json` — 完整结果含 per-model data
- `final_summary.json` — 汇总表
- 脚本: `exp006/compute_all_baselines_unified.py`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1081341,
  "duration_api_ms": 1030624,
  "num_turns": 74,
  "stop_reason": "end_turn",
  "session_id": "847d89d6-122e-49b2-ae18-0c2f10e27c75",
  "total_cost_usd": 3.9099482500000002,
  "usage": {
    "input_tokens": 45,
    "cache_creation_input_tokens": 143401,
    "cache_read_input_tokens": 3451086,
    "output_tokens": 51340,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 143401,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1212,
        "cache_read_input_tokens": 154958,
        "cache_creation_input_tokens": 284,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 284
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 4324,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.004424,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 45,
      "outputTokens": 51340,
      "cacheReadInputTokens": 3451086,
      "cacheCreationInputTokens": 143401,
      "webSearchRequests": 0,
      "costUSD": 3.90552425,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e646673b-6f3b-4c94-b082-fdba5a36feea"
}
```

</details>

---
