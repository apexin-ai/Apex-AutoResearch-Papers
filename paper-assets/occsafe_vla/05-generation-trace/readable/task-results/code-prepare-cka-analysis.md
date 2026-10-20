# code prepare cka analysis

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_cka_analysis_20260525T195156_result.json`
- **Structured JSON:** [`93d8e5877dbd811a29db.json`](../../sessions/93/93d8e5877dbd811a29db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CKA 分析准备状态

**脚本路径**: `/root/occsafe_vla/analysis/cka_analysis.py`
- 支持多 checkpoint 对比，linear CKA，per-layer (DINOv2 + SigLIP)
- 输出 JSON (`cka_results.json`) + PDF/PNG 图表 + summary (mean/min)

**Batch runner**: `/root/occsafe_vla/cka_batch_s3.sh`（旧版 4 条件对比，可复用逻辑）

**依赖状态**: OK（h5py, torch, numpy, matplotlib, transformers 均已在 conda env `occsafe` 中安装）

**数据状态**:
- Pretrained baseline: `/root/autodl-tmp/models/openvla-7b` ✅
- LIBERO 数据: `/root/autodl-tmp/libero_datasets/libero_spatial` ✅
- Detach s3 checkpoint: **50000_chkpt 尚未生成**（当前仅有 10000/20000_chkpt），训练仍在进行

**Checkpoint 路径**（来自 `eval_batch_10894.sh` 确认）:
```
/root/autodl-tmp/checkpoints/ablation_occ_detach_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3--50000_chkpt
```

**运行命令模板**（待 50000_chkpt 生成后执行）:

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe

cd /root/occsafe_vla

CUDA_VISIBLE_DEVICES=3 python analysis/cka_analysis.py \
    --pretrained_path /root/autodl-tmp/models/openvla-7b \
    --checkpoint_paths \
        "/root/autodl-tmp/checkpoints/ablation_occ_detach_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3--50000_chkpt" \
    --condition_names "Detach OCC" \
    --libero_data_dir /root/autodl-tmp/libero_datasets/libero_spatial \
    --output_dir /root/autodl-tmp/analysis/cka_detach_s3_v2 \
    --gpu 0 \
    --num_samples 200
```

**待填参数**:
- checkpoint: 等 50000_chkpt 目录生成（当前训练进度在 20k-50k 之间）
- GPU: 命令中 `CUDA_VISIBLE_DEVICES=3` 映射为脚本内 `--gpu 0`，可选任意空闲 GPU

---
