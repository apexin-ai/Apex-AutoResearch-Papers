# research eikonal diagnosis

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_eikonal_diagnosis_20260521T185810_result.json`
- **Structured JSON:** [`fa20e87f6169f9695bfb.json`](../../sessions/fa/fa20e87f6169f9695bfb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

### 1. Eikonal=0 的根因：**不是 bug，是正常收敛**

从 wandb offline 数据提取了 291 个 logged steps 的 eikonal 值：

| Step | Eikonal | Phase |
|------|---------|-------|
| 2500 | 0.589 | 1 |
| 2700 | 0.00114 | 1 |
| 2800 | 1.56e-4 | 1 |
| 2900 | 4.53e-5 | 1 |
| 17000 | 1.90e-7 | 2 |
| 29900 | 3.94e-6 | 2 |

Eikonal = `((||∇SDF|| - 1)^2).mean()`，目标就是让 SDF 梯度范数趋近 1.0。SDF decoder 是一个很小的 4层 MLP (hidden=256)，在 Phase 1 的前几百步就把 eikonal 从 0.59 压到了 1e-4，之后稳定在 1e-6~1e-7。wandb dashboard 因精度截断显示为 0。

**291 个步中 168 个 < 1e-6 — 这是 eikonal 正则化成功的标志。**

### 2. VRAM 7.5GB 是否合理

- Pi0 base 模型 ~14GB (fp32 safetensors) → bf16 加载 ~7GB
- Phase 1 仅训练 SDF decoder + EE extractor (658K params)，optimizer states 可忽略
- Phase 2 增加 LoRA (33.5M params)，会涨到 ~10-12GB

**7.5GB 对 Phase 1 是合理的**（bf16 模型权重 + 小量 trainable 参数的 optimizer + 激活值）。Phase 2 VRAM 应该更高。

### 3. 无需修复

代码逻辑正确：`return_gradients=True` 始终传入，eikonal 始终计算并记录。`eikonal_weight=0.1` 默认值生效。唯一的"问题"是 wandb 显示精度不足——如果需要观察收敛过程，可以在 wandb panel 中对 eikonal 使用 log scale y轴。

---
