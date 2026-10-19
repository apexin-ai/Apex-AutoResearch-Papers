# bugfix eval image mask

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_eval_image_mask_20260516T081039_result.json`
- **Structured JSON:** [`2225bf6ff002c2eb4bac.json`](../../sessions/22/2225bf6ff002c2eb4bac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 结论：Dry Run **失败** — 不启动评估

---

### 1. Kill 结果
**ALL_DEAD** — 3 组旧进程（含 tmux wrapper + timeout + python）全部 killed。

---

### 2. 代码修改 diff

**修改前（line 421）：**
```python
lambda x: torch.from_numpy(np.array(x)).to(self.device)[None, ...] if np.issubdtype(np.array(x).dtype, np.number) else x
```

**修改后：**
```python
lambda x: torch.from_numpy(np.array(x)).to(self.device)[None, ...] if (np.issubdtype(np.array(x).dtype, np.number) or np.issubdtype(np.array(x).dtype, np.bool_)) else x
```

**Bool 修复已确认生效** — `image_mask` 各字段成功转为 `tensor([True/False], device='cuda:0')`。

---

### 3. Dry Run 输出 — 新错误

**每个 episode 立即失败，错误一致：**

```
RuntimeError: Given groups=1, weight of size [1152, 3, 14, 14], expected input[1, 224, 224, 3] to have 3 channels, but got 224 channels instead
```

**Traceback 调用链：**
```
meta_brain_assembly.py:313  _run_prefix_probe
  → model._preprocess_observation(observation, train=False)
  → model.embed_prefix(images, img_masks, ...)
  → paligemma_with_expert.embed_image(img)
  → paligemma.model.get_image_features(image)
  → vision_tower(pixel_values)  [SigLIP]
  → embeddings.patch_embedding(pixel_values)  [Conv2d]
  → F.conv2d  ← CRASH
```

---

### 4. Observation 各字段 dtype/shape/值样例

| 字段 | 类型 | dtype | shape | 值样例 |
|------|------|-------|-------|--------|
| `image` | dict | — | — | `{'base_0_rgb': tensor, 'left_wrist_0_rgb': tensor, 'right_wrist_0_rgb': tensor}` |
| `image["base_0_rgb"]` | Tensor | **uint8** | **[1, 224, 224, 3]** (HWC!) | `tensor([[[[180, 165, 147], [180, 164, 146], ...]]])` |
| `image_mask` | dict | — | — | `{'base_0_rgb': tensor, 'left_wrist_0_rgb': tensor, ...}` |
| `image_mask["base_0_rgb"]` | Tensor | bool | [1] | `tensor([True], device='cuda:0')` ✅ |
| `prompt` | str | — | — | `'pick up the black bowl...'` |
| `state` | Tensor | float64 | [1, 8] | `tensor([[...]])` |

---

### 5. 根因分析

Images 以 **uint8 HWC** `[1, 224, 224, 3]` 格式传入。`preprocess_observation_pytorch` 只对**已经是 CHW** 的输入做 permute-back（line 42: `is_channels_first = image.shape[1] == 3`），HWC 输入直接原样通过。SigLIP 的 `patch_embedding` (Conv2d) 期望 CHW `[B, 3, H, W]`。

**两个问题叠加：**
1. **Channel order**: HWC `[1, 224, 224, 3]` 应为 CHW `[1, 3, 224, 224]`
2. **dtype/normalization**: uint8 `[0, 255]` — preprocessing 的 train=False 路径无归一化步骤，SigLIP 通常期望 float32 normalized

此前 bool 标量错误在更早阶段就让代码崩溃，掩盖了这个 channel format 问题。现在 bool 已修复，暴露出图像预处理管线缺少 HWC→CHW 转换 + 归一化。

---

**不启动评估。等待指令。**

---
