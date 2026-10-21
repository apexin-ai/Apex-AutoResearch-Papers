# code plan001 update

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-update_20260513T033539_result.json`
- **Structured JSON:** [`31a6ccf9fae4c3940b72.json`](../../sessions/31/31a6ccf9fae4c3940b72.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

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

---
