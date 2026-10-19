# ssh verify evaluate inference mode

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-evaluate-inference-mode_20260520T061415_result.json`
- **Structured JSON:** [`3073c4fedc4199449d3d.json`](../../sessions/30/3073c4fedc4199449d3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息已经足够了。

---

```
推理模式: batched（共享 KV cache）
证据代码行: smolvla_wrapper.py:319, 227-268
KV cache: 有，encode_prefix 一次，KV cache repeat_interleave(K) 后所有 K 个 sample 并行去噪
```

### 详细分析

**1. VLA action sampling：batched，共享 KV cache**

核心调用链（`smolvla_wrapper.py`）：

- **L316-319** `get_obs_features_and_samples()`：
  ```python
  obs_feat, kv_cache, pad_masks = self.encode_prefix(...)   # 一次 VLM forward
  samples = self.generate_k_samples_batched(kv_cache, pad_masks, K=K)
  ```

- **L227-268** `generate_k_samples_batched()`：
  - L238-242: KV cache 通过 `repeat_interleave(K, dim=0)` 从 `(B, ...)` 扩展到 `(B*K, ...)`
  - L245: noise shape = `(B*K, chunk_size, max_act_dim)`
  - L247-255: **单个去噪循环**（不是 K 个循环），`B*K` 个 sample 同时走完所有 denoising steps
  - L258: reshape 回 `(B, K, chunk_size, FULL_ACTION_DIM)`

代码中也保留了老版本的 sequential 实现 `generate_k_samples()`（L194-225，`for _ in range(K)` 循环），但 **evaluate.py 调用的是 `_batched` 版本**。

**2. KV cache 复用：有**

`encode_prefix()`（L168-190）做一次 VLM forward pass 并返回 `past_key_values`。`generate_k_samples_batched()` 把这个 cache `repeat_interleave` 到 K 份，所有 K 个 sample 共享同一份 prefix encoding。VLM 编码只做 1 次，不是 K 次。

**3. 各 mode 的调用路径**

| Mode | 采样方式 | CRM | 具体路径 |
|------|----------|-----|----------|
| `vla_only` | `get_obs_features_and_samples(K)` → batched → mean of K samples | 无 | `select_action_vla_only` (evaluate.py ~L155) |
| `crm_perdof` / `acr_vla` / `crm_scalar` / `crm_obs_only` | 同上 batched K=10 → CGS → argmin → CRM refine | 有 | `select_action_crm` (evaluate.py ~L170) |
| `reconvla` | 同上 batched K=10 → scalar Euclidean argmin | 无 CRM | `select_action_reconvla` (evaluate.py ~L200) |
| `random_selection` | 同上 batched K=10 → random pick 1 | 无 | `select_action_random` (evaluate.py ~L215) |
| `adaptive_k` | `get_obs_features_and_samples_adaptive(k_init=2, k_full=10)` → 先 batched 生成 2 个，L2 > threshold 则再 batched 生成 8 个 → fast path: mean of 2; full path: argmin + CRM obs_only | 条件触发 | `select_action_adaptive_k` (evaluate.py ~L295) |

**adaptive_k 细节**：`generate_adaptive_k_samples()`（wrapper L332-366）先调 `generate_k_samples_batched(K=2)`，判断 L2；若超阈值，再调 `generate_k_samples_batched(K=8)` 并 `torch.cat`。两次都复用同一个 KV cache，不重新编码。

**结论：所有 mode 均为 batched + shared KV cache。** 论文中声明的延迟计算可以基于"VLM encode 1 次 + batched denoising"来分析，不需要乘以 K 倍的 VLM forward cost。

---
