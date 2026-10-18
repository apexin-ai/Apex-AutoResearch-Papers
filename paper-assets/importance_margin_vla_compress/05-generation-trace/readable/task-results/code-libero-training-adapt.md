# code libero training adapt

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero_training_adapt_20260516T130739_result.json`
- **Structured JSON:** [`dabf2a9ee231f3be4658.json`](../../sessions/da/dabf2a9ee231f3be4658.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

aloha 配置完全不受影响（`image_shape` 不存在时默认 `(3,256,256)`，alpha 保持 64）。

---

## 完成总结

### 修改清单

**1. `configs/libero_baseline.yaml`** — alpha 64 → 16
- 从 aloha mode collapse 教训出发，降低 LoRA scaling factor（scale=alpha/rank=0.5）

**2. `configs/libero_imm.yaml`** — 无需修改（通过 `_base_` 继承 baseline，alpha 自动变为 16）

**3. `train.py` line 118** — `_adapt_projections` 图像尺寸可配置
- 新增 `image_shape = tuple(features.get("image_shape", (3, 256, 256)))` 
- 替代原来硬编码的 `(3, 256, 256)`
- 向后兼容：aloha 配置无 `image_shape` 字段，自动 fallback 到默认值

### 验证结果

| 检查项 | 状态 |
|--------|------|
| Python 语法 (`py_compile`) | ✅ |
| libero_baseline 配置加载 | ✅ repo_id=HuggingFaceVLA/libero, state=8, action=7, alpha=16 |
| libero_imm 配置继承 | ✅ IMM enabled, delta=0.3, lambda=0.5, gradient_isolation=true |
| aloha 配置向后兼容 | ✅ state=14, action=14, alpha=64 不变 |
| LIBERO 数据集元数据 | ✅ fps=10, 1693 episodes, 273465 frames, 40 tasks |
| 数据集特征匹配 | ✅ image(256×256×3)×2, state(8,), action(7,) |

### 训练前准备

数据集 `HuggingFaceVLA/libero`（~34GB）尚未下载到本地。首次训练时会自动下载，或可提前运行：
```bash
python -c "from lerobot.datasets import LeRobotDataset; LeRobotDataset('HuggingFaceVLA/libero')"
```

---
