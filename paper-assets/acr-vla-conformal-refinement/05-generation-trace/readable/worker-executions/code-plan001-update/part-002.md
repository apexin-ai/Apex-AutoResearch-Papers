# code plan001 update — Part 2 of 2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

[← Part 1](part-001.md) · [Transcript overview](../code-plan001-update.md) · [Structured JSON](../../../sessions/f6/f6e6149448d5e9475394.json)

## Before a recorded user message

### Assistant

_source line 277_

## 完成总结

### 1. SmolVLA obs_features 维度
- **obs_dim = 960** (VLM text_config.hidden_size，通过 mean-pool prefix hidden states 得到)
- Expert hidden_size = 720 (960 × 0.75)

### 2. 更新的文件
| 文件 | 变更 |
|------|------|
| `src/cgs.py` | action_dim=6, 自动截取 (K, 50, 32)→(K, 5, 6), 输出 40D+30D, 新增 `compute_features_batch`, 使用 `slogdet` 替代 `logdet` |
| `src/crm.py` | action_dim=30, uncertainty_dim=40, obs_dim=960, input_dim=1030 |
| `src/utils.py` | 新增 `load_libero_demos()`, `build_training_samples()`, 维度常量, BENCHMARK_MAP |
| `src/smolvla_wrapper.py` | **新文件** — `SmolVLAWrapper` 封装 obs_features 提取 + K-sample flow-matching 生成, 共享 KV cache |
| `src/train_crm.py` | 完整两阶段训练: `--precompute` 缓存特征 + CRM MSE训练, 含合成增强、cosine LR、checkpoint |
| `src/evaluate.py` | 完整 LIBERO rollout 评估, 支持 `vla_only`/`crm_scalar`/`crm_perdof` 三种 mode |

### 3. CRM 参数量
**337,438** (input 1030D → 256 → 256 → 30D, 残差连接)

### 4. Dry-run 结果
```
CGS OK — uncertainty_features: (40,), mean_action: (30,)
ACI OK
CRM OK — params=337,438, output: (B, 30)
train_crm.py --help ✓
evaluate.py --help ✓
LIBERO data loading OK — 20 trajs, 3020 samples
END_TO_END_TEST_PASSED — SmolVLA load 201s, K=3 sample gen 1.6s
  obs_features: (1, 960), samples: (1, 3, 50, 32)
```

### 5. SmolVLA 推理 API
```python
# 加载
wrapper = SmolVLAWrapper("lerobot/smolvla_base", device="cuda")

# 端到端: raw obs → 960D obs_features + K samples
obs_feat, samples = wrapper.get_obs_features_and_samples(
    agentview_rgb, task_name, joint_states, eye_in_hand_rgb, K=10
)

# 或分步: 先 encode prefix (缓存 KV), 再生成 K 个样本 (复用 KV cache)
obs_feat, kv_cache, pad_masks = wrapper.encode_prefix(images, img_masks, ...)
samples = wrapper.generate_k_samples(kv_cache, pad_masks, K=10)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0b805d77-1682-4478-9ae2-60c517e75463",
  "uuid": "4255f50a-7860-4ef0-ad30-5a8d22fd39bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BindgN4ajdVnekXL5CbBio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 415,
      "cache_read_input_tokens": 138132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 415
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

_source line 278_

## 完成总结

### 1. SmolVLA obs_features 维度
- **obs_dim = 960** (VLM text_config.hidden_size，通过 mean-pool prefix hidden states 得到)
- Expert hidden_size = 720 (960 × 0.75)

### 2. 更新的文件
| 文件 | 变更 |
|------|------|
| `src/cgs.py` | action_dim=6, 自动截取 (K, 50, 32)→(K, 5, 6), 输出 40D+30D, 新增 `compute_features_batch`, 使用 `slogdet` 替代 `logdet` |
| `src/crm.py` | action_dim=30, uncertainty_dim=40, obs_dim=960, input_dim=1030 |
| `src/utils.py` | 新增 `load_libero_demos()`, `build_training_samples()`, 维度常量, BENCHMARK_MAP |
| `src/smolvla_wrapper.py` | **新文件** — `SmolVLAWrapper` 封装 obs_features 提取 + K-sample flow-matching 生成, 共享 KV cache |
| `src/train_crm.py` | 完整两阶段训练: `--precompute` 缓存特征 + CRM MSE训练, 含合成增强、cosine LR、checkpoint |
| `src/evaluate.py` | 完整 LIBERO rollout 评估, 支持 `vla_only`/`crm_scalar`/`crm_perdof` 三种 mode |

### 3. CRM 参数量
**337,438** (input 1030D → 256 → 256 → 30D, 残差连接)

### 4. Dry-run 结果
```
CGS OK — uncertainty_features: (40,), mean_action: (30,)
ACI OK
CRM OK — params=337,438, output: (B, 30)
train_crm.py --help ✓
evaluate.py --help ✓
LIBERO data loading OK — 20 trajs, 3020 samples
END_TO_END_TEST_PASSED — SmolVLA load 201s, K=3 sample gen 1.6s
  obs_features: (1, 960), samples: (1, 3, 50, 32)
```

### 5. SmolVLA 推理 API
```python
# 加载
wrapper = SmolVLAWrapper("lerobot/smolvla_base", device="cuda")

# 端到端: raw obs → 960D obs_features + K samples
obs_feat, samples = wrapper.get_obs_features_and_samples(
    agentview_rgb, task_name, joint_states, eye_in_hand_rgb, K=10
)

# 或分步: 先 encode prefix (缓存 KV), 再生成 K 个样本 (复用 KV cache)
obs_feat, kv_cache, pad_masks = wrapper.encode_prefix(images, img_masks, ...)
samples = wrapper.generate_k_samples(kv_cache, pad_masks, K=10)
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 1380944,
  "duration_api_ms": 1160711,
  "num_turns": 103,
  "stop_reason": "end_turn",
  "session_id": "0b805d77-1682-4478-9ae2-60c517e75463",
  "total_cost_usd": 6.8512535,
  "usage": {
    "input_tokens": 108,
    "cache_creation_input_tokens": 126706,
    "cache_read_input_tokens": 9515154,
    "output_tokens": 51917,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 126706,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 843,
        "cache_read_input_tokens": 138132,
        "cache_creation_input_tokens": 415,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 415
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3209,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003299,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 108,
      "outputTokens": 51917,
      "cacheReadInputTokens": 9515154,
      "cacheCreationInputTokens": 126706,
      "webSearchRequests": 0,
      "costUSD": 6.8479545,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "28598df1-6f71-49b6-9fa3-c51851b444b9"
}
```

</details>

---
