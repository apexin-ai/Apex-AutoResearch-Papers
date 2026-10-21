# code bev aux head

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bev-aux-head_20260520T065627_result.json`
- **Structured JSON:** [`4090e810eb48ae8b0798.json`](../../sessions/40/4090e810eb48ae8b0798.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结如下：

---

## 代码变更清单

### 新增文件
- **`prismatic/models/occ_head.py`** — BEVOccupancyHead (1.2M params) + FocalLoss
  - 输入: `(B, 256, 2176)` fused visual features (projector 前)
  - 架构: Linear(2176→256) → ConvTranspose2d 16→32 → ConvTranspose2d 32→64 → Conv2d → `(B, 1, 64, 64)`
  - 多视角输入自动取第一视角的 256 patches

### 修改文件

**`prismatic/extern/hf/modeling_prismatic.py`** (1 行)
- `_process_vision_features()` 中添加 `self._cached_patch_features = patch_features`，在 projector 投影前缓存原始特征

**`vla-scripts/finetune.py`** (6 处修改)
- 新增 `import`: `BEVOccupancyHead`, `FocalLoss`, `math`
- `FinetuneConfig` 新增 6 个参数: `use_occ_head`, `occ_data_dir`, `occ_loss_weight`(0.01), `occ_loss_decay_steps`(50000), `occ_detach`(True), `occ_resolution`(64)
- 新增 `get_base_model()` helper: 解包 DDP + PEFT 获取基础模型
- `run_forward_pass()`: 新增 occ 参数，在主 loss 后计算 `loss = loss_action + λ_occ * loss_occ`
- `finetune()`: 初始化 occ_head (DDP-wrapped) + 加入 optimizer + metrics + 训练循环 + checkpoint 保存
- Loss 权重指数衰减: `λ = 0.01 × exp(-step / 50000)`

**`prismatic/vla/datasets/datasets.py`** (4 处修改)
- `RLDSBatchTransform`: 新增 `occ_data_dir`, `occ_resolution` 字段
- 新增 `_load_occ_label()`: 从 HDF5 加载 BEV 标签，未找到时 fallback 到全零
- `DummyDataset`: 返回 dummy `occ_labels` (64×64 全零)

**`prismatic/util/data_utils.py`** (1 处修改)
- `PaddedCollatorForActionPrediction`: collate `occ_labels` tensor

### 干跑验证
- BEVOccupancyHead: 输入 `(2, 256, 2176)` → 输出 `(2, 1, 64, 64)` ✓
- 多视角输入 `(2, 512, 2176)` → 正确截取 → `(2, 1, 64, 64)` ✓
- FocalLoss 计算正确，梯度回传正常 ✓
- bfloat16 兼容 ✓
- 所有 5 个文件语法检查通过 ✓
- 33 个集成点全部验证通过 ✓

### 使用方式
```bash
# 启用 occ head 训练
python vla-scripts/finetune.py \
    --use_occ_head true \
    --occ_data_dir /path/to/bev_labels \
    --occ_loss_weight 0.01 \
    --occ_loss_decay_steps 50000 \
    --occ_detach true
```

---
