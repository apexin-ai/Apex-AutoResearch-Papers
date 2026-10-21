# debug spatial eval 0pct

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_spatial-eval-0pct_20260513T151936_result.json`
- **Structured JSON:** [`7e52ff91c12d88b65018.json`](../../sessions/7e/7e52ff91c12d88b65018.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

代码只在远程服务器上，本地目录是项目管理用的。修复已部署到服务器。

## 诊断结果总结

### 根因：wrapper 完全绕过了 lerobot 官方推理管线的 6 个关键步骤

通过对比 lerobot 官方代码（`LiberoProcessorStep` + `SmolVLAPolicy` + `normalizer_processor` + `unnormalizer_processor`）和我们的 `SmolVLAWrapper`，发现以下 bug：

| Bug | 官方管线 | 我们（修复前） | 影响 |
|-----|---------|--------------|------|
| **图像翻转** | `torch.flip(dims=[2,3])` 翻转 H+W | 无翻转 | 模型看到上下颠倒镜像的场景 |
| **图像尺寸** | `resize_with_pad(512,512)` | `Resize(256,256)` | SigLIP 输入分辨率错误 |
| **图像值域** | `img * 2.0 - 1.0` → [-1,1] | `ToTensor()` → [0,1] | 像素值超出 SigLIP 期望范围 |
| **State 维度** | 8D: pos(3)+axisangle(3)+**gripper(2)** | 6D: pos(3)+axisangle(3) | 缺少夹爪本体感知 |
| **State 归一化** | `(s - mean) / (std + ε)` MEAN_STD | 原始值直接传入 | 输入量级完全错误 |
| **Action 反归一化** | `a * std + mean` MEAN_STD | 模型原始输出 | 动作在标准化空间，不是物理命令 |

### 修复内容

**`smolvla_wrapper.py`** — 完全重写预处理管线：
- 加载 `policy_preprocessor_step_5_normalizer_processor.safetensors` (state 8D mean/std)
- 加载 `policy_postprocessor_step_0_unnormalizer_processor.safetensors` (action 7D mean/std)
- `_preprocess_image`: flip → resize_with_pad 512×512 → normalize [-1,1]
- `_normalize_state` / `_unnormalize_action`: MEAN_STD normalization
- `preprocess_obs`: 接受 8D state，归一化后 pad 到 32D

**`evaluate.py`** — `get_eef_state` → `get_robot_state`：
- 返回 8D: `concat(eef_pos, eef_axisangle, gripper_qpos).float32`

### 验证

测试通过：
- Image: `(1, 3, 512, 512)`, range `[-0.99, 0.98]`
- State: 8D normalized + padded
- Action sample: range `[-1.03, 1.01]`，first action `[0.29, 0.02, -0.18, 0.00, 0.03, -0.02, 1.01]` — 合理

### 下一步

用修复后的 wrapper 重新跑 `vla_only` baseline eval 验证成功率是否恢复到合理水平。

---
