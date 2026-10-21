# SmolVLA → K=10 → CGS → CRM Pipeline Dimension Verification

**Date**: 2026-05-13  
**Server**: autodl-4090 (RTX 4090)  
**Status**: ALL 12 CHECKS PASSED

## 1. SmolVLA 推理 API

### 加载
```python
from lerobot.policies.smolvla.modeling_smolvla import SmolVLAPolicy
policy = SmolVLAPolicy.from_pretrained("lerobot/smolvla_base")
policy.eval().to(device)
```
- 450.0M params, 0.86GB VRAM
- VLM backbone: SmolVLM2-500M-Video-Instruct (16 layers used)

### 输入构造
```python
from lerobot.utils.constants import OBS_LANGUAGE_TOKENS, OBS_LANGUAGE_ATTENTION_MASK
batch = {
    "observation.state": torch.randn(1, 6),               # state
    "observation.images.camera1": torch.randn(1, 3, 256, 256),  # camera 1
    "observation.images.camera2": torch.randn(1, 3, 256, 256),  # camera 2
    "observation.images.camera3": torch.randn(1, 3, 256, 256),  # camera 3
    OBS_LANGUAGE_TOKENS: tokenized_ids,                    # (1, 48) int64
    OBS_LANGUAGE_ATTENTION_MASK: attention_mask,            # (1, 48) bool ← 必须是 bool!
}
```

### 单次推理
```python
policy.reset()
actions = policy._get_action_chunk(batch)  # (1, 50, 6)
```
输出 `(batch, chunk_size=50, action_dim=6)`，内部 padded 到 max_action_dim=32 后 unpad 回 6。

## 2. K=10 采样实现（KV cache 复用）

SmolVLA 的 `num_steps=10` 是 flow matching 的去噪步数，不是采样数。K=10 需要 10 次独立的去噪 pass。

**关键优化**: prefix KV cache（VLM 处理 image+language+state 的结果）可以计算一次，K 次去噪 pass 复用。

```python
from lerobot.policies.smolvla.modeling_smolvla import make_att_2d_masks

# 1) 计算 prefix embeddings + KV cache（一次）
images, img_masks = policy.prepare_images(batch)
state = policy.prepare_state(batch)
prefix_embs, prefix_pad_masks, prefix_att_masks = policy.model.embed_prefix(
    images, img_masks, lang_tokens, lang_masks, state=state
)
prefix_att_2d_masks = make_att_2d_masks(prefix_pad_masks, prefix_att_masks)
prefix_position_ids = torch.cumsum(prefix_pad_masks, dim=1) - 1
_, past_key_values = policy.model.vlm_with_expert.forward(
    attention_mask=prefix_att_2d_masks,
    position_ids=prefix_position_ids,
    past_key_values=None,
    inputs_embeds=[prefix_embs, None],
    use_cache=True, fill_kv_cache=True,
)

# 2) K 次去噪采样
num_steps = 10; dt = -1.0 / num_steps
all_samples = []
for k in range(K):
    noise = policy.model.sample_noise((1, 50, 32), device)
    x_t = noise
    for step in range(num_steps):
        t = 1.0 + step * dt
        time_tensor = torch.tensor(t, device=device).expand(1)
        v_t = policy.model.denoise_step(
            x_t=x_t, prefix_pad_masks=prefix_pad_masks,
            past_key_values=past_key_values, timestep=time_tensor,
        )
        x_t = x_t + dt * v_t
    all_samples.append(x_t[:, :, :action_dim])  # unpad
```

## 3. obs_features 维度和提取

| 层 | 维度 |
|---|---|
| VLM text hidden_size | **960** |
| Expert hidden_size | 720 (960 × 0.75) |
| prefix_embs | (1, 241, 960) — 241 tokens = 3×image_patches + 48 lang + 1 state |
| state_proj | 32 → 960 |

**CRM 的 obs_features**: 取 `prefix_embs` 并 pool over seq_len → (960,) per sample。
或者取 state token 对应的 embedding 作为 obs representation。

## 4. CGS 40D 验证

| 特征 | 维度 | 验证 |
|---|---|---|
| per_dof_stds | H_eff × D = 5 × 6 = **30** | PASS |
| conformal_radii | H_eff = **5** | PASS |
| log_volumes | H_eff = **5** | PASS |
| **CGS total** | **40D** | PASS |

## 5. 推理耗时 (RTX 4090)

| 操作 | 耗时 |
|---|---|
| Model load (cached) | 31.2s |
| K=1 inference | **380.8ms** |
| K=10 with KV cache reuse | **3225.8ms** (322.6ms/sample) |
| K=10 without cache reuse | 7879.3ms (787.9ms/sample) |
| **Cache reuse speedup** | **2.44×** |
| VRAM peak | 0.92GB |

## 6. 完整 Pipeline Shape Flow

```
INPUT:
  image ×3:      (1, 3, 256, 256) → resized to (512, 512)
  instruction:   str → tokenized to (1, 48)
  state:         (1, 6) → padded to (1, 32)
                          ↓
SmolVLA PREFIX (computed ONCE):
  VLM prefix:    (1, 241, 960)   [img+lang+state embeddings]
  KV cache:      16 layer entries
                          ↓
K=10 FLOW MATCHING (10 denoising steps × 10 samples):
  noise:         (1, 50, 32)
  → 10 denoise steps → (1, 50, 32) → unpad → (1, 50, 6)
  × 10 samples = (10, 50, 6)
                          ↓
TRIM to H_eff=5:
  (10, 5, 6)
                          ↓
CGS FEATURES:
  per_dof_stds:    (30,)   [5 steps × 6 DoF]
  conformal_radii: (5,)    [1 per step]
  log_volumes:     (5,)    [1 per step]
  → CGS total:    (40,)
                          ↓
  mean_action:     (30,)   [5 steps × 6 DoF flattened]
                          ↓
CRM INPUT:
  obs_features:    (960,)  [pooled VLM prefix]
  mean_action:     (30,)
  CGS features:    (40,)
  → total:        (1030,)
                          ↓
CRM OUTPUT:
  refined_action:  (30,)  → reshape to (5, 6)
```

## Dimension Check Results

| Check | Actual | Expected | Status |
|---|---|---|---|
| action_dim | 6 | 6 | PASS |
| chunk_size | 50 | 50 | PASS |
| flow_matching_steps | 10 | 10 | PASS |
| K samples shape[0] | 10 | 10 | PASS |
| trimmed shape | (10, 5, 6) | (10, 5, 6) | PASS |
| per_dof_stds dim | 30 | 30 | PASS |
| conformal_radii dim | 5 | 5 | PASS |
| log_volumes dim | 5 | 5 | PASS |
| CGS total dim | 40 | 40 | PASS |
| mean_action dim | 30 | 30 | PASS |
| CRM action+unc input | 70 | 70 | PASS |
| VLM hidden (obs_features) | 960 | 960 | PASS |

**ALL 12 CHECKS PASSED**

## 注意事项

1. **attention_mask 必须是 bool 类型**，不能是 int64，否则 `torch.where` 报错
2. **KV cache 复用 2.44× 加速** — K=10 时仍需 3.2s，实时推理需优化（如批量去噪、减少 num_steps）
3. **VRAM 仅 0.92GB** — 4090 上有充裕空间同时运行 CRM
4. `lerobot.utils.constants` 中的 key 是 `observation.language.tokens`（带点号），不是下划线
