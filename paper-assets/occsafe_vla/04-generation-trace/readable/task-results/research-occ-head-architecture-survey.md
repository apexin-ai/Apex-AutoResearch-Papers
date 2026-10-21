# research occ head architecture survey

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_occ-head-architecture-survey_20260522T022018_result.json`
- **Structured JSON:** [`f77ffe99d94968822030.json`](../../sessions/f7/f77ffe99d94968822030.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All critical code read. Here's the architecture report:

---

## OCC Head 架构调研报告

### 1. OCC Head 架构

**文件**: `prismatic/models/occ_head.py`

- **输入**: `(B, N, D)` fused visual features, 取前 256 个 patch（即第一个 view 的 16×16 patch）
  - D = `vision_backbone.embed_dim`（DINOv2 1152 + SigLIP 1152 = **1024+1152=2176**... 实际由 timm 模型决定，代码中直接用 `vla.module.vision_backbone.embed_dim`）
  - 来源: `self._cached_patch_features`，在 `modeling_prismatic.py:447` 的 `_process_vision_features()` 中缓存，是 projector 之前的原始 patch features
- **网络结构**:
  1. `nn.Linear(in_dim → 256)` — 投影层
  2. reshape 为 `(B, 256, 16, 16)` 空间特征图
  3. `ConvTranspose2d(256→128, k4s2p1)` + BN + GELU — 16→32
  4. `ConvTranspose2d(128→64, k4s2p1)` + BN + GELU — 32→64
  5. `Conv2d(64→1, k1)` — 输出层
- **输出**: `(B, 1, 64, 64)` — 单通道 BEV binary occupancy logits

### 2. Loss 设计

**文件**: `prismatic/models/occ_head.py` (FocalLoss class) + `finetune.py:465-474`

- **类型**: Focal Loss（alpha=0.25, gamma=2.0），基于 BCE with logits
- **Weight 配置**:
  - 初始值: `occ_loss_weight`（默认 0.01）
  - 衰减: `occ_weight_now = occ_loss_weight * exp(-batch_idx / occ_loss_decay_steps)`
  - 可选 cutoff: `occ_loss_cutoff_step > 0` 时，cutoff 之后 weight 归零
- **occ_detach 实现** (`finetune.py:468-469`):
  ```python
  if occ_detach:
      patch_features = patch_features.detach()
  ```
  detach 后 occ loss 梯度不回传到 vision backbone，只更新 occ_head 本身

### 3. 数据流

**文件**: `prismatic/vla/datasets/datasets.py`

- **GT 格式**: `(64, 64)` binary float tensor，来自 HDF5 文件中的 `data/{demo_key}/bev_binary` 字段
- **加载方式**:
  1. 启动时从 `occ_index.json` 加载索引（task_name → file + demos 映射）
  2. **预加载全部数据到内存**（`_preload_occ_data()`），cache 为 `_occ_cache[task_name][demo_key] = np.ndarray(T, 64, 64)`
  3. `_load_occ_label()` 通过 task language instruction 匹配 task_name，通过 traj_len 匹配最近 demo，取 `timestep + offset` 对应帧
  4. 缺失时返回 `zeros(64, 64)` fallback
- **Collator**: `PaddedCollatorForActionPrediction` (`data_utils.py:158-160`) 将 `occ_labels` stack 成 `(B, 64, 64)` tensor

### 4. 训练集成点

| 位置 | 行号 | 内容 |
|------|------|------|
| 配置参数 | `finetune.py:90-96` | `use_occ_head`, `occ_data_dir`, `occ_loss_weight`, `occ_loss_decay_steps`, `occ_loss_cutoff_step`, `occ_detach`, `occ_resolution` |
| import | `finetune.py:63` | `from prismatic.models.occ_head import BEVOccupancyHead, FocalLoss` |
| Head 初始化 | `finetune.py:971-988` | `init_module(BEVOccupancyHead, ...)` + `FocalLoss().to(device_id)` |
| 加入 optimizer | `finetune.py:998-999` | occ_head params 加入 trainable_params |
| 数据加载 | `finetune.py:1043` | `occ_data_dir` 传给 `RLDSBatchTransform` |
| Loss weight 调度 | `finetune.py:1108-1114` | 指数衰减 + 可选 cutoff |
| Forward + loss | `finetune.py:465-474` | `base_model._cached_patch_features` → occ_head → focal loss → 加到总 loss |
| Checkpoint 保存 | `finetune.py:685-686` | `torch.save(occ_head.state_dict(), ...)` |
| 日志打印 | `finetune.py:1151` | 每 100 step 打印 occ_loss 和 action_loss |

### 5. 替换为 Depth Head 的改动清单

| 文件 | 改动 |
|------|------|
| **`prismatic/models/occ_head.py`** | 新增 `DepthHead` 类：输入不变 `(B, N, D)`，输出改为 `(B, 1, H, W)` 连续 depth map；移除 FocalLoss，新增 depth loss（L1/SmoothL1/ScaleInvariant）|
| **`vla-scripts/finetune.py:63`** | import 改为 `from prismatic.models.occ_head import DepthHead, DepthLoss`（或新文件 `depth_head.py`）|
| **`vla-scripts/finetune.py:90-96`** | 新增参数 `use_depth_head`, `depth_data_dir`, `depth_loss_weight` 等（或复用 occ 参数改名）|
| **`vla-scripts/finetune.py:971-988`** | 初始化 DepthHead 替换 BEVOccupancyHead；loss_fn 改为 L1/SmoothL1 |
| **`vla-scripts/finetune.py:465-474`** | 输出改为 regression：`depth_pred = depth_head(patch_features)`，loss 计算用 L1 而非 focal，target key 改为 `depth_labels` |
| **`prismatic/vla/datasets/datasets.py`** | `_load_occ_label` 改为 `_load_depth_label`：读 depth map（可能是 .npy/.h5），返回 `(H, W)` float tensor 而非 binary |
| **`prismatic/util/data_utils.py:158-160`** | collator 中 `occ_labels` 改为 `depth_labels` |
| **数据准备** | 需要新的 depth GT 文件（每帧 depth map）和对应的 index json |

**关键不变点**:
- 输入来源不变：仍取 `_cached_patch_features`（vision backbone 的 patch-level 特征）
- Head 架构可复用：Linear projection + ConvTranspose2d upsampling，只需把最后一层改为输出连续值（去掉 sigmoid，或用 ReLU 保证非负）
- `occ_detach` 机制直接复用
- Loss weight 衰减调度逻辑可复用

---
