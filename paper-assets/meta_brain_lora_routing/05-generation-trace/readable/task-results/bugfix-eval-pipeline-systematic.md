# bugfix eval pipeline systematic

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_eval_pipeline_systematic_20260516T082810_result.json`
- **Structured JSON:** [`fa6929e863f42ae36e74.json`](../../sessions/fa/fa6929e863f42ae36e74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两路评估均已进入推理阶段，GPU 使用正常：
- **GPU 1** (eval_univ_r16): 35% utilization, 9094 MiB — 正在跑 LIBERO env
- **GPU 2** (spatial 训练): 99%, 12713 MiB — 不受影响
- **GPU 3** (eval_univ_r48): 58% utilization, 9182 MiB — 正在跑 LIBERO env

---

## 最终输出

### 1. API 调查发现

| 项目 | 发现 |
|------|------|
| **Tokenizer** | `PaligemmaTokenizer(max_len=48)` from `openpi.models.tokenizer`; `.tokenize(prompt, state=None)` → `(tokens[48] int64, mask[48] bool)`; PI0 模式用 `state=None` |
| **Observation.from_dict** | 处理 uint8→float32[-1,1] 归一化; 不做 BHWC→BCHW 转换; 期望 `tokenized_prompt` + `tokenized_prompt_mask`（不是 `prompt` 字符串） |
| **STATE_DIM** | `STATE_DIM=32`, `LIBERO_STATE_DIM_RAW=8`; 在 `data_loader.py:43` 定义 |
| **SigLIP** | `get_image_features(pixel_values)` 期望 BCHW `(batch, channels, height, width)` |

### 2. 代码修改 Diff

**5 处修改**：

```diff
 # Import
 from openpi.models.model import Observation
+from openpi.models.tokenizer import PaligemmaTokenizer

 # Constant
 PALIGEMMA_HIDDEN_DIM = 2048
+PI0_STATE_DIM = 32

 # __init__
         self.routing_history: list[np.ndarray] = []
+        self._tokenizer = PaligemmaTokenizer(max_len=48)

 # New method (before infer)
+    def _preprocess_real_obs(self, inputs: dict) -> dict:
+        """Transform LIBERO env observations to PI0 model input format."""
+        import torch.nn.functional as F
+
+        # Tokenize prompt string → tokenized_prompt + tokenized_prompt_mask
+        prompt_str = inputs.pop("prompt", None)
+        if prompt_str is not None:
+            tokens_np, mask_np = self._tokenizer.tokenize(prompt_str)
+            inputs["tokenized_prompt"] = (
+                torch.from_numpy(tokens_np).to(self.device)[None, ...]
+            )
+            inputs["tokenized_prompt_mask"] = (
+                torch.from_numpy(mask_np).to(self.device)[None, ...]
+            )
+
+        # Zero-pad state from LIBERO 8-dim to PI0 32-dim
+        state = inputs["state"]
+        if state.shape[-1] < PI0_STATE_DIM:
+            inputs["state"] = F.pad(state, (0, PI0_STATE_DIM - state.shape[-1]))
+        inputs["state"] = inputs["state"].float()
+
+        # Permute images BHWC → BCHW (SigLIP vision tower expects channels-first)
+        for key in inputs["image"]:
+            img = inputs["image"][key]
+            if img.ndim == 4 and img.shape[-1] in (1, 3):
+                inputs["image"][key] = img.permute(0, 3, 1, 2)
+
+        return inputs

 # infer() call site
         )
+        inputs = self._preprocess_real_obs(inputs)
         observation = Observation.from_dict(inputs)
```

### 3. Dry Run DEBUG 输出

```
[DEBUG] image.base_0_rgb: dtype=torch.uint8, shape=[1, 3, 224, 224], min=3.000, max=189.000    ← BCHW ✓
[DEBUG] image.left_wrist_0_rgb: dtype=torch.uint8, shape=[1, 3, 224, 224], min=13.000, max=122.000 ← BCHW ✓
[DEBUG] image.right_wrist_0_rgb: dtype=torch.uint8, shape=[1, 3, 224, 224], min=0.000, max=0.000
[DEBUG] image_mask.*: dtype=torch.bool, shape=[1]
[DEBUG] state: dtype=torch.float32, shape=[1, 32]       ← 32-dim padded ✓
[DEBUG] tokenized_prompt: dtype=torch.int64, shape=[1, 48]  ← tokenized ✓
[DEBUG] tokenized_prompt_mask: dtype=torch.bool, shape=[1, 48]
```

7/7 perturbation 类型全部完成，每个 220 步，零错误零崩溃。

### 4. 结论：**通过**

### 5. 2 路评估 PID

| 评估 | GPU | PID | tmux session |
|------|-----|-----|---|
| Universal r16 (50 ep) | cuda:1 | **579770** | eval_univ_r16 |
| Universal r48 (50 ep) | cuda:3 | **579847** | eval_univ_r48 |

---
