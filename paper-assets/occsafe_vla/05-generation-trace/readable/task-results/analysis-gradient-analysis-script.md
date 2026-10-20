# analysis gradient analysis script

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_analysis_script_20260524T185559_result.json`
- **Structured JSON:** [`b8af3786696d34feadd2.json`](../../sessions/b8/b8af3786696d34feadd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已完成并注册。

**产出：**

1. **`same_seed_gradient_analysis.py`** — 主分析脚本，每次运行一个条件。基于现有 `gradient_analysis.py` 改进：
   - 固定 seed=42 确保跨条件数据采样一致
   - 新增 BN running stats drift 分析（提取 occ_head 中 BatchNorm2d 的 running_mean/var 相对初始化的偏移）
   - 输出标准化 JSON，包含 `occ_norm`、`occ_detach`、`bn_drift` 字段
   - 默认路径已预填（data_root、occ_data_dir）

2. **`plot_gradient_comparison.py`** — 可视化脚本，读取 2-4 个条件的 JSON 结果，生成 7 张图：
   - Action gradient norms（DINOv2/SigLIP 分列）
   - OCC gradient norms
   - Gradient amplification ratio（Full/Detach）
   - Cosine similarity
   - Conflict rate
   - BN drift 对比
   - Combined 2×3 summary（论文用）

**运行方式（实验完成后）：**

```bash
# 在 westd-10894 上，逐个条件运行
cd /root/occsafe_vla
conda activate occsafe

# 1. detach_ln (已完成)
python analysis/same_seed_gradient_analysis.py \
  --checkpoint_path /root/autodl-tmp/checkpoints/detach_ln_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
  --condition_name detach_ln --occ_detach true --occ_norm ln \
  --output_dir /root/occsafe_vla/analysis/same_seed_results

# 2-4. 其他条件类似，替换 checkpoint_path 和参数

# 全部完成后生成对比图
python analysis/plot_gradient_comparison.py \
  --results_dir /root/occsafe_vla/analysis/same_seed_results \
  --output_dir /root/occsafe_vla/analysis/same_seed_results/figures
```

**待确认：** `ablation_occ_s0`（Full OCC + BN, seed=42）的 checkpoint 路径在 registry 和当前服务器上未找到，可能在另一台服务器或需要用 `full_occ_retrain_s0` 的 checkpoint。

---
