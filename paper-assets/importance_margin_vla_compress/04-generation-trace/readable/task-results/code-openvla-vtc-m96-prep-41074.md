# code openvla vtc m96 prep 41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla_vtc_m96_prep_41074_20260519T213458_result.json`
- **Structured JSON:** [`87ed6dbfd1b452de0efd.json`](../../sessions/87/87ed6dbfd1b452de0efd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 结果

### M=96 配置
- 路径: `/root/autodl-tmp/importance_margin_vla_compress/configs/openvla_smart_compress_m96.yaml`
- `num_queries: 96`, `output_dir: checkpoints/openvla_sc_m96`, 无 lora 配置 ✓

### Dry-run 验证通过
```
VisionTokenCompressor: 403,177,472 params (5.07% trainable)
Dataset: 273,465 samples
num_compressed_tokens: 96
compression_ratio: 2.67 (256→96)
Forward OK: loss=18.60
Backward OK: grad_norm=825.57
=== DRY RUN PASSED ===
```
GPU 2 已释放。

### M=32/M=64 配置
两个配置均已存在 ✓

### 三套正式启动命令

**M=96** (westd-41074 GPU 2):
```bash
bash -c "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=2 python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m96.yaml"
```

**M=64** (westd-41074 GPU 3):
```bash
bash -c "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=3 python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m64.yaml"
```

**M=32** (westd-27271 GPU 1):
```bash
bash -c "cd /root/autodl-tmp/importance_margin_vla_compress && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export HF_HOME=/root/autodl-tmp/.hf_cache && export HF_HUB_OFFLINE=1 && CUDA_VISIBLE_DEVICES=1 python -u train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml"
```

> **注意**: 启动命令需要 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则数据集路径找不到会报错。原始任务中的 `--seed 42 --gpu 0` 参数该脚本不支持（seed 在 yaml 里配置，GPU 通过 CUDA_VISIBLE_DEVICES 控制）。

---
