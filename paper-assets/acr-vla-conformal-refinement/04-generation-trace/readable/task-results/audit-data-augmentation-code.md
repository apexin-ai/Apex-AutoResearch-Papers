# audit data augmentation code

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data-augmentation-code_20260513T224539_result.json`
- **Structured JSON:** [`431073778c2a29097606.json`](../../sessions/43/431073778c2a29097606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：代码实际增强 vs 论文声称

### 代码中实际实现的增强（仅 1 种）

**Action noise augmentation（动作噪声）**：在 CRM 输入端（`ma` 和 `uf`，即 CGS 的 mean action 和 uncertainty features）添加高斯噪声，目标不变。具体实现在 `train_crm.py` 训练循环中：

```python
aug_ma = ma[:n_aug] + torch.randn_like(ma[:n_aug]) * ma_noise
aug_uf = uf[:n_aug] + torch.randn_like(uf[:n_aug]) * noise_scale.mean() * 0.1
```

`utils.py` 中还有一个 `synthetic_augmentation` 函数（对 expert action 加噪），但在训练代码中**未被调用**（只是 import 了）。

### 与论文声称的差异

| 论文声称 | 代码实现 | 匹配？ |
|---------|---------|--------|
| Camera viewpoint shifts | **未实现。** 整个代码库中没有任何 viewpoint/camera augmentation 代码。`camera` 仅出现在 evaluate.py 的相机配置参数中 | **不符** |
| Sensor noise | 部分匹配——对 CGS 特征（`ma`, `uf`）加高斯噪声，但不是对原始传感器数据（图像/robot state）加噪 | **勉强** |
| Robot-state perturbation | **未实现。** `robot_state` 仅在推理路径（evaluate.py, smolvla_wrapper.py）中使用，训练时 CRM 的输入是预计算的 CGS 特征，不涉及 robot state 的扰动 | **不符** |

### 核心问题

CRM 训练使用的是**预计算的特征**（Phase 1 冻结 SmolVLA 提取 obs_features + K_samples），增强只发生在 CGS 输出的统计量上（mean action + uncertainty features），而非原始感知层面。论文描述的三种增强暗示了感知级（image/state）的数据增强，但代码实际只做了**特征空间的高斯噪声扰动**这一种。

---
