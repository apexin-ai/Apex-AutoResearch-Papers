# research eval image pipeline

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_eval_image_pipeline_20260516T082033_result.json`
- **Structured JSON:** [`1eddf2749be4c88fe5e8.json`](../../sessions/1e/1eddf2749be4c88fe5e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Here's the full analysis:

---

## 1. Dry Run 输入格式

**构造代码**: `meta_brain_assembly.py:550-569` (`make_dummy_observation`)

```python
images={
    "base_0_rgb": torch.rand(B, 3, 224, 224, device=device) * 2 - 1,
    ...
}
image_masks={
    "base_0_rgb": torch.tensor([True], device=device),  # shape [1]
    ...
}
```

- **dtype**: float32
- **shape**: `[1, 3, 224, 224]` — **BCHW**
- **值域**: [-1, 1]
- **channel order**: channels-first

**注意**: 这个格式**违反了** openpi 的 Observation 类型注解 `*b h w c`（应为 BHWC），但因 `preprocess_observation_pytorch` 的逻辑恰好能处理 BCHW 输入并保持 BCHW 输出，所以意外通过。

---

## 2. LIBERO env 输出格式

**env 创建**: `evaluate_libero_plus.py:273-274`
```python
env = OffScreenRenderEnv(
    bddl_file_name=..., camera_heights=256, camera_widths=256,
)
```

**obs 提取**: `evaluate_libero_plus.py:207-228` (`obs_to_model_input`)
```python
agentview = obs["agentview_image"]       # uint8, HWC [256, 256, 3]
wrist = obs["robot0_eye_in_hand_image"]  # uint8, HWC [256, 256, 3]
agentview = _resize_with_pad(agentview, 224)  # → uint8, HWC [224, 224, 3]
```

`_resize_with_pad` (`evaluate_libero_plus.py:194-201`): PIL resize → numpy canvas `np.zeros((size, size, 3), dtype=np.uint8)`

返回 dict:
```python
{"observation/image": agentview,         # np.uint8, [224, 224, 3] HWC
 "observation/wrist_image": wrist,       # np.uint8, [224, 224, 3] HWC
 "observation/state": state,             # np.float64, [8]
 "prompt": str(task_description)}        # string
```

---

## 3. preprocess_observation 管道

### 3a. `MetaBrain.infer()` (`meta_brain_assembly.py:380-435`)

1. `_parse_image(img)` — 对 uint8 HWC 无操作（既不是 float，shape[0] 也不是 3）
2. 构建 `inputs` dict，images 仍是 **np.uint8 HWC `[224,224,3]`**，image_mask 是 `np.True_` / `np.False_` 标量
3. **`jax.tree.map` lambda** (`meta_brain_assembly.py:421`):
   ```python
   lambda x: torch.from_numpy(np.array(x)).to(device)[None, ...] if (numeric or bool) else x
   ```
   - images: `np.uint8 [224,224,3]` → `torch.uint8 [224,224,3]` → `[None,...]` → **`[1, 224, 224, 3]` BHWC**
   - image_mask: `np.True_` → `tensor(True)` 0-dim → `[None,...]` → **`tensor([True])` shape `[1]`**
   - prompt: string → 不转换，保持 string

4. **`Observation.from_dict(inputs)`** (`openpi/models/model.py:109-131`):
   - 检测 `torch.uint8` → 转换: `x.to(float32) / 255.0 * 2.0 - 1.0`
   - 输出: **float32 `[1, 224, 224, 3]` BHWC, 值域 [-1, 1]**
   - `tokenized_prompt = data.get("tokenized_prompt")` → **None**（dict 中只有 `"prompt"` key，没有 `"tokenized_prompt"`）

### 3b. `preprocess_observation_pytorch` (`preprocessing_pytorch.py:20-173`)

```python
is_channels_first = image.shape[1] == 3  # shape[1]=224 → False
```

- BHWC 输入 → `is_channels_first = False` → **不 permute**
- shape `[1, 224, 224, 3]`，`image.shape[1:3] = (224, 224)` == `IMAGE_RESOLUTION` → 不 resize
- `train=False` → 不 augment
- `is_channels_first = False` → **不 permute back**
- **输出仍然是 BHWC `[1, 224, 224, 3]`**

### 3c. 对比：dry run 走的路径

- 输入 BCHW `[1, 3, 224, 224]` → `shape[1] == 3` → `is_channels_first = True`
- permute 到 BHWC → 处理 → permute 回 BCHW
- **输出 BCHW `[1, 3, 224, 224]`**

---

## 4. PI0 Observation.from_dict() 期望

**类定义**: `openpi/models/model.py:82-108`

```python
images: dict[str, at.Float[ArrayT, "*b h w c"]]  # ← BHWC
image_masks: dict[str, at.Bool[ArrayT, "*b"]]
state: at.Float[ArrayT, "*b s"]
```

- jaxtyping 注解: `*b h w c` → **BHWC**
- `from_dict` 内置 uint8→float32 转换（`/255*2-1`）
- **不做 permute**

**但 SigLIP 视觉塔实际需要 BCHW**:

`siglip/modeling_siglip.py:273-274`:
```python
_, _, height, width = pixel_values.shape  # 假设 B,C,H,W
patch_embeds = self.patch_embedding(pixel_values)  # Conv2d(in_channels=3, ...)
```

`patch_embedding` 是 `nn.Conv2d(in_channels=config.num_channels=3, ...)`，**必须接收 `[B, 3, H, W]`**。

---

## 5. Gap 分析

### 核心 gap：BHWC vs BCHW

| 阶段 | Dry run | LIBERO eval |
|------|---------|-------------|
| 输入格式 | BCHW `[1,3,224,224]` float32 | BHWC `[1,224,224,3]` float32 |
| `preprocess` 检测 | `shape[1]==3` → True | `shape[1]==224` → False |
| `preprocess` 输出 | BCHW `[1,3,224,224]` ✓ | **BHWC `[1,224,224,3]`** ✗ |
| SigLIP Conv2d | `in_channels` 看到 3 → 正常 | `in_channels` 看到 224 → **crash** |

**`preprocess_observation_pytorch` 的设计缺陷**: 它只"保留原始格式"，不做 BHWC→BCHW 的强制转换。JAX 原版不需要这步（JAX SigLIP 处理 BHWC），但 PyTorch Conv2d 必须 BCHW。

### 4 个 bug 的因果链

1. **string→tensor**: `infer()` 把 `"prompt"` 作为 string 放入 inputs dict，`jax.tree.map` 跳过 string 不转换，`Observation.from_dict()` 找不到 `"tokenized_prompt"` 得到 None。后续 `embed_prefix` 对 `lang_tokens=None` 调用 `embed_language_tokens(None)` 时崩溃。

2. **NCHW/NHWC (BCHW/BHWC)**: 上表所述。`preprocess_observation_pytorch` 不会把 BHWC 转成 BCHW，因为 `is_channels_first` 判定为 False 时不触发 permute。

3. **bool 标量**: `infer()` 中 `image_mask` 用 `np.True_`（numpy 0-dim bool），经 `jax.tree.map` 后变成 `tensor([True])` shape `[1]`。如果后续代码期望 `bool` 标量用于 `if mask:` 判断，`tensor([True])` 在某些上下文会触发 "bool value of Tensor is ambiguous" 错误。

4. **Conv2d channel 不匹配**: 这是 bug #2 的直接后果。SigLIP `patch_embedding = Conv2d(in_channels=3, ...)` 收到 BHWC `[1, 224, 224, 3]`，把 H=224 当 C，报错 `expected 3 channels, got 224`。

### 缺失的转换步骤

从 LIBERO env 到 PI0 模型，**至少缺 3 步**:

1. **Prompt tokenization**: `infer()` 传了 raw string `"prompt"`，但没有调用 PaliGemma tokenizer 把它转成 `tokenized_prompt` (int32 tensor)。Dry run 手动构造了 `torch.randint(0, 10000, (B, 48))`。

2. **State padding**: LIBERO state 是 8 维 (`[eef_pos(3) + axisangle(3) + gripper(2)]`)，但 PI0 期望 32 维 (`STATE_DIM = 32`)。`infer()` 直接传了 `[1, 8]`，没有 zero-pad 到 32。

3. **Image BHWC→BCHW**: `preprocess_observation_pytorch` 应在输出前强制 permute 到 BCHW，但只在 `is_channels_first=True` 时才 permute back（而 BHWC 输入不触发）。

---
