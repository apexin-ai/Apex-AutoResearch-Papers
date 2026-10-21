# code v2 gradient dryrun

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v2-gradient-dryrun_20260526T183446_result.json`
- **Structured JSON:** [`bafce481cad765f21c44.json`](../../sessions/ba/bafce481cad765f21c44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 脚本路径
- 分析脚本：`/root/occsafe_vla/scripts/run_gradient_analysis_v2.py` (17KB)
- 绘图脚本：`/root/occsafe_vla/scripts/plot_gradient_analysis_v2.py` (15KB)

### D057 要求逐项确认

| # | 要求 | 状态 | 实现 |
|---|---|---|---|
| 1 | 真实 DataLoader | ✅ | `RLDSDataset` 从 `/root/autodl-tmp/data/modified_libero_rlds/libero_spatial_no_noops` 加载 |
| 2 | 逐层 backbone 梯度 | ✅ | `get_layer_groups()` 遍历 `model.vision_backbone.named_parameters()`，按 block 分组 |
| 3a | 每层 action grad norm (mean, std) | ✅ | `torch.autograd.grad(action_loss, all_params)` → `compute_per_layer_grads()` |
| 3b | 每层 occ grad norm（仅 Full OCC） | ✅ | 仅当 `occ_head is not None and not occ_detach` 时计算 |
| 3c | action vs occ cosine similarity（逐层） | ✅ | `F.cosine_similarity` + conflict_rate |
| 3d | cross-condition ratio | ⚠️ | 在 plot 脚本中做后处理（设计合理） |
| 4 | ≥200 样本 | ✅ | `--num_samples` 默认值 200 |
| 5 | 50K checkpoint | ✅ | 用户通过 `--checkpoint_dir` 指定 |
| 6 | 输出格式 | ✅ | JSON（summary + raw 两个文件） |

### Dry-run 验证（无 GPU 可用，仅静态检查）

| 检查项 | 结果 |
|---|---|
| AST 语法 | ✅ |
| `--help` | ✅ |
| 全部 13 个 import | ✅ |
| 数据路径存在 | ✅ |
| OCC 数据路径存在 | ✅ |
| 3 个条件的 50K checkpoint + occ_head 文件 | ✅ |

### 注意：缺少 Vanilla v2 checkpoint

`/root/autodl-tmp/checkpoints/` 中**无 vanilla_v2 目录**。可能正在训练中。现有 50K v2 checkpoints：
- `full_occ_ln_s3_v2` ✅
- `ablation_occ_detach_s3_v2` ✅
- `mvp_occ_s3_v2`（有 occ_head，不是 vanilla）

### 运行命令模板

```bash
ENV="source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft"
OUT="/root/occsafe_vla/artifacts/gradient_v2"

# 1. Full OCC LN v2
$ENV && python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3_v2--50000_chkpt \
  --condition_name "Full_OCC_LN_v2" --seed 42 --gpu &lt;FREE_GPU> \
  --output_dir $OUT

# 2. Detach LN v2
$ENV && python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/ablation_occ_detach_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3_v2--50000_chkpt \
  --condition_name "Detach_LN_v2" --seed 42 --gpu &lt;FREE_GPU> \
  --output_dir $OUT

# 3. Vanilla v2 — checkpoint 路径待确认
$ENV && python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py \
  --checkpoint_dir /root/autodl-tmp/checkpoints/&lt;VANILLA_V2_EXP_ID>/openvla-7b+...--&lt;VANILLA_V2_EXP_ID>--50000_chkpt \
  --condition_name "Vanilla_v2" --seed 42 --gpu &lt;FREE_GPU> \
  --output_dir $OUT
```

**condition_name 不要包含空格**（用作输出文件名）。3 条可以串行跑同一 GPU，每条约 20-30 分钟（200 samples / bs=4 = 50 batches）。

---
