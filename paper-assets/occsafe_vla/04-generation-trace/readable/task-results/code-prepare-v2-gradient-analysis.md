# code prepare v2 gradient analysis

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-v2-gradient-analysis_20260527T034223_result.json`
- **Structured JSON:** [`1dc8b4a7694c0d6f5959.json`](../../sessions/1d/1dc8b4a7694c0d6f5959.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本就绪。以下是完整报告。

---

## 报告

### 脚本

`/root/occsafe_vla/openvla-oft/scripts/v2_gradient_analysis.py` (438 行)

### v2 关键接口差异（vs v1）

- **patch_features 来源**：v2 通过 `_process_vision_features()` 在 `modeling_prismatic.py:447` 缓存到 `self._cached_patch_features`，无需手动 hook vision backbone
- **访问方式**：`get_base_model(vla)._cached_patch_features`，在 VLA forward 之后自动可用
- **OCC head**：直接消费 `patch_features (B, 256, vision_dim)` → `BEVOccupancyHead` → `(B, 1, 64, 64)` logits
- **梯度流**：`occ_detach=False` 时梯度直接通过 patch_features 流回 vision backbone；`occ_detach=True` 时 `.detach()` 截断

### 使用方法

```bash
# Dry-run（已验证通过）
python scripts/v2_gradient_analysis.py --dry_run

# 完整分析（需要 1 张 GPU ~14GB VRAM）
python scripts/v2_gradient_analysis.py \
  --checkpoint_path /root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3_v2--50000_chkpt \
  --condition_name full_occ_ln \
  --num_samples 100 --device cuda:0
```

### 5 个条件的 checkpoint 映射

| Condition | Checkpoint 路径 | 状态 |
|-----------|----------------|------|
| **full_occ_ln** | `full_occ_ln_s3_v2/...--50000_chkpt` | 50k 已完成 |
| **detach_bn** | `ablation_occ_detach_s3_v2/...--50000_chkpt` | 50k 已完成 |
| **full_occ_bn** | `full_occ_bn_v2_s1/...` | 训练中，无 50k |
| **detach_ln** | `detach_ln_v2_s0c/...--10000_chkpt` | 仅 10k |
| **vanilla** | 无 v2 checkpoint | 需要指定 |

### Dry-run 结果

全部 5 个 condition 的 import + 参数解析通过。`ACTION_DIM=7, NUM_ACTIONS_CHUNK=8`。

### 预估运行时间

每个条件：加载模型 ~30s + 100 samples × ~2s/sample ≈ **4 分钟/条件**。5 个条件串行约 20 分钟（单 GPU）。

### 注意事项

- 当前 8 GPU 全忙，不能跑完整分析
- 脚本使用合成数据（随机图像 + 随机 OCC labels）做前向/反向。对于梯度方向和比率的统计分析，合成数据足够（梯度流由模型权重决定）
- 已有的 v1 分析脚本在 `/root/occsafe_vla/scripts/same_seed_gradient_analysis.py`（D056/D057 确认其有 bug），不要使用

---
