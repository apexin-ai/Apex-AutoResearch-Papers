# code smolvla pipeline verify

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_smolvla-pipeline-verify_20260513T033616_result.json`
- **Structured JSON:** [`b8d95fe4e0e5d50ba2ed.json`](../../sessions/b8/b8d95fe4e0e5d50ba2ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**ALL 12 DIMENSION CHECKS PASSED.** 核心发现：

### Architecture
| 参数 | 值 |
|---|---|
| action_dim | 6 |
| chunk_size | 50, H_eff=5 |
| VLM hidden (obs_features) | **960** |
| Expert hidden | 720 |
| Prefix seq_len | 241 tokens |

### K=10 采样
- SmolVLA `num_steps=10` 是去噪步数，K=10 需要 10 次独立 pass
- **KV cache 复用**: prefix 只算一次，K 次 pass 复用 → **2.44× 加速**
- K=10 耗时: 3.2s (cache) vs 7.9s (no cache)

### CGS 维度对齐
- `per_dof_stds`: 30D (5×6) ✓
- `conformal_radii`: 5D ✓
- `log_volumes`: 5D ✓
- CGS total: **40D** ✓
- mean_action: **30D** ✓

### CRM 输入
- obs_features: 960D + mean_action: 30D + CGS: 40D = **1030D total**

### 踩坑
1. `attention_mask` 必须是 `bool` 类型（不是 int64）
2. Key 格式是 `observation.language.tokens`（点号分隔）
3. 加载模型需要 `HF_HUB_OFFLINE=1` 避免 AutoDL 网络超时

---
